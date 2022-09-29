def filterBible(scripture, book, chapter):
    res=[]
    for i in scripture:
        if i[0:2] == book and i[2:5] == chapter:
            res.append(i)
    return res
