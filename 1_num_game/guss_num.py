import random
secret = random.randint(1, 50)
guss = 0
tries = 0
print("play thsi game")
while guss != secret and tries < 6:
    guss = int(input("please input a new number"))
    if(guss > secret):
        print("the number is greater than goal")
    if(guss < secret):
        print("the number is lower than goal")
    tries += 1
    
if guss == secret:
    print("you got it :"+str(guss)+" "+str(secret))
if tries >=6:
    print("tries is over")
    
