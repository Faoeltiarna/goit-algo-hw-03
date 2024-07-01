from datetime import datetime

def get_days_from_today(date):
    date_value = datetime.strptime(date, "%Y-%m-%d").date()
    current_date = datetime.today().date()
    difference = date_value.toordinal() - current_date.toordinal()
    return difference


print(get_days_from_today("2005-09-01"))
