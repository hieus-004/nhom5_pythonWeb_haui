from django import forms
from .models import SanPham

class PaymentForm(forms.Form):
    ho = forms.CharField(label="Họ", max_length=100)
    ten = forms.CharField(label="Tên", max_length=100)
    email = forms.EmailField(label="Email")
    so_dien_thoai = forms.CharField(label="Số điện thoại", max_length=100)
    dia_chi = forms.CharField(label="Địa chỉ", max_length=100)
    san_pham = forms.ModelChoiceField(label="Sản phẩm", queryset=SanPham.objects.all())
    so_luong = forms.IntegerField(label="Số lượng", min_value=1, initial=1)