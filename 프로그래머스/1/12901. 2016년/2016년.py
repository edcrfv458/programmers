import datetime

def solution(a, b):
    wek = ["MON", 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day = datetime.date(2016, a, b).weekday()
    return wek[day]