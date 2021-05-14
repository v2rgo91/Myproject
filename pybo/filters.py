# import babel.

def format_datetime(value, fmt='%Y년 %m월 %H:%M'):
    return babel.dates.format_datetime(value,fmt)

def format_str(value, fmt='%s'):
    return babel.str.format_str(value,fmt)



