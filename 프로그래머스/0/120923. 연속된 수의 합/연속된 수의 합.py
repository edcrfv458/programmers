def solution(num, total):
    answer = [0 + i for i in range(num)]
    if num % 2 == 1:
        mid = total // num
        answer[num // 2] = mid
        s = 1
        t = 1
        for a in range(num // 2 - 1, -1, -1):
            answer[a] = mid - s
            s += 1
        for a in range(num // 2 + 1, num):
            answer[a] = mid + t
            t += 1
    else:
        mid_left = total // num
        mid_right = total // num + 1
        answer[num // 2 - 1] = mid_left
        answer[num // 2] = mid_right
        s, t = 1, 1
        for a in range(num // 2 - 2, -1, -1):
            answer[a] = mid_left - s
            s += 1
        for a in range(num // 2 + 1, num):
            answer[a] = mid_right + t
            t += 1
    return answer