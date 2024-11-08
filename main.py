import random
from myPizza import MyPizza
from FizzBuzz import FizzBuzz
from DynamicArray import DynamicArray
from Love_Calculator import Love_Cal
##########################################################################################
##########################################################################################
                                    #ALGORITHMS
##########################################################################################
##########################################################################################

# the -> None does not have to be there but helps the programmer understand that
# the function does not return anyting, python allows for hints of what the parameter is
def insertionSort(Array : list) -> None:
    # when viewing the pseudocode, we had (A : list of items) which is convention for an expectation of items
    # in list format
    # recall that we start at position 2 in the array or index 1 and
    # recall that range in python is not inclusive for the last index
    # i believe it goes from 1 up to the end - 1

    for i in range(1, len(Array)):
        # we are holding the current value in question to be either sorted or not
        temp = Array[i]

        j = i - 1

        while  j >= 0 and Array[j] > temp:
            Array[j + 1] = Array[j]
            j = j - 1

        Array[j + 1] = temp



def BinarySearch(Array, target):
    low = 0
    high = len(Array) - 1
    while low <= high:
        mid = (low + high) // 2
        if Array[mid] == target:
            return mid
        if Array[mid] < target:
            # moves to the right
            low = mid + 1
        else:
            # move to the left
            high = mid - 1
    return -1

def selctionSort(Array):
    for i in range(0,len(Array)):
        min_index = i
        for j in range(i + 1, len(Array)):
            if Array[j] < Array[min_index]:
                min_index = j
        if min_index != i:
            # Correct swap operation
            Array[i], Array[min_index] = Array[min_index], Array[i]
    return Array

def linearSerach(Array, target):
    for i in range(len(Array)):
        if Array[i] == target:
            return Array[i]
    return -1
##########################################################################################
##########################################################################################
                             # END OF ALGORITHMS
##########################################################################################
##########################################################################################





##########################################################################################
##########################################################################################
                             # MATRIX
##########################################################################################
##########################################################################################

def creatingMatrix(row, col):
    # okay so to print a matrix, we do need a datastructure such as a matrix
    # python has list so we will use list
    matrix = []
    value = 1
    for i in range(row):
        row = []
        for j in range(col):
            row.append(value)
            value += 1
        matrix.append(row)
    return matrix

def printingMatrix(matrix, row, col):
    for i in range(row):
        for j in range(col):
            print(matrix[i][j], end=" ")
        print()



##########################################################################################
##########################################################################################
                           #Classes
##########################################################################################
##########################################################################################
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        #you can define a variable here
        self.odometer_reading = 0
    def car_description(self):
        description = f"{self.year} {self.make} {self.model}"
        return description
    def read_odometer(self):
        return f"car odeometer {self.odometer_reading}"
    def increment_odometer(self,miles):
        self.odometer_reading += miles

##########################################################################################
##########################################################################################
                           #LinkedList
##########################################################################################
##########################################################################################
class Node:
    def __init__(self, value):
        self.value = value;
        self.next = None;

class LinkedList:
    # what all these functions have in common is that they need to create a node
    def __init__(self, value):
        #creation of new node by calling the constructor of the Node class
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)

        # this was my way -> if self.tail == None and self.tail == None:
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        # if you reach here, then you have added a node to the list hence you must increase the size by 1 node
        self.length += 1
        # in the future you might need to know if the append was successful so you can return true
        return True
        # if we get here then the tails next points to the new node and tail itself points to the new node
        # almost, below is Daniels original code, you got it mostly correct but forgot to increase the length
        # self.tail.next = new_node
        # self.tail = new_node

    def pop(self,index,value):
        pass
    def prepend(self,value):
        pass
    def insert(self,index,value):
        pass


##########################################################################################
##########################################################################################
                           #built in useful functions in python
##########################################################################################
##########################################################################################
people = ["Daniel", "jake", "Henry", "Natalie"]
age = [30,40,50,18]
# zip will be bottlenecked by the smallest list, so for example, say age had only 3 elements, then the zip function
# would only print in tuple form, (daniel, age1) (Jake, age2) (Henry, age3) 

print("-----------------------------------")
for people, age in zip(people,age):
    print(f"({people}, {age})")
print("-----------------------------------")


# using random, this function is inclusive, I will get a random number
# between 1 (including 1) and 10 (including 10)
random_integer = random.randint(1,10)

# now what if you wanted to print out a random float number
# well we have a function from that called random() which
# will print a random float from 0.0 (inclusive) up to 1 (exclusive)
random_float_between_zero_and_one = random.random()

# now we can use the uniform() function to return a set range, we the programmer set
random_float_ranged = random.uniform(1,15)

##########################################################################################
##########################################################################################
                             # OUR TESTING GROUND
##########################################################################################
##########################################################################################


if __name__ == "__main__":
    print("commented out everything for now")
    # Uncomment below to run BinarySearch
    # result = BinarySearch([1,2,3,5,6,40], 40)
    # print(result)

    # beforeInsertionSort = [1,4,2,6,90,39,22,33,44,55,66,77,3,4,5,6,2,1,3,4,5,6,7,7,8,88,99,8,67,1,2,3,1,2,3,4,545]
    # insertionSort(beforeInsertionSort)
    # print("After Insertion Sort:", beforeInsertionSort)

    # Uncomment below to run Matrix creation and printing
    # m = creatingMatrix(5,5)
    # printingMatrix(m, 5,5)
    # element = m[2][2]
    # print("This is my element:", element)

    # #calling my car example class
    # myCar = Car("Honda", "Civic", 2022)
    # print(myCar.car_description())
    # print(myCar.read_odometer())
    # for i in range(0,5):
    #     myCar.increment_odometer(500)
    #     print(myCar.read_odometer())

    Array = [10,29,14,37,13]
    print(selctionSort(Array))

    r = linearSerach(Array, 100)
    print(r)


    my_linked_list = LinkedList(0)
    my_linked_list.append(5)
    print("below we use print_list")
    my_linked_list.print_list()


    # print(f"printing random integer {random_integer}")
    # print(f"my fav number: {My_module.my_fav_num}")
    # print(f"random number between 0 inclusive and 1 exclusive {random_float_between_zero_and_one}")
    # print(f"random float number in a set range {random_float_ranged}")
    print("\n=================================================================================\n")
    fizzbuzz_instance = FizzBuzz(15)



    print(fizzbuzz_instance.main_algorithm())

    dynamic_array = DynamicArray(4)
    dynamic_array.pushback(4)
    print(dynamic_array.get(0))
    print(dynamic_array.getSize())


    s = "Daniel"
    left = 1
    print(s[left])
    print("//////////////////////////////////////////////////")
    love_cal_instance = Love_Cal("daniel", "natalie")
    print(love_cal_instance.calculate_love_score())