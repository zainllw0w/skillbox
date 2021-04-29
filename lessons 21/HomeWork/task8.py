nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]

def f(*args, db = list()):
    for i in args:
        if isinstance(i, list):
            for i_2 in i:
                f(i_2)
        else:
            db.append(i)
            return i
    return db





print(f(nice_list))
