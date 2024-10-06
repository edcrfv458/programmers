def solution(players, callings):
    score = {}
    for i, p in enumerate(players):
        score[p] = i
    for c in callings:
        idx = score[c]  # 현재 불린 선수의 등수
                        # idx-1 = 앞서 가던 선수의 등수
                        # c는 현재 불린 선수의 이름
        front_player = players[idx-1]     # 앞서 가던 선수의 이름
        players[idx], players[idx-1] = front_player, c
        score[c] -= 1
        score[front_player] += 1
    return players
        