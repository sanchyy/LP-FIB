def count_unique(L):
    return (len(set(L)))


def remove_duplicates(L):
    return list(set(L))


def flatten(L):
    res = []
    for sub_l in L:
        res += sub_l
    return res


def flatten_rec(L):
    res = []
    for sub_l in L:
        if isinstance(sub_l, list):
            res += flatten_rec(sub_l)
        else: res.append(sub_l) 
    return res
