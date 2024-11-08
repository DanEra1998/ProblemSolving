import random

def returnCoin():
    randomValue = random.randint(0,1)
    if(randomValue == 0):
        print("Head")
    else:
        print("Tail")
if __name__ == "__main__":
    returnCoin()