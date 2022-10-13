def check_odd_even (number):
    try:
        return "Entered number is even" if number % 2 == 0 else "Entered number is odd"
    except TypeError:
        return "You entered not a number."
