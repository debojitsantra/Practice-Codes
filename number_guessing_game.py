import random
import os

print("Number Guessing Game")
multip, newmultip  = 1, 100
number = random.randint(multip, newmultip )


def gamef():
  guess = False
  i = 0
  while (guess == False):
    try:
       userinput = int(input("Enter a number: "))
    except ValueError:
      os.system("clear")
      print("Please enter a valid number.")
      continue
    if (userinput > number):
        os.system("clear")
        
        print(f"number is less than {userinput}")
        i = i+1
        continue
        
    elif (userinput < number):
        os.system("clear")
        
        print(f"number is bigger than {userinput}")
        i = i+1
        continue
    elif (userinput == number):
          os.system("clear")
          
          i = i+1
          print(f"You guessed right!! the number was {number}")
          print(f"you guessed it in {i} times")
          break
    else:
        print("error")
                 
gamef()
j = 2
while(1):
    user = input(f"do you want to level {j}? (yes or no): ")
    multip = newmultip
    newmultip = multip + 100*j
    if user.upper() == "YES":
            os.system("clear")
            print(f"level {j}")
            gamef(multip, newmultip)
            j = j+1    
    else:
      os.system("clear")
      print("bye bye...")
      break

    