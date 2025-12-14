import datetime
from datetime import datetime
from datetime import timedelta

def string_to_date(date_string):   
    date_object = datetime.strptime(date_string, "%Y.%m.%d").date()
    return date_object

def date_to_string(converted_date):
    return converted_date.strftime("%Y.%m.%d")

def prepare_user_list(users):
    for user in users:
        for key in user:
            if key == "birthday":
                user[key] = string_to_date(user[key])
    return users

def find_next_weekday(converted_date, weekday):
    x = weekday - (datetime.weekday(converted_date))
    if not (x <= 0):
        converted_date = converted_date + timedelta(days=x)
    else:
        converted_date = converted_date + timedelta(days=7+x)
    return converted_date

def get_upcoming_birthdays(new_users, days=7):
    upcoming_birthdays = []
    today = datetime.today()

    for user in new_users:
        user["birthday"].replace(year = today.year)
        birthday_this_year = string_to_date(user["birthday"])
        birthday_this_year = user["birthday"].strftime("%d")
        x = (birthday_this_year - today).days
        if 0 <=x and x<= days:
            upcoming_birthdays.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
        
    return upcoming_birthdays


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
birthday_user = get_upcoming_birthdays(new_users)
print(birthday_user)



