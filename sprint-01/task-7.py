def Cipher_Zeroes(N):
    count = 0
    N = [*N]
    for i in N:
        if i in ['0', '6', '9']:
            count += 1
        elif i == '8':
            count += 2
    if count > 0 and count % 2 == 1:
        count += 1
    elif count > 0 and count % 2 == 0:
        count -= 1
    else:
        count = 0
    return "{0:b}".format(int(count))
