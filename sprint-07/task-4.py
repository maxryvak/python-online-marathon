class Washing:
    def wash(self):
        print("Washing...")


class Rinsing:
    def rinse(self):
        print("Rinsing...")


class Spinning:
    def spin(self):
        print("Spinning...")


class WashingMachine:
    def __init__(self):
        self.washing = Washing().wash()
        self.rinsing = Rinsing().rinse()
        self.spinning = Spinning().spin()

    def startWashing(self):
        self.__init__()
