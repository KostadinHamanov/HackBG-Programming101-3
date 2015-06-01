from datetime import date


def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def friday_years(start, end):
    fridayYears = 0

    for year in range(start, end + 1):
        if is_leap(year):
            if (date(year, 1, 1).isoweekday() == 5) or \
                    (date(year, 1, 2).isoweekday() == 5):

                fridayYears += 1
        else:
            if (date(year, 1, 1).isoweekday() == 5):
                fridayYears += 1
    return fridayYears


def main():
    print (friday_years(1000, 2000))
    print (friday_years(1753, 2000))
    print (friday_years(1990, 2015))

if __name__ == "__main__":
    main()
