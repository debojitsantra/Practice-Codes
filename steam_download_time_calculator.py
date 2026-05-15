gameSize = float(input("Enter Game Size(in Gb)"))
intSpeed = float(input("Enter Your Internet Speed(In MB/s)"))
gameMb = gameSize * 1024
timeNeed = ((gameMb/intSpeed)/60)/60
print(timeNeed)

