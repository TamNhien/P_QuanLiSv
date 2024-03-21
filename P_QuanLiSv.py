class SinhVien:
    def __init__(self, ten, lop, id_sv):
        self.ten = ten
        self.lop = lop
        self.id_sv = id_sv
    
    def nhap_thong_tin(self):
        self.ten = input("Nhập tên sinh viên : ")
        self.lop = input("Nhập lớp : ")
        self.id_sv = input("Nhập ID sinh viên : ")

class LopHoc:
    def __init__(self, ten_lop):
        self.ten_lop = ten_lop
        self.danh_sach_sv = []
    
    def them_sinh_vien(self, sinh_vien):
        self.danh_sach_sv.append(sinh_vien)
    
    def sua_sinh_vien(self, id_sv):
        for sv in self.danh_sach_sv:
            if sv.id_sv == id_sv:
                sv.nhap_thong_tin()
                print("Thông tin sinh viên sau khi sửa : ")
                self.hien_thi_sinh_vien(sv)
                return
        print("Không tìm thấy sinh viên có ID : ", id_sv)
    
    def xoa_sinh_vien(self, id_sv):
        for sv in self.danh_sach_sv:
            if sv.id_sv == id_sv:
                self.danh_sach_sv.remove(sv)
                print("Đã xóa sinh viên có ID :", id_sv)
                return
        print("Không tìm thấy sinh viên có ID :", id_sv)
    
    def hien_thi_sinh_vien(self, sinh_vien=None):
        if sinh_vien:
            print(f"Tên : {sinh_vien.ten}, Lớp : {sinh_vien.lop}, ID : {sinh_vien.id_sv}")
        else:
            print(f"Danh sách sinh viên của lớp {self.ten_lop} : ")
            for sv in self.danh_sach_sv:
                self.hien_thi_sinh_vien(sv)

                # Khởi tạo một lớp học
lop_10A = LopHoc("10A")

# Thêm sinh viên vào lớp
sv1 = SinhVien("Hoa", "10A", "SV001")
sv2 = SinhVien("Nam", "10A", "SV002")
lop_10A.them_sinh_vien(sv1)
lop_10A.them_sinh_vien(sv2)

# Hiển thị danh sách sinh viên của lớp
lop_10A.hien_thi_sinh_vien()

# Sửa thông tin sinh viên
lop_10A.sua_sinh_vien("SV002")

# Xóa sinh viên khỏi lớp
lop_10A.xoa_sinh_vien("SV001")

# Hiển thị lại danh sách sinh viên của lớp sau khi sửa và xóa
lop_10A.hien_thi_sinh_vien()