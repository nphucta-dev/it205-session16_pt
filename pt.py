"""
PHÂN TÍCH & THIẾT KẾ GIẢI PHÁP

1. find_patient_index(patients, er_id)
- Input: list[str], str
- Output: int
- Duyệt danh sách, dùng startswith để tìm mã ER

2. extract_vital_value(vital_string)
- Input: str ("HR:115")
- Output: float
- Split ":" lấy phần số và ép kiểu float

3. display_dashboard(patients)
- Input: list[str]
- Output: None
- Split từng chuỗi và in bảng

4. admit_patient(patients)
- Input: list[str]
- Output: None
- Nhập dữ liệu, validate, chuẩn hóa, join và append

5. update_vitals(patients)
- Input: list[str]
- Output: None
- Split → sửa HR hoặc TEMP → join → gán lại

6. trigger_red_alert(patients)
- Input: list[str]
- Output: None
- Lọc HR > 100 hoặc TEMP >= 39

7. discharge_patient(patients)
- Input: list[str]
- Output: None
- Xóa bằng pop/remove
"""

patients = [
    "ER01|Nguyen Van Quan|HR:115|TEMP:39.5",
    "ER02|Tran Thi Binh|HR:80|TEMP:37.0",
    "ER03|Le Van Cuong|HR:130|TEMP:38.2"
]


def find_patient_index(patients, er_id):
    er_id = er_id.strip().upper()
    for i, p in enumerate(patients):
        if p.startswith(er_id + "|"):
            return i
    return -1


def extract_vital_value(vital_string):
    return float(vital_string.split(":")[1])


def display_dashboard(patients):
    if len(patients) == 0:
        print("Khoa cấp cứu hiện đang trống.")
        return

    print("--- BẢNG THEO DÕI CA CẤP CỨU ---")

    for i, p in enumerate(patients, 1):
        er_id, name, hr, temp = p.split("|")

        hr_val = hr.split(":")[1]
        temp_val = temp.split(":")[1]

        print(f"{i}. [{er_id}] {name} | Nhịp tim: {hr_val} bpm | Nhiệt độ: {temp_val} °C")

    print("---------------------------------")


def admit_patient(patients):
    print("--- TIẾP NHẬN CA CẤP CỨU MỚI ---")

    er_id = input("Nhập mã ER: ").strip().upper()
    if len(er_id) == 0:
        print("Mã ER không được để trống!")
        return

    if find_patient_index(patients, er_id) != -1:
        print("Mã ca cấp cứu đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ").strip().title()
    if len(name) == 0:
        print("Tên bệnh nhân không được để trống!")
        return

    while True:
        hr = input("Nhập nhịp tim HR: ").strip()
        if hr.isdigit() and int(hr) > 0:
            hr = int(hr)
            break
        print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!")

    while True:
        temp = input("Nhập nhiệt độ TEMP: ").strip()
        if temp.replace(".", "", 1).isdigit() and float(temp) >= 36.5:
            temp = float(temp)
            break
        print("Sinh hiệu không hợp lệ, vui lòng nhập >= 36.5!")

    record = "|".join([
        er_id,
        name,
        f"HR:{hr}",
        f"TEMP:{temp}"
    ])

    patients.append(record)

    print("\nTiếp nhận ca cấp cứu mới thành công!")
    print(record)


def update_vitals(patients):
    print("--- CẬP NHẬT LẠI SINH HIỆU ---")

    er_id = input("Nhập mã ER cần cập nhật: ").strip().upper()
    idx = find_patient_index(patients, er_id)

    if idx == -1:
        print("Không tìm thấy bệnh nhân. Vui lòng kiểm tra lại mã ER!")
        return

    parts = patients[idx].split("|")

    print(f"Tìm thấy bệnh nhân: {parts[1]}")
    print(f"Sinh hiệu hiện tại: {parts[2]} | {parts[3]}")

    print("1. Nhịp tim HR")
    print("2. Nhiệt độ TEMP")

    choice = input("Chọn loại sinh hiệu: ").strip()

    if choice == "1":
        while True:
            new_hr = input("Nhập nhịp tim mới: ").strip()
            if new_hr.isdigit() and int(new_hr) > 0:
                parts[2] = f"HR:{int(new_hr)}"
                break
            print("Sinh hiệu không hợp lệ!")

        print("Cập nhật nhịp tim thành công!")

    elif choice == "2":
        while True:
            new_temp = input("Nhập nhiệt độ mới: ").strip()
            if new_temp.replace(".", "", 1).isdigit() and float(new_temp) >= 36.5:
                parts[3] = f"TEMP:{float(new_temp)}"
                break
            print("Sinh hiệu không hợp lệ!")

        print("Cập nhật nhiệt độ thành công!")

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2!")
        return

    patients[idx] = "|".join(parts)


def trigger_red_alert(patients):
    print("!!! BÁO ĐỘNG ĐỎ !!!")

    danger_list = []

    for p in patients:
        er_id, name, hr, temp = p.split("|")

        hr_val = extract_vital_value(hr)
        temp_val = extract_vital_value(temp)

        if hr_val > 100 or temp_val >= 39:
            danger_list.append(p)

    if len(danger_list) == 0:
        print("Không có bệnh nhân nguy kịch.")
        return

    for i, p in enumerate(danger_list, 1):
        er_id, name, hr, temp = p.split("|")
        print(f"{i}. [{er_id}] {name} | {hr} | {temp} | CẦN XỬ LÝ KHẨN CẤP")

    print(f"Tổng số ca nguy kịch: {len(danger_list)}")


def discharge_patient(patients):
    er_id = input("Nhập mã ER cần xóa: ").strip().upper()

    idx = find_patient_index(patients, er_id)

    if idx == -1:
        print("Không tìm thấy bệnh nhân. Vui lòng kiểm tra lại mã ER!")
        return

    name = patients[idx].split("|")[1]
    patients.pop(idx)

    print(f"Đã chuyển khoa thành công cho bệnh nhân {name}!")


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ CẤP CỨU RIKKEI ER =====")
    print("1. Bảng theo dõi bệnh nhân")
    print("2. Tiếp nhận ca cấp cứu mới")
    print("3. Cập nhật lại sinh hiệu")
    print("4. BÁO ĐỘNG ĐỎ")
    print("5. Xuất viện / Chuyển khoa")
    print("6. Thoát")
    print("================================================")

    choice = input("Chọn chức năng (1-6): ").strip()

    match choice:
        case "1":
            display_dashboard(patients)
        case "2":
            admit_patient(patients)
        case "3":
            update_vitals(patients)
        case "4":
            trigger_red_alert(patients)
        case "5":
            discharge_patient(patients)
        case "6":
            print("Kết thúc ca trực.")
            break
        case _:
            print("Lựa chọn không hợp lệ!")