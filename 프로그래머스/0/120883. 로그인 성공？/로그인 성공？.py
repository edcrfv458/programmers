def solution(id_pw, db):
    I, P = id_pw
    for i, p in db:
        if I == i and P == p:
            return "login"
        elif I == i and P != p:
            return "wrong pw"
    return "fail"