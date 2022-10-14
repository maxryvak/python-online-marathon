import cmath


def solve_quadric_equation(a, b, c):
    # your code
    try:
        a, b, c = float(a), float(b), float(c)
        x2 = (-b + cmath.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x1 = (-b - cmath.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        return f"The solution are x1={x1} and x2={x2}"
    except ZeroDivisionError:
        return "Zero Division Error"
    except ValueError:
        return "Could not convert string to float"
