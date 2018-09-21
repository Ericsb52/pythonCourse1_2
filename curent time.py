import calendar 
import time


def current_time():
    seconds = calendar.timegm(time.gmtime())
    current_seconds = seconds % 60
    minutes = seconds // 60
    current_minutes= minutes % 60
    hours = minutes // 60
    current_hour = hours % 24

    return current_seconds, current_minutes, current_hour

s,m,h = current_time()
print(h,m,s)
