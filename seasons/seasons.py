import re
import sys
import inflect
from datetime import date, datetime


def main():
    dob = input("Date of Birth: ")
    if check_valid(dob):
        if match := re.sub(r'\band\b', '',return_diff(dob)):
            minutes = ("".join(list(match))).replace('  ', ' ')

        formatted_minutes = minutes[0].upper() + minutes[1:]
        print(formatted_minutes)
    else:
        sys.exit("Invalid Format")


def check_valid(s):
      if re.search(r'^([0-9]{4})-(0[0-9]|1[-2])-([0-2][0-9]|3[0-1])$', s):
        return True
      return False


def return_diff(i):
     p = inflect.engine()
     i_value = datetime.timestamp( datetime.strptime(i, '%Y-%m-%d'))
     today_value = str(date.today())
     today_value = datetime.timestamp(datetime.strptime(today_value, '%Y-%m-%d'))
     diff = int((today_value - i_value)/60)
     return f"{p.number_to_words(diff)} minutes"

if __name__ == "__main__":
    main()