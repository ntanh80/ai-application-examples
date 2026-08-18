from models.sinh_vien import SinhVien
from services.sinh_vien_service import SinhVienService


def main():
    service = SinhVienService()

    danh_sach = [
        SinhVien("SV001", "Nguyen Van An", 2005, 8.2),
        SinhVien("SV002", "Tran Thi Binh", 2004, 6.8),
        SinhVien("SV003", "Le Minh Chau", 2006, 4.9),
        SinhVien("SV004", "Pham Quoc Dung", 2005, 7.5),
        SinhVien("SV005", "Hoang Mai Linh", 2004, 9.1),
        SinhVien("SV006", "Do Thanh Nam", 2006, 5.6),
    ]

    for sinh_vien in danh_sach:
        service.them_sinh_vien(sinh_vien)

    service.hien_thi_danh_sach(2026)
    service.ghi_ra_csv("ds.csv")
    print("Da ghi danh sach sinh vien vao file ds.csv")


if __name__ == "__main__":
    main()
