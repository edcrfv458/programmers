def solution(lottos, win_nums):
    score = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }
    zero_count = lottos.count(0)
    match = len(set(lottos) & set(win_nums))
    return [score[match+zero_count], score[match]]