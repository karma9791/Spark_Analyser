from datetime import datetime


def long_to_datetime(long):
    return datetime.fromtimestamp(long/1000)