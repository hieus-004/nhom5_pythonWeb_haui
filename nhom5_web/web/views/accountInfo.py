from django.shortcuts import render
from web.models import TaiKhoan
from web.models import DanhMuc

def account_info_view(request):
    user_id = request.session.get('user_id')
    danhMuc = DanhMuc.objects.all()
    if not user_id:
        return render(request, 'Dangnhap.html')
    try:
        user = TaiKhoan.objects.get(MaTK=user_id)
        # Lấy tên từ địa chỉ nếu có
        first_name = user.MaDC.Ten if user.MaDC and hasattr(user.MaDC, 'Ten') else ''
    except TaiKhoan.DoesNotExist:
        user = None
        first_name = ''
    return render(request, 'accountInfo.html', {'user': user, 'first_name': first_name, 'danhMuc': danhMuc})
