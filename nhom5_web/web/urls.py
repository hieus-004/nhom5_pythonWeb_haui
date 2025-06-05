from django.urls import path
from web.views.homePage import homePage
from web.views.Timkiem import timkiem_view
from web.views.Giohang import (
    giohang_view,
    xoa_san_pham_gio,
    cap_nhat_so_luong_gio,  # đúng tên hàm
)
from web.views.them_vao_gio import them_vao_gio

urlpatterns = [
    path('', homePage, name='homePage'),
    path('giohang/', giohang_view, name='giohang'),
    path('timkiem/', timkiem_view, name='timkiem'),
    path('them-vao-gio/', them_vao_gio, name='them_vao_gio'),
    path('xoa-san-pham-gio/', xoa_san_pham_gio, name='xoa_san_pham_gio'),
    path('cap_nhat_so_luong_gio/', cap_nhat_so_luong_gio, name='cap_nhat_so_luong'),
]