import math
def kthTerm(n, k):
    res = [1]
    pow = math.ceil(math.log2(k))
    for i in range(1, pow+1):
        res.append(n**i)
        for j in range(2**i-1):
            res.append(n**i + res[j])
    return res[k-1]
