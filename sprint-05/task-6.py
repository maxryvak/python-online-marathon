class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg


def check_positive(number):
    try:
        if float(number) > 0:
            return f"You input positive number: {float(number)}"
        elif float(number) < 0:
            raise MyError(f'You input negative number: {float(number)}. Try again.')
    except ValueError:
        return "Error type: ValueError!"
    except MyError as er:
        return er.msg
