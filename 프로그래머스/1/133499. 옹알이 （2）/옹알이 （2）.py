def solution(babbling):
    # 'aya', 'ye', 'woo', 'ma'
    count = 0
    for b in babbling:
        if 'aya'*2 not in b:
            b = b.replace('aya', ' ')
        if 'ye'*2 not in b:
            b = b.replace('ye', ' ')
        if 'woo'*2 not in b:
            b = b.replace('woo', ' ')
        if 'ma'*2 not in b:
            b = b.replace('ma', ' ')
        if not b.replace(' ', ''):
            count += 1
    return count
        