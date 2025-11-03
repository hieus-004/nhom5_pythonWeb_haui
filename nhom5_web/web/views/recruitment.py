from django.shortcuts import render
from web.models import *

def recruitment_view(request):
    danhMuc = DanhMuc.objects.all()
    return render(request, 'recruitmentPage.html', {
        'danhMuc': danhMuc
    })