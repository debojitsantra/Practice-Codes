for i in range(5):
    for j in range(5, i, -1):
            print("*", end="")
    for j in range(5, i, -1):
        if i == 1 and (j == 4 or j == 3):
            print(" ", end="") 
        else:
             print(" *", end="")
    print()

for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    for j in range(i + 1):
        print("    *", end="")
    print()