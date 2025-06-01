from django.db import models

class DanhMuc(models.Model):
    MaDM = models.CharField(max_length=30, primary_key=True)
    TenDM = models.CharField(max_length=100)
    DanhMucCha = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.TenDM

class SanPham(models.Model):
    MaSp = models.CharField(max_length=30, primary_key=True)
    TenSp = models.CharField(max_length=100)
    HangSX = models.CharField(max_length=100)
    Gia = models.FloatField()
    CPU = models.CharField(max_length=100)
    Ram = models.CharField(max_length=100)
    OCung = models.CharField(max_length=100)
    Card = models.CharField(max_length=100)
    DVD = models.CharField(max_length=100)
    Keyboard = models.CharField(max_length=100)
    PhanLoai = models.CharField(max_length=100)
    CongIOsau = models.CharField(max_length=100)
    CongXuatTrinh = models.CharField(max_length=100)
    Wifi_Bluetooth = models.CharField(max_length=100)
    LAN = models.CharField(max_length=100)
    CongIOtruoc = models.CharField(max_length=100)
    KichThuoc = models.CharField(max_length=100)
    KhoiLuong = models.CharField(max_length=100)
    HDH = models.CharField(max_length=100)
    BaoHanh = models.IntegerField(default=0)
    MaDM = models.ForeignKey(DanhMuc, on_delete=models.CASCADE)

    def __str__(self):
        return self.TenSp

class TinTuc(models.Model):
    MaTT = models.CharField(max_length=30, primary_key=True)
    TenTT = models.CharField(max_length=100)

    def __str__(self):
        return self.TenTT

class HinhAnh(models.Model):
    MaHA = models.CharField(max_length=30, primary_key=True)
    MaSp = models.ForeignKey(SanPham, on_delete=models.CASCADE, null=True, blank=True)
    MaDM = models.ForeignKey(DanhMuc, on_delete=models.CASCADE, null=True, blank=True)
    MaTT = models.ForeignKey(TinTuc, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Hình ảnh {self.MaHA}"

class DonHang(models.Model):
    MaDH = models.CharField(max_length=30, primary_key=True)
    Ngay = models.DateField()
    GiaTri = models.FloatField()
    TrangThaiTT = models.CharField(max_length=100)
    TrangThaiGH = models.CharField(max_length=100)
    PTTT = models.CharField(max_length=100)

    # Thiết lập quan hệ nhiều-nhiều với bảng trung gian
    MaSP = models.ManyToManyField('SanPham', through='DonHang_SanPham')

    def __str__(self):
        return f"Đơn hàng {self.MaDH}"

class DonHang_SanPham(models.Model):
    DonHang = models.ForeignKey(DonHang, on_delete=models.CASCADE)
    SanPham = models.ForeignKey('SanPham', on_delete=models.CASCADE)
    SoLuong = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = (('DonHang', 'SanPham'),)

    def __str__(self):
        return f"{self.DonHang.MaDH} - {self.SanPham.TenSp} x{self.SoLuong}"


class DiaChi(models.Model):
    MaDC = models.CharField(max_length=30, primary_key=True)
    Ten = models.CharField(max_length=100)
    Ho = models.CharField(max_length=100)
    CongTy = models.CharField(max_length=100)
    DiaChi1 = models.CharField(max_length=100)
    DiaChi2 = models.CharField(max_length=100)
    QuocGia = models.CharField(max_length=100)
    MaZip = models.CharField(max_length=20)  # sửa từ IntegerField -> CharField
    SoDienThoai = models.CharField(max_length=100)
    MaDH = models.OneToOneField(DonHang, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Ho} {self.Ten}, {self.DiaChi1}"

class TaiKhoan(models.Model):
    MaTK = models.CharField(max_length=30, primary_key=True)
    Email = models.EmailField()
    MatKhau = models.CharField(max_length=100)
    MaDC = models.ForeignKey(DiaChi, on_delete=models.CASCADE)

    def __str__(self):
        return self.Email

class GioHang(models.Model):
    MaGH = models.CharField(max_length=30, primary_key=True)
    TaiKhoan = models.OneToOneField(TaiKhoan, on_delete=models.CASCADE)
    SanPham = models.ManyToManyField(SanPham, through='GioHang_SanPham')

    def __str__(self):
        return self.MaGH

class GioHang_SanPham(models.Model):
    GioHang = models.ForeignKey(GioHang, on_delete=models.CASCADE)
    SanPham = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    SoLuong = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = (('GioHang', 'SanPham'),)

    def __str__(self):
        return f"{self.GioHang.MaGH} - {self.SanPham.TenSp} x{self.SoLuong}"

class KhuyenMai(models.Model):
    MaKM = models.CharField(max_length=30, primary_key=True)
    NgayBatDau = models.DateField()
    NgayKetThuc = models.DateField()
    PhanTram = models.DecimalField(max_digits=5, decimal_places=2)
    MaSP = models.ForeignKey(SanPham, on_delete=models.CASCADE)

    def __str__(self):
        return f"Giảm {self.PhanTram}% cho {self.MaSP.TenSp}"
