def solution(id_pw, db):
    ids = []
    for data in db:
        ids.append(data[0])
    if id_pw in db:
        return 'login'
    elif id_pw[0] in ids:
        return 'wrong pw'
    else:
        return 'fail'