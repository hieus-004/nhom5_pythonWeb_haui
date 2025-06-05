from django.urls import path
from web.views.homePage import homePage
from web.views.Timkiem import timkiem_view
from web.views.Giohang import giohang_view
urlpatterns = [
    path('', homePage, name='homePage'),
    path('timkiem/', timkiem_view, name='timkiem'),
    path('giohang/', giohang_view, name='giohang'),  # Thêm dòng này
]