
# AgeOperations.py <--------Module Name

import datetime
import calendar

from AgeExcept import InvalidDateError, FutureDateError


def add_months(dob, months):

    month_index = dob.month - 1 + months

    year = dob.year + month_index // 12
    month = month_index % 12 + 1

    day = min(
        dob.day,
        calendar.monthrange(year, month)[1]
    )

    return datetime.date(year, month, day)


def calculate_age():

    dob_input = input(
        "\tENTER YOUR DATE OF BIRTH (DD-MM-YYYY): "
    )

    try:
        dob = datetime.datetime.strptime(
            dob_input, "%d-%m-%Y"
        ).date()

    except ValueError:
        raise InvalidDateError

    today = datetime.date.today()

    if dob > today:
        raise FutureDateError

    total_months = (
        (today.year - dob.year) * 12
        + today.month - dob.month
    )

    while add_months(dob, total_months) > today:
        total_months -= 1

    years = total_months // 12
    months = total_months % 12

    last_date = add_months(dob, total_months)

    days = (today - last_date).days

    print("\n\tYOUR EXACT AGE")
    print("\tYEARS  :", years)
    print("\tMONTHS :", months)
    print("\tDAYS   :", days)
