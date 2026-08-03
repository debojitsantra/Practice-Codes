import os
a = []
j = int(input("Enter The Number Of Elements: "))
os.system("clear")
i = 0

print("Enter Elements Cutie: ")
for i in range(j):
    item = int(input())
    a.append(item)
    
    
print("------------------")
r = 0
s = 0
for i in range(j):
    s += a[i]
    r += 1

print(s)