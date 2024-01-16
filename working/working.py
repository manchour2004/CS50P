import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    format = '([0-9]|1[0-2])(?:\:)?([0-5]?[0-9])?\s(AM|PM)'
    if re.search(fr'^{format}\sto\s{format}$', s.upper(), re.IGNORECASE):
        start, end = s.split("to")

        if "PM" in start and ":" in start:
            start_hour, start_minute = start.replace("PM", "").split(":")
            start_minute = int(start_minute)
            if int(start_hour) != 12:
                start_hour = int(start_hour) + 12
            else:
                start_hour = int(start_hour)
        elif "PM" in start and ":" not in start:
            start_hour = start.replace("PM", "")
            start_minute = 0
            if int(start_hour) != 12:
                start_hour = int(start_hour) + 12
            else:
                start_hour = int(start_hour)
        else:
            if ":" not in start:
                start_hour = start.replace("AM", "")
                start_minute = 0
                if int(start_hour) != 12:
                    start_hour = int(start_hour)
                else:
                    start_hour = 0
            else:
                start_hour, start_minute = start.replace("AM", "").split(":")
                start_minute = int(start_minute)
                if int(start_hour) != 12:
                    start_hour = int(start_hour)
                else:
                    start_hour = 0

        if "PM" in end and ":" in end:
            end_hour, end_minute = end.replace("PM", "").split(":")
            end_minute = int(end_minute)
            if int(end_hour) != 12:
                end_hour = int(end_hour) + 12
            else:
                end_hour = int(end_hour)
        elif "PM" in end and ":" not in end:
            end_hour = end.replace("PM", "")
            end_minute = 0
            if int(end_hour) != 12:
                end_hour = int(end_hour) + 12
            else:
                end_hour = int(end_hour)
        else:
            if ":" not in end:
                end_hour = end.replace("AM", "")
                end_minute = 0
                if int(end_hour) != 12:
                    end_hour = int(end_hour)
                else:
                    end_hour = 0

            else:
                end_hour, end_minute = end.replace("AM", "").split(":")
                end_minute = int(end_minute)
                if int(end_hour) != 12:
                    end_hour = int(end_hour)
                else:
                    end_hour = 0
    else:
        raise ValueError

    return f"{start_hour:02d}:{start_minute:02d} to {end_hour:02d}:{end_minute:02d}"


if __name__ == "__main__":
    main()