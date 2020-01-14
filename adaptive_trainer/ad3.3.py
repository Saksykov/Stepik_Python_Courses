def modify_list(l):
    s = l.copy()
    l.clear()
    for i in s:
        if i % 2 == 0:
            l.append(i//2)