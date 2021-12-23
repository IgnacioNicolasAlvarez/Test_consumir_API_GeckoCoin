from datetime import datetime, timedelta


def get_datetime_last_n_days(format='%d-%m-%Y', n=-1) -> str:
    return (datetime.now() + timedelta(days=n)).strftime(format)


def validate_format_input_date(date: str, format: str = '%d-%m-%Y') -> bool:
    try:
        datetime.strptime(date, format)
    except ValueError:
        return False
    return True

def get_dates_in_interval(start_date, end_date, format='%d-%m-%Y') -> list:
    start_date = datetime.strptime(start_date, format)
    end_date = datetime.strptime(end_date, format)
    dates = []
    while start_date <= end_date:
        dates.append(start_date.strftime(format))
        start_date += timedelta(days=1)
    return dates


