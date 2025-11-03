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
                request.session['user_name'] = user.MaDC.Ten if user.MaDC else 'Khách hàng'
                request.session['user_phone'] = user.MaDC.SoDienThoai if user.MaDC else 'Chưa có số điện thoại'
                request.session['user_address1'] = user.MaDC.DiaChi1 if user.MaDC else 'Chưa có địa chỉ'
                request.session['user_address2'] = user.MaDC.DiaChi2 if user.MaDC else 'Chưa có địa chỉ'
                messages.success(request, 'Đăng nhập thành công!')
                return redirect('homePage')
            else:
                messages.error(request, 'Mật khẩu không đúng!')
        except TaiKhoan.DoesNotExist:
            messages.error(request, 'Email không tồn tại!')
        return render(request, 'dangnhap.html')
    return render(request, 'dangnhap.html')
