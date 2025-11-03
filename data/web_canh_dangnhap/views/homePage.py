from django.http import HttpResponse
from django.shortcuts import render
from web.models import *

def index(request):
    return HttpResponse("Hello, world. You're at the tech_part index.")

def homePage(request):
    danhMuc = DanhMuc.objects.all()  # Fetch all categories
    sale_products = SanPham.objects.all() 
    return render(request, 'homePage.html', {
        'danhMuc': danhMuc,
        'sale_products': sale_products
    })
