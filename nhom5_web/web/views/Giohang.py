from django.shortcuts import render, get_object_or_404
from web.models import *

def giohang_view(request):
    # Nếu user đã đăng nhập thì lấy theo email, chưa đăng nhập thì trả về giỏ hàng trống
    if request.user.is_authenticated:
        tai_khoan = get_object_or_404(TaiKhoan, Email=request.user.email)
        gio_hang = get_object_or_404(GioHang, TaiKhoan=tai_khoan)
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
    }
    return render(request, 'Giohang.html', context)