import datetime

def solution(a, b):
    weekdays = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    dt = weekdays[datetime.date(2016,a,b).weekday()]
    return dt