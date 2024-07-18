def solution(babbling): # 'aya', 'ye', 'woo', 'ma'
    answer = 0
    for idx, b in enumerate(babbling):
        if 'aya' in b:
            b = b.replace('aya', ' ')
        if 'ye' in b:
            b = b.replace('ye', ' ')
        if 'woo' in b:
            b = b.replace('woo', ' ')
        if 'ma' in b:
            b = b.replace('ma', ' ')
        b = b.replace(' ', '')
        if len(b) == 0:
            answer += 1
        babbling[idx] = b
    return answer