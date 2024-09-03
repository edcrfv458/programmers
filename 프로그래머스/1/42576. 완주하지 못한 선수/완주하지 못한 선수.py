def solution(participant, completion):
    dict1 = {}
    dict2 = {}
    for i in sorted(participant):
        try:
            dict1[i] += 1
        except:
            dict1[i] = 1
    
    for i in sorted(completion):
        try:
            dict2[i] += 1
        except:
            dict2[i] = 1
    
    for p in dict1.keys():
        if p not in dict2:
            return p
        
    for p in dict1.keys():
        if dict1[p] != dict2[p]:
            return p