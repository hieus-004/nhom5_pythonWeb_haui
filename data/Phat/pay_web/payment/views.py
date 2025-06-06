from django.shortcuts import render
from nhom5_web.web.models import GioHang, GioHang_SanPham

def payment_view(request):
    # Giả sử đã có user đăng nhập và lấy được tài khoản
    user = request.user
    gio_hang = GioHang.objects.get(TaiKhoan__Email=user.email)
    items = GioHang_SanPham.objects.filter(GioHang=gio_hang).select_related('SanPham')
    tong_tien = sum(item.SanPham.Gia * item.SoLuong for item in items)
    return render(request, 'payment.html', {
        'cart_items': items,
        'tong_tien': tong_tien,
    })