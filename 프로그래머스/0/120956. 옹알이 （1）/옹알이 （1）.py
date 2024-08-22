def solution(babbling): # 'aya', 'ye', 'woo', 'ma'
    count = 0
    for b in babbling:
        data = b.replace('aya', ' ')
        data = data.replace('ye', ' ')
        data = data.replace('woo', ' ')
        data = data.replace('ma', ' ')
        data = data.replace(' ','')
        if len(data) == 0:
            count += 1
    return count