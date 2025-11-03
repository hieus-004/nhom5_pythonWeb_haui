from django.shortcuts import render, redirect
from django.contrib import messages
from web.models import TaiKhoan

def dangnhap_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = TaiKhoan.objects.get(Email=email)
            if user.MatKhau == password:
                # Lưu trạng thái đăng nhập vào session
                request.session['user_id'] = user.MaTK
                request.session['user_email'] = user.Email
                messages.success(request, 'Đăng nhập thành công!')
                return redirect('homePage')
            else:
                messages.error(request, 'Mật khẩu không đúng!')
        except TaiKhoan.DoesNotExist:
            messages.error(request, 'Email không tồn tại!')
        return render(request, 'Dangnhap.html')
    return render(request, 'Dangnhap.html')
