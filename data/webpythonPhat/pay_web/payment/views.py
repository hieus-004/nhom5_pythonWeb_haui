from django.shortcuts import render
from .models import SanPham, HinhAnh

def payment_view(request):
    sanpham_list = SanPham.objects.all()
    selected_product = None
    product_image = None
    total_price = None

    if request.method == 'POST':
        ma_sp = request.POST.get('ma_sp')
        if ma_sp:
            try:
                selected_product = SanPham.objects.get(MaSp=ma_sp)
                product_image = HinhAnh.objects.filter(MaSp=selected_product).first()
                total_price = selected_product.Gia
            except SanPham.DoesNotExist:
                selected_product = None
                product_image = None
                total_price = None

    context = {
        'sanpham_list': sanpham_list,
        'selected_product': selected_product,
        'product_image': product_image,
        'total_price': total_price,
    }
    return render(request, 'payment.html', context)