def findPermutation(p, q):
    r=[]
    for i in range(0, len(p)):
        for j in range(0, len(q)):
            if q[i] == p[j]:
                r.append(p.index(p[j])+1)
    return r
