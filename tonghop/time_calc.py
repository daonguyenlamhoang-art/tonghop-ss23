import datetime

def evaluate_flex_time(attendance_book):
    print("-- ĐÁNH GIÁ VI PHẠM ---")
    for employee in attendance_book:
        clock_in = employee["times"][0]
        clock_out = employee["times"][1]

        if clock_out == None:
            continue

        in_time = datetime.datetime.strptime(clock_in,"%H:%M")

        out_time = datetime.datetime.strptime(clock_out,"%H:%M")

        limit = datetime.datetime.strptime("10:00","%H:%M")

        if in_time > limit:
            print(
                employee["id"],
                "- Vi phạm: Đến muộn quá 90 phút."
            )

        else:
            work_time = out_time - in_time
            if work_time.seconds < 32400:
                print(employee["id"], "- Vi phạm: Về sớm, chưa hoàn thành đủ 9 tiếng bù giờ.")
            else:
                print(employee["id"],"- Hợp lệ: Hoàn thành ca làm việc.")
