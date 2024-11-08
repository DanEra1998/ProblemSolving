class DynamicArray:
    def __init__(self, capacity: int):
        # time complexity is O(n)
        # capacity is the maxsize of the array but if you have not inserted anything, then the size is 0 but is can hold
        # up to the max capacity, in this case, we just call it capacity
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity
    # O(1)
    def get(self, i: int)-> int:
        return self.arr[i]
    # O(1)
    def insert(self, i: int, n: int)-> None:
        # i represents the index of the element in the array
        # the following is read as, "at index i in arr, we set n to that location
        # overwritting a value at i with the value n
        self.arr[i] = n
    # O(1) - avg case/ Ammortized time complexity
    def pushback(self, n: int)-> None:

        # we are prown to out of bound error so we should check
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1
    # O(1)
    def popback(self) -> int:
        self.size -=1
        return self.arr[self.size]
    # O(n)

    # //////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////



    def resize(self)-> None:
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity
    #   recall that not only do we have increase our capacity by double but we also have to copy the value from the
    #   current array to the new array
        for i in range(self.size):
            self.new_arr[i] = self.arr[i]

        self.arr = new_arr
    # O(1)

    def getSize(self)->int:
        return self.size
    # O(1)
    def getCapacity(self)->int:
        # apparently capacity and size are not the same? Im still not understanding but our brains do not work that way
        # we have to learn by constant repetition
        return self.capacity