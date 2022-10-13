def check_number_group(number):
    try:
        if int(number) <= 10:
            return "We obtain error:Number of your group can't be less than 10"
        else:
            return f"Number of your group {number} is valid"

    except ValueError:
        return "You entered incorrect data. Please try again."
