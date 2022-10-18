import json

def find(file, key):
    with open(file) as file:
        data = json.load(file)
    unique = []
    finding(data, key, unique, False)
    return unique


def finding(structure, key, unique, end):
    if type(structure) == str and end and structure not in unique:
        unique.append(structure)
    if type(structure) == list:
        for i in structure:
            finding(i, key, unique, end)
    if type(structure) == dict:
        for struc_key, value in structure.items():
            if struc_key == key:
                finding(value, key, unique, True)
            else:
                finding(value, key, unique, end)
