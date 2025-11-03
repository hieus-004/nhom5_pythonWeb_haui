from django.urls import path
from web.views.homePage import homePage
from web.views.Timkiem import timkiem_view
from web.views.Giohang import giohang_view
from web.views.Dangnhap import dangnhap_view
from web.views.Dangky import dangky_view
from web.views.Dangxuat import dangxuat_view
from web.views.accountInfo import account_info_view
from web.views.address import address_view

urlpatterns = [
    path('', homePage, name='homePage'),
    path('timkiem/', timkiem_view, name='timkiem'),
    path('giohang/', giohang_view, name='giohang'),
    path('dangnhap/', dangnhap_view, name='dangnhap'),
    path('dangky/', dangky_view, name='dangky'),
    path('accountInfo/', account_info_view, name='account_info'),
    path('address/', address_view, name='address'),
    path('dangxuat/', dangxuat_view, name='dangxuat'),
]