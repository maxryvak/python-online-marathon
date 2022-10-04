import re


def pretty_message(string):
    string = re.sub(r"(\w{1})(\1*)\b", r'\1', string)
    string = re.sub(r"(\w{2})(\1*)\b", r'\1', string)
    string = re.sub(r"(\w{3})(\1*)\b", r'\1', string)
    return string
