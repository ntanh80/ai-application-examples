class SinhVien:
    def __init__(self, ma_sv, ho_ten, nam_sinh, diem_tb):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.diem_tb = diem_tb

    def tinh_tuoi(self, nam_hien_tai):
        return nam_hien_tai - self.nam_sinh

    def xep_loai(self):
        if self.diem_tb >= 8.0:
            return "Gioi"
        if self.diem_tb >= 6.5:
            return "Kha"
        if self.diem_tb >= 5.0:
            return "Trung binh"
        return "Yeu"

    def hien_thi_thong_tin(self):
        print("Thong tin sinh vien")
        print(f"Ma sinh vien: {self.ma_sv}")
        print(f"Ho ten: {self.ho_ten}")
        print(f"Nam sinh: {self.nam_sinh}")
        print(f"Diem trung binh: {self.diem_tb}")
        print(f"Xep loai: {self.xep_loai()}")
