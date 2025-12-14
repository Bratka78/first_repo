import datetime
from datetime import datetime

def string_to_date(date_string):   
    date_object = datetime.strptime(date_string, "%Y.%m.%d").date()
    return date_object

def date_to_string(converted_date):
    date_string = converted_date.strftime("%Y.%m.%d")
    return date_string

def prepare_user_list(users):
    for ch in users:
        for key in ch:
            if key == "birthday":
                ch[key] = string_to_date(ch[key])
                print(ch[key])
            '''else: 
                print(f"{key}, {value}")'''
    return users


users = [
    {"name": "Bill Gates", "birthday": "1955.03.25"},
    {"name": "Steve Jobs", "birthday": "1955.03.21"},
    {"name": "Jinny Lee", "birthday": "1956.03.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]


date_string = "2024.01.01"
converted_date = string_to_date(date_string)
print(converted_date)
date_string = date_to_string(converted_date)
print(date_string)
dat = [{}]
dat = prepare_user_list(users)
print(dat)



