from django.urls import path
from .views import *

urlpatterns = [
    path('', homePage, name='homePage'),
    path('timkiem/', timkiem_view, name='timkiem'),
    path('giohang/', giohang_view, name='giohang'),  
    path('gioithieu/', intro_view, name='gioithieu'),  
    path('tintuc/', news_view, name='tintuc'),
    path('hoadon/', onlineBill_view, name='hoadon'),
    path('tuyendung/', recruitment_view, name='tuyendung'),
    path('dangnhap/', dangnhap_view, name='dangnhap'),
    path('dangky/', dangky_view, name='dangky'),
    path('dangxuat/', dangxuat_view, name='dangxuat'),
    path('thongtintaikhoan/', account_info_view, name='thongtintaikhoan'),
    path('diachi/', address_view, name='diachi'),
    path('chitietsp/<str:ma_sp>/', chiTietSp_view, name='chitietsp'),
    path('payment/', payment_view, name='thanhtoan'),
    path('add_to_cart/', add_to_cart_view, name='them_vao_gio'),
    path('update_cart/', update_cart_view, name='cap_nhat_gio_hang'),
]