import csv


class SinhVienService:
    def __init__(self):
        self.danh_sach_sinh_vien = []

    def them_sinh_vien(self, sinh_vien):
        self.danh_sach_sinh_vien.append(sinh_vien)

    def hien_thi_danh_sach(self, nam_hien_tai):
        for sinh_vien in self.danh_sach_sinh_vien:
            sinh_vien.hien_thi_thong_tin()
            print(f"Tuoi: {sinh_vien.tinh_tuoi(nam_hien_tai)}")
            print()

    def ghi_ra_csv(self, duong_dan_file):
        with open(duong_dan_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ma_sv", "ho_ten", "nam_sinh", "diem_tb", "xep_loai"])

            for sinh_vien in self.danh_sach_sinh_vien:
                writer.writerow([
                    sinh_vien.ma_sv,
                    sinh_vien.ho_ten,
                    sinh_vien.nam_sinh,
                    sinh_vien.diem_tb,
                    sinh_vien.xep_loai(),
                ])
