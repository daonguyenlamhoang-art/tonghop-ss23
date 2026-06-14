from hrm_package.ui_display import display_records
from hrm_package.attendance_logic import clock_in
from hrm_package.attendance_logic import clock_out
from hrm_package.time_calc import evaluate_flex_time as evaluate_shifts

attendance_book = [
    {
        "id": "NV01",
        "name": "Nguyễn Văn A",
        "times": ("08:30", "17:30")
    },

    {
        "id": "NV02",
        "name": "Trần Thị B",
        "times": ("09:30", None)
    },

    {
        "id": "NV03",
        "name": "Lê Văn C",
        "times": ("10:15", "19:15")
    }
]

while True:
    print("=== HỆ THỐNG CHẤM CÔNG RIKKEI ===")
    print("1. Xem bảng chấm công ngày")
    print("2. Chấm công vào")
    print("3. Chấm công ra")
    print("4. Đánh giá vi phạm")
    print("5. Thoát")
    print("=================================")

    choice = input(
        "Chọn chức năng (1-5): "
    )

    if choice == "1":
        display_records(
            attendance_book
        )

    elif choice == "2":
        clock_in(
            attendance_book
        )

    elif choice == "3":
        clock_out(
            attendance_book
        )

    elif choice == "4":
        evaluate_shifts(
            attendance_book
        )

    elif choice == "5":
        print("Tạm biệt!")
        break

    else:
        print("Vui lòng chọn từ 1 đến 5.")
