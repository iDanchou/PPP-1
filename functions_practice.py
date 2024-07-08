def hello():
    print("Hello!")

def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

def eat_lunch(food):
    if len(food) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(food)):
            if i == 0:
                print(f"First, I will eat {food[0]}")
            else:
                print(f"Then, I will eat {food[i]}")

hello()
print(pack(1, 2, 3))
eat_lunch(["apple", "banana", "carrot"])
eat_lunch([])
