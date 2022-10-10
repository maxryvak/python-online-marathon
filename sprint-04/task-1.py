class Employee:
    firstname = ''
    lastname = ''
    salary = 0
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @staticmethod
    def from_string(string):
        string = string.split("-")
        Employee.firstname, Employee.lastname, Employee.salary = string[0], string[1], int(string[2])
        return Employee
