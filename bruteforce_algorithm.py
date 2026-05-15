from hashlib import md5

hash = input("Hash")
dic = input("Path")
with open(dic, "r") as file:
        for line in file:
            passw = line.strip()
            hashcheck = md5(passw.encode()).hexdigest()
            if hashcheck == hash:
                print(f"found: {line}")
                break
            
            

