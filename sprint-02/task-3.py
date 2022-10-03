import math


def distance(p1, p2):
    return math.sqrt(
        math.pow(int(p2[0])-int(p1[0]), 2) + math.pow(int(p2[1])-int(p1[1]), 2))


def figure_perimetr(string):
    string = string.split('#')
    string.pop(0)
    points = []
    for i in string:
        i = i[2:]
        points.append(i.split(':'))

    points[2], points[3] = points[3], points[2]
    suma = 0
    for i in range(len(points)-1):
        suma += distance(points[i], points[i+1])
    suma += distance(points[0], points[-1])
    return suma
