from datetime import datetime
print(datetime(1993,9,21).isocalendar()[1]-datetime(1993,9,25).isocalendar()[1])
print(datetime(1993,9,21).isocalendar()[2]-datetime(1993,9,25).isocalendar()[2]+2)

def lc_calc(start='1993-09-21', date):
    start = datetime(start)
    date = datetime(date)
    timediff = datetime.timedelta(date - start)
    diffyear = datetime.isocalendar()[0]
    diffweeks = datetime.isocalendar()[1]
    diffdays = datetime.isocalendar()[2]
    print(diffyear)
    print(diffweeks)
    print(diffdays)
