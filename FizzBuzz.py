class FizzBuzz:
    def __init__(self, n: int):
        self.n = n

    def main_algorithm(self):

        str_list = []
        for i in range(1, self.n + 1):
            # We will use the parity of numbers
            if i % 3 == 0 and i % 5 == 0:
                str_list.append("FizzBuzz")
            elif i % 3 == 0:
                str_list.append("Fizz")
            elif i % 5 == 0:
                str_list.append("Buzz")
            else:
                str_list.append(str(i))

        return str_list


if __name__ == "__main__":
    print("Daniel is awesome in fizzbuzz")




