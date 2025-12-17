import datetime
from datetime import datetime
from datetime import timedelta
from datetime import date, datetime, timedelta


def string_to_date(date_string):   
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def date_to_string(converted_date):
    return converted_date.strftime("%Y.%m.%d")

def prepare_user_list(users): 
    for user in users:
        for key in user:
            if key == "birthday":
                user[key] = string_to_date(user[key])
    return users

def find_next_weekday(converted_date, weekday):
    days_ahead = weekday - converted_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return converted_date + timedelta(days=days_ahead)

def get_upcoming_birthdays(new_users, days=7):
    upcoming_birthdays = []
    today = "2023.03.20"
    today =string_to_date(today)
    for user in new_users:
        birthday_this_year = user["birthday"].replace(year = today.year)
        
        x = (birthday_this_year - today).days
        
        if 0 <=x and x<= days:
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": date_to_string(birthday_this_year)})
    return upcoming_birthdays

def adjust_for_weekend(birthday):
    '''for user in birthday_user:
        y = string_to_date(user["congratulation_date"])
        print(type(y))
        if y.weekday() >= 5:
            x = find_next_weekday(y,0)
            birthday_user.append({"name": user["name"], "send_mail": date_to_string(x)})'''
    if isinstance(birthday, str):
        birthday = string_to_date(birthday) 
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday,0)
    else:
        return birthday

users = [
    {"name": "Bill Gates", "birthday": "1955.03.25"},
    {"name": "Steve Jobs", "birthday": "1955.03.21"},
    {"name": "Jinny Lee", "birthday": "1956.03.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]


date_string = "2020.01.01"
converted_date = string_to_date(date_string)
print(converted_date)
next_monday = find_next_weekday(converted_date,0)
print(next_monday)
next_friday = find_next_weekday(converted_date,4)
print(next_friday)
print()
date_string = date_to_string(converted_date)
print(date_string)
new_users = prepare_user_list(users)
print(new_users)
print()
birthday_user = get_upcoming_birthdays(new_users)
print(birthday_user)
birthdayy = adjust_for_weekend("2024.04.27")
print(birthdayy)

