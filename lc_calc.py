from datetime import datetime
from datetime import timedelta
import argparse

def lc_calc(date, start='1993-09-21'):
    print(date)
    date = datetime.strptime(date, "%Y-%m-%d")
    start = datetime.strptime(start, "%Y-%m-%d")
    date_adjusted = date + timedelta(days=2)

    dateyear = date.isocalendar()[0]
    dateweek = date.isocalendar()[1]
    dateday = date.isocalendar()[2]

    date_adjustedyear = date_adjusted.isocalendar()[0]
    date_adjustedweek = date_adjusted.isocalendar()[1]
    date_adjustedday = date_adjusted.isocalendar()[2]

    startyear = start.isocalendar()[0]
    startweek = start.isocalendar()[1]
    startday = start.isocalendar()[2]

    lc_col = date_adjustedyear - startyear
    lc_row = date_adjustedweek - startweek
    if lc_row < 0:
        lc_row = 52 + lc_row
        lc_col += -1
    print(f'Year: {lc_col}')
    print(f'Week: {lc_row}')
    print(f'LC Coords: {lc_col}, {lc_row}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    today_str = datetime.today().strftime("%Y-%m-%d")
    date = today_str
    parser.add_argument('date', help="Date to place on Life Calendar in format YYYY-MM-DD eg 2017-06-17.")
    args = parser.parse_args()
    date = args.date
    lc_calc(date)
