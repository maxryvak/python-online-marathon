# type your code here
import string
from collections import Counter


def create_account(user_name, password, secret_words):
    low = any(elem in string.ascii_lowercase for elem in password)
    up = any(elem in string.ascii_uppercase for elem in password)
    char = any(elem in string.punctuation for elem in password)
    num = any(elem in string.digits for elem in password)
    t = low and up and char and num
    if not t or len(password) < 6:
        raise ValueError

    def check(pswrd, words):
        diff = Counter(words) - Counter(secret_words)
        if len(list(diff.elements())) > 1:
            return False
        if password != pswrd:
            return False
        if len(words) != len(secret_words):
            return False
        else:
            return True

    return check
    
tom = create_account("Tom", "Qwerty1_", ["1", "word"])  
check1 = tom("Qwerty1_",  ["1", "word"]) 
check2 = tom("Qwerty1_",  ["word"]) 
check3 = tom("Qwerty1_",  ["word", "2"]) 
check4 = tom("Qwerty1!",  ["word", "12"]) 
