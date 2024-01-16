import re

def main():
    accepted_months = {"January":1, "February":2, "March":3,"April":4,"May":5,"June":6,
                       "July":7,"August":8,"September":9,"October":10,"November":11,"December":12}

    months = "|".join(accepted_months.keys())
    date = input("Enter MM DD, YYYY date: ").title()

    if matches := re.search(fr"^({months})\s(0[1-9]|[1-2][0-9]|3[0-1]{{2}}),\s([0-9]{{4}})$", date):
       month, day, year = matches.groups()
       print(f"{accepted_months[month]:02d}/{int(day):02d}/{year}")
    else:
        print("Invalid date")


main()