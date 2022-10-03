def morse_number(num):
    res = ''
    for i in num:
        i = int(i)
        if int(i) < 6:
            res+=(i * '.' + (5-i) * '-' + ' ')
        else:
            res+=((i-5) * '-' + (5 - (i-5)) * '.'  + ' ')
    return res
