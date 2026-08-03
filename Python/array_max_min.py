a = []
n = int(input("Size: "))
for i in range(n):
    print("Enter", i+1, "th Element: ", end = " ")
    a.append(int(input()))
    

max = a[0]
min = a[0]

for i in range(n):
    if max < a[i]:
        max = a[i]

for i in range(n):
    if min > a[i]:
        min = a[i]
        
  
  
print("------------------\nmax: ", max, "\nmin: ", min)



