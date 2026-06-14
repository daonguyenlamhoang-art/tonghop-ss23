from tabulate import tabulate
def display_records(attendance_book):
    table = []

    for employee in attendance_book:
        clock_out = employee["times"][1]
        if clock_out == None:
            clock_out = "[Đang làm việc]"

        row = [
            employee["id"],
            employee["name"],
            employee["times"][0],
            clock_out
        ]
        table.append(row)

    print("--- BẢNG CHẤM CÔNG ---")

    print(
        tabulate(
            table,
            headers=[
                "Mã NV",
                "Tên Nhân Viên",
                "Giờ Vào",
                "Giờ Ra"
            ],
            tablefmt="grid"
        )
    )
