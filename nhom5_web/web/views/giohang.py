from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from web.models import *

def giohang_view(request):
    danhMuc = DanhMuc.objects.all()
    # Nếu user đã đăng nhập thì lấy theo email, chưa đăng nhập thì trả về giỏ hàng trống
    if request.session.get('user_id'):
        tai_khoan = get_object_or_404(TaiKhoan, Email=request.session['user_id'])
        gio_hang, created = GioHang.objects.get_or_create(TaiKhoan=tai_khoan,
                                                          defaults={'MaGH': None})
        cart_items_qs = GioHang_SanPham.objects.filter(GioHang=gio_hang)
    else:
        cart_items_qs = []
        gio_hang = None
        tai_khoan = None

    cart_items = []
    cart_total = 0
    for item in cart_items_qs:
        image = HinhAnh.objects.filter(MaSp=item.SanPham).first()
        image_url = image.MaHA.url if image and hasattr(image.MaHA, 'url') else '/static/img/no-image.png'
        product_name = item.SanPham.TenSp
        product_price = item.SanPham.Gia
        quantity = item.SoLuong
        total_price = quantity * product_price
        cart_total += total_price
        cart_items.append({
            'product_id': item.SanPham.MaSp,
            'product_name': product_name,
            'product_price': product_price,
            'image_url': image_url,
            'quantity': quantity,
            'total_price': total_price,
        })

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
        'gio_hang_id': gio_hang.MaGH if gio_hang else None,
        'user_email': tai_khoan.Email if tai_khoan else None,
        'danhMuc': danhMuc,
    }
    return render(request, 'Giohang.html', context)

@csrf_exempt
def add_to_cart_view(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        try:
            product = SanPham.objects.get(MaSp=product_id)
        except SanPham.DoesNotExist:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'Sản phẩm không tồn tại.'})
            return HttpResponseRedirect('/giohang/?error=notfound')
        user_email = request.session.get('user_id')
        if not user_email:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'Bạn cần đăng nhập để thêm vào giỏ hàng.'})
            return HttpResponseRedirect('/giohang/?error=login')
        tai_khoan = TaiKhoan.objects.get(Email=user_email)
        gio_hang, _ = GioHang.objects.get_or_create(TaiKhoan=tai_khoan)
        item, created = GioHang_SanPham.objects.get_or_create(GioHang=gio_hang, SanPham=product)
        if not created:
            item.SoLuong += quantity
        else:
            item.SoLuong = quantity
        item.save()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'message': 'Đã thêm vào giỏ hàng!'})
        return HttpResponseRedirect('/giohang/')
    return HttpResponseRedirect('/giohang/')