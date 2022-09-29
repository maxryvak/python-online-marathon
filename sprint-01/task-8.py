def studying_hours(a):
    count = 1
    len_list = [1]
    for i in range(1, len(a)+1):
        if i == len(a):
            len_list.append(count)
        elif a[i-1] <= a[i]:
            count += 1
        else:
            len_list.append(count)
            count = 1
    return max(len_list)
