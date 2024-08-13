def solution(babbling): # 'aya', 'ye', 'woo', 'ma'
    count = 0
    for i in babbling:
        i = i.replace('aya',' ')
        i = i.replace('ye',' ')
        i = i.replace('woo',' ')
        i = i.replace('ma',' ')
        i = i.replace(' ','')
        if len(i) == 0:
            count += 1
    return count