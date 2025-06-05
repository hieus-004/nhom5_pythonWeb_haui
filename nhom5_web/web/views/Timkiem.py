from django.shortcuts import render
from web.models import *

def timkiem_view(request):
    keyword = request.GET.get('q', '').strip()
    products = SanPham.objects.all()
    if keyword:
        products = products.filter(TenSp__icontains=keyword)

    # Chuẩn bị danh sách sản phẩm với ảnh đại diện
    product_list = []
    for sp in products:
        image = HinhAnh.objects.filter(MaSp=sp).first()
        image_url = image.MaHA.url if image and hasattr(image.MaHA, 'url') else '/static/img/no-image.png'
        product_list.append({
            'TenSP': sp.TenSp,
            'Gia': sp.Gia,
            'image_url': image_url,
            'MaSp': sp.MaSp,   # BẮT BUỘC phải có dòng này
        })

    danhMuc = DanhMuc.objects.all()  # Lấy danh mục như trang chủ

    return render(request, 'Timkiem.html', {
        'danhMuc': danhMuc,
        'products': product_list,
        'keyword': keyword,
    })