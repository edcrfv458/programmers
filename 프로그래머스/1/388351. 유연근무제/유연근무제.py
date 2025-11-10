def solution(schedules, timelogs, startday):
    result = 0
    
    for i, timelog in enumerate(timelogs):
        yes, count = 0, 0
        
        t = schedules[i] // 100
        m = schedules[i] % 100
        
        if m >= 50:
            cut_time = schedules[i] + 50
        else:
            cut_time = schedules[i] + 10
        
        for j, time in enumerate(timelog):
            
            day = (j + startday - 1) % 7
            if day in (5, 6):
                continue
        
            count += 1
            if time <= cut_time:
                yes += 1
                
        if count == yes:
            result += 1
            
    return result