array = [1, 2, 3]

def revert(lst):
    if len(lst) == 1:
        return lst
    item = lst[0]
    return revert(lst[1:]) + [item]

print(revert(array))