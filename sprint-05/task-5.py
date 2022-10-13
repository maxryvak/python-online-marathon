def day_of_week(day):
    try:
        if type(day) != int:
            raise TypeError
        match day:
            case 1:
                return "Monday"
            case 2:
                return "Tuesday"
            case 3:
                return "Wednesday"
            case 4:
                return "Thursday"
            case 5:
                return "Friday"
            case 6:
                return "Saturday"
            case 7:
                return "Sunday"
    except TypeError:
        return "You did not enter a number! Please try again."


def day_of_week_2(day):
    try:
        days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        return days[int(day)-1] if int(day) in range(1, 8) else "There is no such day of the week! Please try again."
    except ValueError:
        return "You did not enter a number! Please try again."
