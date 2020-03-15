import time

for i in range(5):
    for j in range(3):
        print("*", end="")

print()

for multi in range(5,8):
    for i in range(1,11):
        print(i, "*", multi, "=", i*multi)
    print()

for i in range(5,0,-1):
    print(i,end="")
    time.sleep(1)
    for j in range(i):
        print("*",end="")
    print()
print("汽车人出发")

for i in range(1, 10):
    for j in range(1, i+1):
        print(i, "*", j, "=", i*j, end=" ")
    print()
