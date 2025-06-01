import pandas as pd
from web.models import *
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Import data from Excel file'

    def handle(self, *args, **kwargs):
        # import data danh muc
        df2 = pd.read_excel('web/data/Data2.xlsx')
        for index, row in df2.iterrows():
            # Assuming the DataFrame has columns matching the model fields
            danh_muc = DanhMuc(
                MaDM=row['MaDM'],
                TenDM=row['TenDM'],
                DanhMucCha=DanhMuc.objects.get(MaDM=row['DanhMucCha']) if pd.notna(row['DanhMucCha']) else None
            )
            danh_muc.save()
        print("DanhMuc data imported successfully.")

        #import data san pham
        df1 = pd.read_excel('web/data/Data1.xlsx')
        for index, row in df1.iterrows():
            # Assuming the DataFrame has columns matching the model fields
            san_pham = SanPham(
                MaSp=row['MaSP'],
                TenSp=row['TenSP'],
                HangSX=row['HangSX'],
                Gia=row['Gia'],
                CPU=row['CPU'],
                Ram=row['RAM'],
                OCung=row['Ocung'],
                Card=row['Card'],
                DVD=row['DVD'],
                Keyboard=row['Keyboard'],
                PhanLoai=row['PhanLoai'],
                CongIOsau=row['CongIOsau'],
                CongXuatTrinh=row['CongXuatTrinh'],
                Wifi_Bluetooth=row['WIFI_Bluetooth'],
                LAN=row['LAN'],
                CongIOtruoc=row['CongIOtruoc'],
                KichThuoc=row['KichThuoc'],
                KhoiLuong=row['KhoiLuong'],
                HDH=row['HDH'],
                BaoHanh=row['BaoHanh'],
                MaDM=DanhMuc.objects.get(MaDM=row['MaDM']) if pd.notna(row['MaDM']) else None
            )
            san_pham.save()

            print("Data imported successfully.")

        # import data tin tuc
        df3 = pd.read_excel('web/data/Data3.xlsx')
        for index, row in df3.iterrows():
            # Assuming the DataFrame has columns matching the model fields
            tin_tuc = TinTuc(
                MaTT=row['MaTT'],
                TenTT=row['TenTT']
            )
            tin_tuc.save()

            print("TinTuc data imported successfully.") 

        # import data hinh anh
        df4 = pd.read_excel('web/data/Data4.xlsx')
        for index, row in df4.iterrows():
            # Assuming the DataFrame has columns matching the model fields
            hinh_anh = HinhAnh(
                MaHA=row['MaHA'],
                MaSp=SanPham.objects.get(MaSp=row['MaSp']) if pd.notna(row['MaSp']) else None,
                MaDM=DanhMuc.objects.get(MaDM=row['MaDM']) if pd.notna(row['MaDM']) else None,
                MaTT=TinTuc.objects.get(MaTT=row['MaTT']) if pd.notna(row['MaTT']) else None
            )
            hinh_anh.save()

            print("HinhAnh data imported successfully.")

        # import data don hang
        df5 = pd.read_excel('web/data/Data5.xlsx')
        for index, row in df5.iterrows():
            # Assuming the DataFrame has columns matching the model fields
            don_hang = DonHang(
                MaDH=row['MaDH'],
                Ngay=row['Ngay'],
                GiaTri=row['GiaTri'],
                TrangThaiTT=row['TrangThaiTT'],
                TrangThaiGH=row['TrangThaiGH'],
                PTTT=row['PTTT']
            )
            don_hang.save()

            print("DonHang data imported successfully.")


        # import data dia chi
        df7 = pd.read_excel('web/data/Data7.xlsx')
        for index, row in df7.iterrows():
            # Assuming the DataFrame has columns matching the model fields
            dia_chi = DiaChi(
                MaDC=row['MaDC'],
                Ten=row['Ten'],
                Ho=row['Ho'],
                CongTy=row['CongTy'],
                DiaChi1=row['DiaChi1'],
                DiaChi2=row['DiaChi2'],
                QuocGia=row['QuocGia'],
                MaZip=row['MaZip'],
                SoDienThoai=row['SoDienThoai'],
                MaDH=DonHang.objects.get(MaDH=row['MaDH']) if pd.notna(row['MaDH']) else None
            )
            dia_chi.save()

            print("DiaChi data imported successfully.")

        # import data tai khoan
        df8 = pd.read_excel('web/data/Data8.xlsx')
        for index, row in df8.iterrows():
            # Assuming the DataFrame has columns matching the model fields
            tai_khoan = TaiKhoan(
                MaTK=row['MaTK'],
                Email=row['Email'],
                MatKhau=row['MatKhau'],
                MaDC=DiaChi.objects.get(MaDC=row['MaDC']) if pd.notna(row['MaDC']) else None
            )
            tai_khoan.save()

            print("TaiKhoan data imported successfully.")

        #import data gio hang
        df6 = pd.read_excel('web/data/Data6.xlsx') 
        for index, row in df6.iterrows():
            # Assuming the DataFrame has columns matching the model fields
            gio_hang = GioHang(
                MaGH=row['MaGH'],
                TaiKhoan=TaiKhoan.objects.get(MaTK=row['MaTK']) if pd.notna(row['MaTK']) else None
                SanPham=SanPham.objects.get(MaSp=row['MaSp']) if pd.notna(row['MaSp']) else None
            )
            gio_hang.save()
            print("GioHang data imported successfully.")
        
        #import data khuyen mai
        df9 = pd.read_excel('web/data/Data9.xlsx')  
        for index, row in df9.iterrows():
            # Assuming the DataFrame has columns matching the model fields
            khuyen_mai = KhuyenMai(
                MaKM=row['MaKM'],
                NgayBatDau=row['NgayBatDau'],
                NgayKetThuc=row['NgayKetThuc'],
                PhanTram=row['PhanTram'],
                MaSp=SanPham.objects.get(MaSp=row['MaSp']) if pd.notna(row['MaSp']) else None
            )
            khuyen_mai.save()
            print("KhuyenMai data imported successfully.")

        self.stdout.write(self.style.SUCCESS('Successfully imported data from Excel file.'))