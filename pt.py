'''
PHÂN TÍCH & THIẾT KẾ HỆ THỐNG

1. MỤC TIÊU HỆ THỐNG
- Quản lý hồ sơ bệnh án bằng List chứa String.
- Chuẩn hóa dữ liệu đầu vào bằng các hàm xử lý chuỗi.
- Tách nhỏ nghiệp vụ thành nhiều Function độc lập.
- Cập nhật dữ liệu bệnh nhân an toàn.
- Phân loại bệnh nhân theo độ tuổi.

2. CẤU TRÚC DỮ LIỆU

Mỗi hồ sơ bệnh nhân được lưu dưới dạng:
"MãBN-TênBN-NămSinh-ChẩnĐoán"

Ví dụ:
"BN001-Nguyen Van A-1985-Viem Phoi"

Danh sách lưu trữ:
patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi"
]

3. THIẾT KẾ HÀM

--------------------------------------------------
Tên hàm:
split_record(record)

Input:
- record (str)

Output:
- list

Mô tả xử lý:
- Dùng split("-")
- Tách hồ sơ thành 4 phần
--------------------------------------------------

--------------------------------------------------
Tên hàm:
display_records(records)

Input:
- records (list)

Output:
- None

Mô tả xử lý:
- Kiểm tra danh sách rỗng
- Duyệt từng hồ sơ
- split("-") để lấy thông tin
- In dữ liệu dạng bảng căn lề
--------------------------------------------------

--------------------------------------------------
Tên hàm:
normalize_patient_id(patient_id)

Input:
- patient_id (str)

Output:
- str

Mô tả xử lý:
- strip()
- upper()
- replace(" ", "")
--------------------------------------------------

--------------------------------------------------
Tên hàm:
normalize_name(name)

Input:
- name (str)

Output:
- str

Mô tả xử lý:
- replace("-", " ")
- title()
--------------------------------------------------

--------------------------------------------------
Tên hàm:
normalize_diagnosis(diagnosis)

Input:
- diagnosis (str)

Output:
- str

Mô tả xử lý:
- replace("-", " ")
- capitalize()
--------------------------------------------------

--------------------------------------------------
Tên hàm:
is_valid_birth_year(year)

Input:
- year (str)

Output:
- bool

Mô tả xử lý:
- Kiểm tra isdigit()
- Ép kiểu int
- Kiểm tra khoảng:
    1900 -> năm hiện tại
--------------------------------------------------

--------------------------------------------------
Tên hàm:
find_patient_index(records, patient_id)

Input:
- records (list)
- patient_id (str)

Output:
- int

Mô tả xử lý:
- Duyệt danh sách
- Kiểm tra startswith(patient_id)
- Nếu tìm thấy:
    return index
- Không tìm thấy:
    return -1
--------------------------------------------------

--------------------------------------------------
Tên hàm:
add_patient(records)

Input:
- records (list)

Output:
- None

Mô tả xử lý:
- Nhập thông tin bệnh nhân
- Chuẩn hóa dữ liệu
- Kiểm tra trùng mã
- Kiểm tra năm sinh hợp lệ
- join() tạo chuỗi hồ sơ
- append() vào danh sách
--------------------------------------------------

--------------------------------------------------
Tên hàm:
update_diagnosis(records)

Input:
- records (list)

Output:
- None

Mô tả xử lý:
- Nhập mã bệnh nhân
- Tìm index bệnh nhân
- Nếu tồn tại:
    + split("-")
    + cập nhật chẩn đoán
    + join() tạo chuỗi mới
    + gán đè dữ liệu
--------------------------------------------------

--------------------------------------------------
Tên hàm:
generate_age_report(records)

Input:
- records (list)

Output:
- None

Mô tả xử lý:
- Duyệt danh sách
- Tính tuổi:
    tuổi = năm hiện tại - năm sinh
- Phân loại:
    + <16
    + 16-60
    + >60
- Đếm số lượng từng nhóm
--------------------------------------------------

4. LUỒNG XỬ LÝ CHỨC NĂNG

CHỨC NĂNG 1:
- Hiển thị danh sách bệnh nhân

CHỨC NĂNG 2:
- Thêm bệnh nhân mới
- Chuẩn hóa dữ liệu
- Kiểm tra lỗi

CHỨC NĂNG 3:
- Cập nhật chẩn đoán
- String immutable:
    + split()
    + sửa dữ liệu
    + join()

CHỨC NĂNG 4:
- Tính tuổi
- Phân loại độ tuổi

CHỨC NĂNG 5:
- Thoát chương trình

5. EDGE CASES

- Năm sinh chứa chữ
- Năm sinh ngoài khoảng hợp lệ
- Trùng mã bệnh nhân
- Không tìm thấy mã bệnh nhân
- Danh sách rỗng

6. KỸ THUẬT ĐÃ SỬ DỤNG

- split()
- join()
- replace()
- title()
- capitalize()
- upper()
- startswith()
- append()
- while True
- match-case
- Docstring
- snake_case
'''


"""
Rikkei Hospital Management System
- Manage patient medical records
- Add and update patient diagnosis
- Generate age classification report
"""

from datetime import datetime

# GLOBAL VARIABLES
patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan"
]


# RECORD FUNCTIONS
def split_record(record: str):
    """
    Tách hồ sơ bệnh án.

    Args:
        record (str):
            Chuỗi hồ sơ bệnh án.

    Returns:
        list:
            Danh sách dữ liệu đã tách.
    """
    return record.split("-")


def display_records(records: list):
    """
    Hiển thị danh sách bệnh nhân.

    Args:
        records (list):
            Danh sách hồ sơ bệnh án.

    Returns:
        None
    """
    if not records:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        return

    print("\n--- DANH SÁCH BỆNH NHÂN ---------------------------")

    for index, record in enumerate(records, 1):

        patient_id, name, birth_year, diagnosis = (
            split_record(record)
        )

        print(
            f"{index}. "
            f"[{patient_id}] "
            f"{name:<20} | "
            f"Năm sinh: {birth_year} | "
            f"Chẩn đoán: {diagnosis}"
        )

    print("--------------------------------------------------")


# NORMALIZE FUNCTIONS
def normalize_patient_id(patient_id: str):
    """
    Chuẩn hóa mã bệnh nhân.

    Args:
        patient_id (str):
            Mã bệnh nhân.

    Returns:
        str:
            Mã đã chuẩn hóa.
    """
    return patient_id.strip().upper().replace(" ", "")


def normalize_name(name: str):
    """
    Chuẩn hóa tên bệnh nhân.

    Args:
        name (str):
            Tên bệnh nhân.

    Returns:
        str:
            Tên đã chuẩn hóa.
    """
    name = name.replace("-", " ")

    return name.title()


def normalize_diagnosis(diagnosis: str):
    """
    Chuẩn hóa chẩn đoán.

    Args:
        diagnosis (str):
            Chuỗi chẩn đoán.

    Returns:
        str:
            Chẩn đoán đã chuẩn hóa.
    """
    diagnosis = diagnosis.replace("-", " ")

    return diagnosis.capitalize()


# VALIDATION FUNCTIONS
def is_valid_birth_year(year: str):
    """
    Kiểm tra năm sinh hợp lệ.

    Args:
        year (str):
            Năm sinh.

    Returns:
        bool:
            True nếu hợp lệ,
            ngược lại False.
    """
    current_year = datetime.now().year

    if not year.isdigit():
        return False

    year = int(year)

    return 1900 <= year <= current_year


def find_patient_index(records: list, patient_id: str):
    """
    Tìm vị trí bệnh nhân trong danh sách.

    Args:
        records (list):
            Danh sách hồ sơ.

        patient_id (str):
            Mã bệnh nhân.

    Returns:
        int:
            Index nếu tìm thấy,
            ngược lại -1.
    """
    for index, record in enumerate(records):

        if record.startswith(patient_id):
            return index

    return -1


# ADD FUNCTIONS
def add_patient(records: list):
    """
    Thêm hồ sơ bệnh nhân mới.

    Args:
        records (list):
            Danh sách hồ sơ bệnh án.

    Returns:
        None
    """
    print("\n--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")

    patient_id = input(
        "Nhập mã bệnh nhân: "
    )

    patient_id = normalize_patient_id(patient_id)

    if find_patient_index(records, patient_id) != -1:
        print("\nMã bệnh nhân đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ")
    name = normalize_name(name)

    while True:

        birth_year = input("Nhập năm sinh: ")

        if is_valid_birth_year(birth_year):
            break

        print(
            "\nNăm sinh không hợp lệ, "
            "vui lòng nhập lại!"
        )

    diagnosis = input("Nhập chẩn đoán: ")
    diagnosis = normalize_diagnosis(diagnosis)

    patient_data = [
        patient_id,
        name,
        birth_year,
        diagnosis
    ]

    record = "-".join(patient_data)

    records.append(record)

    print("\nThêm hồ sơ bệnh nhân thành công!")

    print("Sau khi chuẩn hóa, dữ liệu được lưu là:")
    print(record)


# UPDATE FUNCTIONS
def update_diagnosis(records: list):
    """
    Cập nhật chẩn đoán bệnh nhân.

    Args:
        records (list):
            Danh sách hồ sơ bệnh án.

    Returns:
        None
    """
    print("\n--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")

    patient_id = input(
        "Nhập mã bệnh nhân cần cập nhật: "
    )

    patient_id = normalize_patient_id(patient_id)

    index = find_patient_index(records, patient_id)

    if index == -1:

        print(
            f"\nKhông tìm thấy bệnh nhân "
            f"mang mã {patient_id}!"
        )

        return

    parts = split_record(records[index])

    print(f"\nTìm thấy bệnh nhân: {parts[1]}")
    print(f"Chẩn đoán hiện tại: {parts[3]}")

    new_diagnosis = input(
        "Nhập chẩn đoán mới: "
    )

    new_diagnosis = normalize_diagnosis(
        new_diagnosis
    )

    parts[3] = new_diagnosis

    updated_record = "-".join(parts)

    records[index] = updated_record

    print("\nCập nhật chẩn đoán thành công!")

    print("Dữ liệu mới được lưu:")
    print(updated_record)


# REPORT FUNCTIONS
def generate_age_report(records: list):
    """
    Báo cáo phân loại theo độ tuổi.

    Args:
        records (list):
            Danh sách hồ sơ bệnh án.

    Returns:
        None
    """
    current_year = datetime.now().year

    children = 0
    adults = 0
    seniors = 0

    for record in records:

        parts = split_record(record)

        birth_year = int(parts[2])

        age = current_year - birth_year

        if age < 16:
            children += 1

        elif age <= 60:
            adults += 1

        else:
            seniors += 1

    print("\n--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")

    print(f"Trẻ em: {children} bệnh nhân")
    print(f"Trưởng thành: {adults} bệnh nhân")
    print(f"Người cao tuổi: {seniors} bệnh nhân")

    print("--------------------------------------")


# MENU
while True:

    print("\n===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====")
    print("1. Xem danh sách hồ sơ bệnh án")
    print("2. Thêm hồ sơ bệnh nhân mới")
    print("3. Cập nhật chẩn đoán theo Mã BN")
    print("4. Báo cáo phân loại theo độ tuổi")
    print("5. Thoát chương trình")
    print("===================================================")

    choice = input("Chọn chức năng (1-5): ")

    match choice:

        case "1":
            display_records(patient_records)

        case "2":
            add_patient(patient_records)

        case "3":
            update_diagnosis(patient_records)

        case "4":
            generate_age_report(patient_records)

        case "5":
            print(
                "Cảm ơn bác sĩ đã sử dụng hệ thống!"
            )

            break

        case _:
            print("Lựa chọn không hợp lệ!")


