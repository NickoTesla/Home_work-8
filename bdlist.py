import datetime

users = [
    {'name': 'John', 'birthday': datetime.datetime(1990, 3, 20)},
    {'name': 'Jane', 'birthday': datetime.datetime(1985, 3, 23)},
    {'name': 'Bill', 'birthday': datetime.datetime(1978, 3, 28)},
    {'name': 'Emma', 'birthday': datetime.datetime(2000, 3, 25)},
    {'name': 'Kate', 'birthday': datetime.datetime(1995, 3, 21)},
    {'name': 'Alex', 'birthday': datetime.datetime(1992, 12, 31)},
]


def get_birthdays_per_week(users):
    today = datetime.date.today()
    weekdays = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday']

    birthday_week = [today + datetime.timedelta(days=i) for i in range(7)]

    birthdays = {weekday: [] for weekday in weekdays}

    for user in users:
        name = user['name']
        birthday = user['birthday'].replace(year=today.year).date()

        if birthday in birthday_week:

            if birthday.weekday() in (5, 6):
                birthdays['Monday'].append(name)
            else:
                birthdays[birthday.strftime("%A")].append(name)

    for weekday in weekdays:
        if birthdays[weekday]:
            names = ", ".join(birthdays[weekday])
            print(f"{weekday}: {names}")


if __name__ == "__main__":
    get_birthdays_per_week(users)
