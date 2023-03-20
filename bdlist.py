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
                'Thursday', 'Friday', 'Saturday', 'Sunday']
    birthday_week = [today + datetime.timedelta(days=i) for i in range(7)]

    birthdays = {weekday: [] for weekday in weekdays}

    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        if birthday in birthday_week:
            index = birthday_week.index(birthday)
            weekday = weekdays[index]
            birthdays[weekday].append(name)
        elif birthday.weekday() >= 5:  # Weekend birthday
            weekdays_cycle = cycle(weekdays)
            for i in range(7):
                next_weekday = next(weekdays_cycle)
                if next_weekday == 'Monday':
                    continue
                if i == 6:  # Couldn't find a weekday this week, so use next week's Monday
                    next_weekday = 'Monday'
                birthdays[next_weekday].append(name)

    for weekday in weekdays:
        if birthdays[weekday]:
            names = ", ".join(birthdays[weekday])
            print(f"{weekday}: {names}")
