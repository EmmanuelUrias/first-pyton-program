def hello():
    print("Hello :)")


hello()


def pack(el1, el2, el3):
    return {el1, el2, el3}


hey = "Hey"
there = "there"
buddy = "buddy"

print(pack(hey, there, buddy))


def eat_lunch(lst):
    for i, item in enumerate(lst):
        if i == 0:
            print(f"First I eat {item}")
        else:
            print(f"Next I eat {item}")
    print("My lunchbox is empty!!")


lst = ["Banana", "Burrito", "Sandwich"]
empty_lst = []
eat_lunch(lst)
