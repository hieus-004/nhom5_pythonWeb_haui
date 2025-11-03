from django.shortcuts import render
from web.models import *

def news_view(request):
    danhMuc = DanhMuc.objects.all()
    return render(request, 'newsPage.html', {
        'danhMuc': danhMuc
    })