class Student:
    low_iqLevel = 69
    base_iqLevel1 = 90
    base_iqLevel2 = 109
    high_iqLevel = 140

    finalOutput = None

    def __init__(self, ids, name, result, iqLevel):
        self.ids = ids
        self.name = name
        self.result = result
        self.iqLevel = iqLevel

        if self.ids <= 100:
            print("First 100's Serial Student's")
        elif self.ids > 100 or self.ids <= 1000:
            print("Second's Serial Student's")
        else:
            print("Last's Serial Student's")

    def studentResult(self):
        if self.result == 5.0 or self.result == 5.00:
            print("Result is A+")
        elif (self.result < 5.0 or self.result < 5.00) and (self.result >= 4.00 or self.result >= 4.0):
            print("Result is A")
        elif (self.result < 4.0 or self.result < 4.00) and (self.result >= 3.50):
            print("Result is A-")
        elif (self.result < 3.50 or self.result >= 3.00) and (self.result >= 3.0):
            print("Result is B")
        elif (self.result < 3.00 or self.result < 3.0) and (self.result >= 2.50):
            print("Result is C")
        elif (self.result < 2.50 or self.result >= 2.00) and (self.result >= 2.0):
            print("Result is D")
        else:
            print("You are Failed")

    def intiligenceStudent(self):
        if self.iqLevel < Student.low_iqLevel:
            print("This is a very Extremely Low level Student")
        elif (self.iqLevel > Student.low_iqLevel) and (self.iqLevel < Student.base_iqLevel1):
            print("This is a Low Average level Student")
        elif (self.iqLevel > Student.base_iqLevel1) and (self.iqLevel < Student.base_iqLevel2):
            print("This is a Average level Student")
        elif (self.iqLevel > Student.base_iqLevel2) and (self.iqLevel < Student.high_iqLevel):
            print("This is a Superior level Student")
        else:
            print("This is a Most Superior level Student")
