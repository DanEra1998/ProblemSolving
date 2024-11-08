class Love_Cal:
    def __init__(self, name_1, name_2):
        self.name_1 = name_1
        self.name_2 = name_2

    def calculate_love_score(self):
        counter_n1 = 0
        counter_n2 = 0
        for letter in self.name_1.lower():
            if letter in "true":
                counter_n1 += 1
            if letter in "love":
                counter_n2 += 1
        for letter_2 in self.name_2.lower():
            if letter_2 in "true":
                counter_n1 += 1
            if letter_2 in "love":
                counter_n2 += 1

        s = str(counter_n1) + str(counter_n2)
        return s


