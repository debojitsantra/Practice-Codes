import numpy as np
import os
import time

r1, c1 = map(int,input("Enter Rows & Columns for matrix: ").split())

arr1 = np.array([list(map(int, input().split())) 
for _ in range(r1)])
print("Enter Second Matrix: ")
arr2 = np.array([list(map(int, input().split())) 
for _ in range(r1)])


while(1):
   choice = int(input("1. Sum \n2. Substraction\n3. Multiplication\n4. Display Inputs\n5. Exit\n---> "))

   match choice: 
      case 1:
            
         b = arr1+arr2
         print(b)
            
      case 2:
          b = arr1 - arr2
          print("Substract: ",b)
           
      case 3:
           b = arr1*arr2
           print("Multipli: \n",b)
           
      case 4:
           print("1st matrix: \n",arr1)
           print("2nd matrix: \n",arr2)
      case 5:
           exit()
           
   time.sleep(10)
   os.system('clear')
    
         
         

