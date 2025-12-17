from datetime import datetime, date, timedelta
import datetime
from datetime import datetime
from datetime import timedelta
from datetime import date, datetime, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list


def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = string_to_date("2024.12.30")

    for user in users:
        
        birthday_this_year = string_to_date(user["birthday"]).replace(year=today.year)
        if birthday_this_year < today:
            birthday_next = string_to_date(user["birthday"]).replace(year=today.year + 1)
            days_diff = (birthday_next - today).days
            if days_diff <= days:
                birthday_next = adjust_for_weekend(birthday_next)
                upcoming_birthdays.append({"name": user["name"], "congratulation_date": date_to_string(birthday_next)})
                

        if 0 <= (birthday_this_year - today).days <= days:
            birthday_this_year = adjust_for_weekend(birthday_this_year)
            congratulation_date_str = date_to_string(birthday_this_year)
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
    return upcoming_birthdays

users = [
    {"name": "Bill Gates", "birthday": "1955.04.25"},
    {"name": "Steve Jobs", "birthday": "1955.03.21"},
    {"name": "Jinny Lee", "birthday": "1956.03.22"},
    {"name": "Sarah Lee", "birthday": "1957.03.23"},
    {"name": "Jonny Lee", "birthday": "1958.03.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.03"}
]


x = get_upcoming_birthdays(users, 7)
print(x)