import unittest


class Worker:
    def __init__(self, name, salary=0):
        if salary < 0:
            raise ValueError
        else:
            self.salary = salary
            self.name = name

    def get_tax_value(self):
        percents = [0.0, 0.1, 0.15, 0.21, 0.3, 0.4, 0.47]
        thresholds = [0, 1000, 3000, 5000, 10000, 20000, 50000]

        taxes = 0
        for i in range(len(percents)):
            if i == len(thresholds) - 1 or self.salary < thresholds[i + 1]:
                taxes += (self.salary - thresholds[i]) * percents[i]
                break
            else:
                taxes += (thresholds[i + 1] - thresholds[i]) * percents[i]
        return taxes


class WorkerTest(unittest.TestCase):
    #your code
    def setUp(self):
        self.s = 100000

    def test_correct(self):
        w = Worker('dfg', self.s)
        self.assertEqual(w.get_tax_value(), 40050.0)
    
    @unittest.expectedFailure
    def test_incorrect(self):
        w = Worker('dfg', -3)
        self.assertNotEqual(w.get_tax_value(), 400.0)
