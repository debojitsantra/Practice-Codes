import random
import os
import pyfiglet

def add(k, j, i):
    n1 ,n2 = random.randint(k, j), random.randint(k, j)
    print(f"Level {i}")
    print(f"{n1} + {n2}")
    userinp = int(input(": "))
    if n1+n2 == userinp:
        print("Right!!")       
        if input("Do you want to proceed to another level? (y/n)") == "y":
           i +=1
           k,j = j, j+100*i
           os.system("clear")
           add(k, j, i)
        else:
            return False
    else:
        os.system("clear")
        print("Game Over!!!")


while True:
    if add(1, 100, 1) == True:
        break  
          
          
                