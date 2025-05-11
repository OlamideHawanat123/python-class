import datetime

from menstrual_cycle import MenstrualCycle


def main():
    while True:
        start = input("Enter the starting date in the format YYYY-MM-DD: ")
        try:
            start_date = datetime.datetime.strptime(start, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

    while True:
        end = input("Enter the ending date in the format YYYY-MM-DD: ")
        try:
            end_date = datetime.datetime.strptime(end, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

    while True:
        menstrual_cycles = int(input("How long does your menstrual cycle go? "))
        try:
            cycle_length = int(menstrual_cycles)
            if cycle_length < 21 or cycle_length > 35:
                print("Your cycle length seems to be out of the normal one)
            else:
                break
        except ValueError:
            print("Invalid menstrual cycle length. Please enter a valid number.")

    date_format = "%Y-%m-%d"
    start_date = datetime.datetime.strptime(start, date_format).date()
    end_date = datetime.datetime.strptime(end, date_format).date()

    my_cycle = MenstrualCycle(start_date,end_date,menstrual_cycles)
    fertile_start,fertile_end = my_cycle.get_fertile_window()

    print(f"The starting date: {my_cycle.start_date}")
    print(f"The ending date: {my_cycle.end_date}")
    print(f"The safe period is: {my_cycle.get_safe_period_end_date()}")
    print(f"The ovulation period is: {my_cycle.get_ovulation_date()}")
    print(f"The next period will be: {my_cycle.get_next_period_start_date()}")
    print(f"The fertile window is from {fertile_start} to {fertile_end}")


if __name__ == "__main__":
    main()