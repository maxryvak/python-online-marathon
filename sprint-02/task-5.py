import re


def max_population(data):
    match = []
    diction = {}
    for i in data:
        city = re.findall(r'[a-zA-Z]{2}_\w+,\d+', i)
        match += city
    for i in range(len(match)):
        match[i] = re.split(',', match[i])
        match[i][1] = int(match[i][1])
        diction[match[i][0]] = match[i][1]

    return tuple([max(diction, key=diction.get), max(diction.values())])
