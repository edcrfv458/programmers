def solution(quiz):
    answer = []
    for q in quiz:
        a, p, b, q, c = q.split()
        if eval(f"{a} {p} {b}") == eval(c):
            answer.append("O")
        else:
            answer.append("X")
    return answer