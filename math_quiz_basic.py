import random

def nmber():
    n1 = random.randint(0, 100)
    n2 = random.randint(0, 100)
    print(f"{n1} + {n2}")
    ui = int(input(": "))
    if ui == (n1+n2):
        print("right!!")
    else:
        print("wrong!!!")

while(1):
    nmber()
    