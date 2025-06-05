from django.shortcuts import render, get_object_or_404, redirect
from web.models import *

def giohang_view(request):
    cart_items = []
    cart_total = 0

    if request.user.is_authenticated:
        # Lấy giỏ hàng từ database
        tai_khoan = get_object_or_404(TaiKhoan, Email=request.user.email)
        gio_hang = GioHang.objects.filter(TaiKhoan=tai_khoan).first()
        if gio_hang:
            for item in GioHang_SanPham.objects.filter(GioHang=gio_hang):
                cart_items.append({
                    'product_name': item.SanPham.TenSp,
                    'quantity': item.SoLuong,
                    'total_price': item.SoLuong * item.SanPham.Gia,
                    'image_url': HinhAnh.objects.filter(MaSp=item.SanPham).first().MaHA.url if HinhAnh.objects.filter(MaSp=item.SanPham).exists() else '/static/img/no-image.png',
                    'MaSp': item.SanPham.MaSp,  # Thêm dòng này
                })
                cart_total += item.SoLuong * item.SanPham.Gia
    else:
        # Lấy giỏ hàng từ session
        cart = request.session.get('cart', {})
        for MaSp, so_luong in cart.items():
            sp = SanPham.objects.filter(MaSp=MaSp).first()
            if sp:
                image = HinhAnh.objects.filter(MaSp=sp).first()
                image_url = image.MaHA.url if image and hasattr(image.MaHA, 'url') else '/static/img/no-image.png'
                cart_items.append({
                    'product_name': sp.TenSp,
                    'quantity': so_luong,
                    'total_price': so_luong * sp.Gia,
                    'image_url': image_url,
                    'MaSp': sp.MaSp,  # Thêm dòng này
                })
                cart_total += so_luong * sp.Gia

    return render(request, 'Giohang.html', {
        'cart_items': cart_items,
        'cart_total': cart_total,
    })

def xoa_san_pham_gio(request):
    if request.method == 'POST':
        product_MaSp = request.POST.get('product_MaSp')
        if request.user.is_authenticated:
            tai_khoan = get_object_or_404(TaiKhoan, Email=request.user.email)
            gio_hang = GioHang.objects.filter(TaiKhoan=tai_khoan).first()
            if gio_hang:
                GioHang_SanPham.objects.filter(GioHang=gio_hang, SanPham__MaSp=product_MaSp).delete()
        else:
            cart = request.session.get('cart', {})
            if product_MaSp in cart:
                del cart[product_MaSp]
                request.session['cart'] = cart
    return redirect('giohang')

def cap_nhat_so_luong(request):
    if request.method == 'POST':
        product_MaSp = request.POST.get('product_MaSp')
        action = request.POST.get('action')
        if request.user.is_authenticated:
            tai_khoan = get_object_or_404(TaiKhoan, Email=request.user.email)
            gio_hang = GioHang.objects.filter(TaiKhoan=tai_khoan).first()
            if gio_hang:
                giohang_sp = GioHang_SanPham.objects.filter(GioHang=gio_hang, SanPham__MaSp=product_MaSp).first()
                if giohang_sp:
                    if action == 'increase':
                        giohang_sp.SoLuong += 1
                    elif action == 'decrease' and giohang_sp.SoLuong > 1:
                        giohang_sp.SoLuong -= 1
                    giohang_sp.save()
        else:
            cart = request.session.get('cart', {})
            if product_MaSp in cart:
                if action == 'increase':
                    cart[product_MaSp] += 1
                elif action == 'decrease' and cart[product_MaSp] > 1:
                    cart[product_MaSp] -= 1
                request.session['cart'] = cart
    return redirect('giohang')

def cap_nhat_so_luong_gio(request):
    if request.method == 'POST':
        product_MaSp = request.POST.get('product_MaSp')
        action = request.POST.get('action')
        if request.user.is_authenticated:
            tai_khoan = get_object_or_404(TaiKhoan, Email=request.user.email)
            gio_hang = GioHang.objects.filter(TaiKhoan=tai_khoan).first()
            if gio_hang:
                giohang_sp = GioHang_SanPham.objects.filter(GioHang=gio_hang, SanPham__MaSp=product_MaSp).first()
                if giohang_sp:
                    if action == 'increase':
                        giohang_sp.SoLuong += 1
                    elif action == 'decrease' and giohang_sp.SoLuong > 1:
                        giohang_sp.SoLuong -= 1
                    giohang_sp.save()
        else:
            cart = request.session.get('cart', {})
            if product_MaSp in cart:
                if action == 'increase':
                    cart[product_MaSp] += 1
                elif action == 'decrease' and cart[product_MaSp] > 1:
                    cart[product_MaSp] -= 1
                request.session['cart'] = cart
    return redirect('giohang')