from datetime import datetime

date_value = input("Enter your date in format 'YYYY-mm-dd': ")
def get_days_from_today(date):
    try:
        date_value = datetime.strptime(date, "%Y-%m-%d").date()
        current_date = datetime.today().date()
        difference = date_value.toordinal() - current_date.toordinal()
        return difference
    except ValueError:
        return "Error date fotmat!"

print(get_days_from_today(date_value))