from django.shortcuts import redirect, get_object_or_404
from web.models import *

def them_vao_gio(request):
    if request.method == 'POST':
        product_MaSp = request.POST.get('product_MaSp')
        product = get_object_or_404(SanPham, MaSp=product_MaSp)

        if request.user.is_authenticated:
            # Đã đăng nhập: lưu vào database
            tai_khoan = get_object_or_404(TaiKhoan, Email=request.user.email)
            gio_hang, created = GioHang.objects.get_or_create(TaiKhoan=tai_khoan)
            giohang_sp, created = GioHang_SanPham.objects.get_or_create(GioHang=gio_hang, SanPham=product)
            if not created:
                giohang_sp.SoLuong += 1
            else:
                giohang_sp.SoLuong = 1
            giohang_sp.save()
        else:
            # Chưa đăng nhập: lưu vào session
            cart = request.session.get('cart', {})
            if product_MaSp in cart:
                cart[product_MaSp] += 1
            else:
                cart[product_MaSp] = 1
            request.session['cart'] = cart

    return redirect(request.META.get('HTTP_REFERER', '/'))