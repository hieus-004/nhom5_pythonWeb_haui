from django.shortcuts import render
from web.models import *

def get_all_child_ids(parent_id):
    child_ids = []
    children = DanhMuc.objects.filter(DanhMucCha_id=parent_id)
    for child in children:
        child_ids.append(child.MaDM)
        child_ids.extend(get_all_child_ids(child.MaDM))  # recursion for deeper levels
    return child_ids

def timkiem_view(request):
    keyword = request.GET.get('q', '').strip()
    products = SanPham.objects.all()
    category_id = request.GET.get('category_id')
    
    if keyword:
        products = products.filter(TenSp__icontains=keyword)

    if category_id:
        all_cat_ids = [category_id] + get_all_child_ids(category_id)
        products = products.filter(MaDM_id__in=all_cat_ids)
    # Chuẩn bị danh sách sản phẩm với ảnh đại diện
    product_list = []
    for sp in products:
        image = HinhAnh.objects.filter(MaSp=sp).first()
        image_url = image.MaHA.url if image and hasattr(image.MaHA, 'url') else '/static/img/no-image.png'
        product_list.append({
            'TenSP': sp.TenSp,
            'Gia': sp.Gia,
            'image_url': image_url,
        })

    danhMuc = DanhMuc.objects.all()  # Lấy danh mục như trang chủ

    return render(request, 'Timkiem.html', {
        'danhMuc': danhMuc,
        'products': product_list,  # Đổi thành 'products' để khớp với template
        'keyword': keyword,
    })


