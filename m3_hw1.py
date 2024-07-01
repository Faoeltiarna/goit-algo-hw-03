import datetime

def get_days_from_today(date):
    date_value = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    current_date = datetime.datetime.today().date()
    difference = date_obj.toordinal() - current_date.toordinal()
    return difference


print(get_days_from_today("2005-09-01"))
