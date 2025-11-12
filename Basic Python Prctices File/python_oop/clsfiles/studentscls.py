class Student:
    low_iqLevel = 69
    base_iqLevel1 = 90
    base_iqLevel2 = 109
    high_iqLevel = 140

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