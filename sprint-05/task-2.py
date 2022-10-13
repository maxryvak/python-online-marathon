import re

regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

def valid_email(email):
    return "Email is valid" if re.match(regex, email) else "Email is not valid"
