a = int(input("Enter The a: "))
b = int(input("Enter The b: "))
c = int(input("Enter The c: "))

if (a > b) and (a > c):
    print("a is large")
elif(b > c):
    print("b is large")
elif(c>b ):
    print("c is large")
else:
    print("same")


