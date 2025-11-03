from django.shortcuts import render
from web.models import *

def onlineBill_view(request): 
    danhMuc = DanhMuc.objects.all()
    return render(request, 'onlineBillPage.html', {
        'danhMuc': danhMuc
    })