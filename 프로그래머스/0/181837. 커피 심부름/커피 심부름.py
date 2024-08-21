def solution(order):
    sum = 0
    for c in order:
        if c == "iceamericano" or c == "americanoice" or c == "americano" or c == "hotamericano" or c == "anything" or c == "americanohot":
            sum += 4500
        else:
            sum += 5000
    return sum