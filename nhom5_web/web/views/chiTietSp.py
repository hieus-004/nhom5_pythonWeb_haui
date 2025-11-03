from django.shortcuts import render, get_object_or_404
from web.models import SanPham, DanhMuc
from django.db.models import Q
import random

def chiTietSp_view(request, ma_sp):
    danhMuc = DanhMuc.objects.all()  # Lấy danh mục như trang chủ
    sanpham = get_object_or_404(SanPham, MaSp=ma_sp)
    # Gợi ý: lấy 4 sản phẩm cùng danh mục, khác mã sp hiện tại, random
    sanpham_goi_y = list(SanPham.objects.filter(MaDM=sanpham.MaDM).exclude(MaSp=ma_sp))
    random.shuffle(sanpham_goi_y)
    sanpham_goi_y = sanpham_goi_y[:4]
    return render(request, 'chiTietSp.html', {
        'sanpham': sanpham,
        'sanpham_goi_y': sanpham_goi_y,
        'danhMuc': danhMuc,
    })