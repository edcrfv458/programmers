def solution(babbling): # 'aya', 'ye', 'woo', 'ma'
    count = 0
    for b in babbling:
        b = b.replace('aya', ' ').replace('ye', ' ').replace('woo', ' ').replace('ma', ' ').replace(' ', '')
        if not b:
            count += 1
    return count