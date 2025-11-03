from django.shortcuts import render, redirect
from django.contrib import messages
from web.models import TaiKhoan, DiaChi

def dangky_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        ho = request.POST.get('lastname')
        ten = request.POST.get('firstname')
        # Đơn giản hóa: tạo địa chỉ tạm nếu chưa có logic địa chỉ
        diachi = DiaChi.objects.first()
        if not diachi:
            diachi = DiaChi.objects.create(MaDC='DC1', Ten=ten, Ho=ho, CongTy='', DiaChi1='', DiaChi2='', QuocGia='', MaZip='', SoDienThoai='', MaDH_id=None)
        if TaiKhoan.objects.filter(Email=email).exists():
            messages.error(request, 'Email đã tồn tại!')
            return render(request, 'Dangky.html')
        TaiKhoan.objects.create(MaTK=email, Email=email, MatKhau=password, MaDC=diachi)
        messages.success(request, 'Đăng ký thành công!')
        return redirect('dangnhap')
    return render(request, 'Dangky.html')
