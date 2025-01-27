def solution(today, terms, privacies):
    y, m, d = map(int, today.split('.'))
    current_date = y * 12 * 28 + m * 28 + d
    answer = []
    term_dict = {}
    
    for term in terms:
        n, p = term.split()
        term_dict[n] = int(p) * 28

    for i, p in enumerate(privacies):
        day, n = p.split()
        y, m, d = map(int, day.split('.'))
        privacy_date = y * 12 * 28 + m * 28 + d 
        expiry_date = privacy_date + term_dict[n]

        if expiry_date <= current_date:
            answer.append(i + 1)

    return answer
