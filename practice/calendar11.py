import calendar
import datetime


def get_time():
    now = datetime.datetime.now()

    first_day = datetime.datetime(now.year, now.month, 1)
    last_day = datetime.datetime(now.year, now.month, calendar.monthrange(now.year, now.month)[1])
    return first_day.strftime("%Y, %m, %d"), last_day.strftime("%Y, %m, %d")


if __name__ == '__main__':
    a, b = get_time()
    print(type(a))
