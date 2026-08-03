st = input("Enter a string: ")
a = ["Fuck", "fuck", "Fcuk", "fcuk", "ass", "asshole", "piece of shit", "Slut", "Pervert"]
i = 0
t2 = False
while i < len(a):
    tracker = a[i] in st
    if tracker == True:
        t2 = True
    i += 1



if t2 == True:
    print("You Entered a bad lang")
else:
    print("Good Person")
    
    