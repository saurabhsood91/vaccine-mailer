import datetime


def now():
    return datetime.datetime.now()


def get_formatted_date() -> str:
    return now().strftime('%d-%b')


def get_ddmmyy_date() -> str:
    return now().strftime('%d-%m-%Y')
