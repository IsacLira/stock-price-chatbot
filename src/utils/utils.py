import time

def get_current_time():
    current_time_date = time.strftime("%d %b, %H:%M:%S", time.localtime())
    return current_time_date
