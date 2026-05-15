uinp = input("Enter 1st Word: ")
uinp1 = input("Enter 2nd Word: ")

u1 = uinp.upper()
u2 = uinp1.upper()


list1 = []
list2 = []
for i in u1:
    list1.append(i)
 
for j in u2:
    list2.append(j)
    
list1.sort() 
list2.sort()

if list1 == list2:
   print("They are anagram")
else:
    print("They are not anagram")







