def check_number_group_1(number):
    try:
        if int(number) <= 10:
            return "We obtain error:Number of your group can't be less than 10"
        else:
            return f"Number of your group {number} is valid"

    except ValueError:
        return "You entered incorrect data. Please try again."
    

    
    
class ToSmallNumberGroupError(Exception): 
     def __init__(self, msg):
        self.msg = msg
    
# enter your code 
def check_number_group_2(number):
    try:
        if int(number) <= 10:
            raise (ToSmallNumberGroupError("We obtain error:Number of your group can't be less than 10"))
        else:
            return f"Number of your group {number} is valid"
    except ToSmallNumberGroupError as error:
        return error.msg
    except ValueError:
        return "You entered incorrect data. Please try again."
