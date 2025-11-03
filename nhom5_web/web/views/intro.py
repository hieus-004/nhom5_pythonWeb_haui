from django.shortcuts import render
from web.models import *

def intro_view(request):
    danhMuc = DanhMuc.objects.all()
    return render(request, 'introductionPage.html', {
        'danhMuc': danhMuc
    })