class Array_Basics:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = []
        for i in range(capacity):
            self.array.append(i)

    def printArray(self):
        print(self.array)
    def insert_Front(self, element):
        self.array.append(0)  # Step 1: Make space
        for i in range(len(self.array) - 2, -1, -1):
            self.array[i + 1] = self.array[i]
        self.array[0] = element  # Step 3: Insert at front



if __name__ == "__main__":
    a = Array_Basics(5)
    a.printArray()
    a.insert_Front(10)
    a.printArray()