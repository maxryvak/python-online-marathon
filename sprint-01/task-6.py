def order(a):
    count_asc = 0
    count_desc = 0
    for i in range(1, len(a)):
        if a[i-1] <= a[i]:
            count_asc += 1
        elif a[i-1] >= a[i]:
            count_desc += 1
    
    if count_asc == len(a) - 1:
        return "ascending"
    elif count_desc == len(a) - 1:
        return "descending"
    else:
        return "not sorted"
