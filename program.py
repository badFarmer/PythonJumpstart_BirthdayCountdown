import datetime


def print_header():
    print('---------------------------------------------')
    print('           birthday countdown.               ')
    print('---------------------------------------------')
    print()


def get_birthday_from_user():
    year = int(input('What year were you born? [YYYY] '))
    month = int(input('Month? [MM] '))
    day = int(input('Day? [DD] '))
    print('It looks like you were born on {}/{}/{}.'.format(month, day, year))
    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year,original_date.month,original_date.day)
    dt = this_year - target_date
    return dt.days


def print_birthday_information(days):
    if days != 0:
        if days >1:
            ub = 'unbirtdays'
        elif days == 1:
            ub = 'unbirthday'
        print('Your birthday is {} {} away.'.format(days,ub))
    elif days <0:
        print ('You have already had your birthday, you sneaky fucking chump.')
    else:
        print('Happy birthday!')

def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = int(compute_days_between_dates(bday, today))
    print_birthday_information(number_of_days)


main()
