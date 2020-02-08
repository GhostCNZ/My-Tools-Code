import datetime
import calendar as c

def calmonths(startdate, enddate):
    # 计算两个日期相隔月差
    samemonthdate = None
    try:
        samemonthdate = datetime.date(enddate.year, enddate.month,startdate.day)
    except Exception as e:
        print(e)
        samemonthdate = datetime.date(enddate.year, enddate.month,c.monthrange(enddate.year,enddate.month)[1])
    holdmonths = 0
    decimalmonth = 0.0
    if samemonthdate > enddate:
        premanthdate = None
        try:
            premanthdate = datetime.date(enddate.year, enddate.month - 1,startdate.day)
        except Exception as e:
            print(e)
            premanthdate = datetime.date(enddate.year, enddate.month - 1,c.monthrange(enddate.year,enddate.month - 1)[1])
        currmonthdays = (samemonthdate - premanthdate).days
        holdmonths = (premanthdate.year - startdate.year ) * 12 + premanthdate.month - startdate.month
        decimalmonth = (enddate - premanthdate).days / currmonthdays
    elif samemonthdate < enddate:
        nextmonthdate = None
        try:
            nextmonthdate = datetime.date(enddate.year, enddate.month + 1,startdate.day)
        except Exception as e:
            nextmonthdate = datetime.date(enddate.year, enddate.month + 1,c.monthrange(enddate.year,enddate.month + 1)[1])
        currmonthdays = (nextmonthdate - samemonthdate).days
        holdmonths = (samemonthdate.year - startdate.year) * 12 + samemonthdate.month - startdate.month
        decimalmonth = (enddate - samemonthdate).days / currmonthdays
    else:
        holdmonths = (enddate.year - startdate.year) * 12 + enddate.month - startdate.month

    return holdmonths

