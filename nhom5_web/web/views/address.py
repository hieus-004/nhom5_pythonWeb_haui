from django.shortcuts import render, redirect
from web.models import TaiKhoan, DiaChi, DanhMuc

def address_view(request):
    user_id = request.session.get('user_id')
    danhMuc = DanhMuc.objects.all()
    if not user_id:
        return redirect('dangnhap')
    user = TaiKhoan.objects.get(MaTK=user_id)
    diachi = user.MaDC
    if request.method == 'POST':
        diachi.Ten = request.POST.get('firstname', diachi.Ten)
        diachi.Ho = request.POST.get('lastname', diachi.Ho)
        diachi.CongTy = request.POST.get('company', diachi.CongTy)
        diachi.DiaChi1 = request.POST.get('address', diachi.DiaChi1)
        diachi.QuocGia = request.POST.get('country', diachi.QuocGia)
        diachi.MaZip = request.POST.get('zip', diachi.MaZip)
        diachi.SoDienThoai = request.POST.get('phone', diachi.SoDienThoai)
        diachi.save()
        return render(request, 'address.html', {'user': user, 'diachi': diachi, 'success': True, 'danhMuc': danhMuc})
    return render(request, 'address.html', {'user': user, 'diachi': diachi, 'danhMuc': danhMuc})
