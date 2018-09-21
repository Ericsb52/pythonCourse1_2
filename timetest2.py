def current_time():
    seconds = calendar.timegm(time.gmtime())
    current_seconds = seconds % 60
    minutes = seconds // 60
    current_minutes= minutes % 60
    hours = minutes // 60
    current_hour = hours % 24
    

    time = str( current_seconds)+":"+str( current_minutes)+":"+str( current_hour)
    return time

time = current_time()
print (time)
