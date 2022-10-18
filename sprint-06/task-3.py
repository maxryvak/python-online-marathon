import json
import jsonschema
from jsonschema import validate
import csv

user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "department_id": {"type": "number"},
    },
    "required" : ["id", "name", "department_id"]
}

depart_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
    },
    "required" : ["id", "name"]
}


class DepartmentName(Exception):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"Department with id {self.id} doesn't exists"


class InvalidInstanceError(Exception):
    def __init__(self, typee):
        self.type = typee

    def __str__(self):
        return f"Error in {self.type} schema"


def validate_json(data, schema, typee):
    try:
        validate(instance=data, schema=schema)
    except jsonschema.exceptions.ValidationError:
        raise InvalidInstanceError(typee)


def user_with_department(csv_file, user_json, department_json):
    header = ["name", "department"]
    with open(user_json) as user:
        user_data = json.load(user)
    with open(department_json) as depart:
        depart_data = json.load(depart)

    new_dict = []
    dep_id_list = []

    for userr in user_data:
        validate_json(userr, user_schema, "user")
        for dep in depart_data:
            validate_json(dep, depart_schema, "department")
            if dep.get('id') not in dep_id_list:
                dep_id_list.append(dep.get('id'))
            if userr.get('department_id') not in dep_id_list:
                raise DepartmentName(userr.get('department_id'))
            if userr.get('department_id') == dep.get('id'):
                new_dict.append({"name": userr.get('name'),
                                 "department": dep.get('name')})

    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerows(new_dict)
