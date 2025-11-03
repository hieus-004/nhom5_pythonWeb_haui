from django.shortcuts import render, get_object_or_404
from web.models import SanPham, HinhAnh, TaiKhoan, GioHang, GioHang_SanPham

def payment_view(request):
    if request.session.get('user_id'):
        tai_khoan = get_object_or_404(TaiKhoan, Email=request.session['user_id'])
        gio_hang, created = GioHang.objects.get_or_create(TaiKhoan=tai_khoan)
        cart_items_qs = GioHang_SanPham.objects.filter(GioHang=gio_hang)
    else:
        cart_items_qs = []
        gio_hang = None
        tai_khoan = None

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        if product_id:
            sanpham = get_object_or_404(SanPham, MaSp=product_id)
            cart_item, created = GioHang_SanPham.objects.get_or_create(
                GioHang=gio_hang, SanPham=sanpham,
                defaults={'SoLuong': quantity}
            )
            if not created:
                cart_item.SoLuong += quantity
                cart_item.save()

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
    }
    return render(request, 'payment.html', context)