class Employee:
    def __init__(self, full_name, **kwargs):
        self.name = full_name.split(" ")[0]
        self.lastname = full_name.split(" ")[1]
        for key, value in kwargs.items():
            setattr(self, key, value)
