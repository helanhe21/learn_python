import time

print("\tDog\tBun\tKetchup\tMustard\tOnions\tCalories")
count = 1

dog_cal = 140
bun_cal = 120
ket_cal = 80
mus_cal = 20
onion_cal = 40

for dog in [0, 1]:
    for bun in [0,  1]:
        for ketchup in [0, 1]:
            for mustard in [0, 1]:
                for onion in [0, 1]:
                    print("#", count, "\t", end="")
                    total_cal = dog*dog_cal + bun*bun_cal + ketchup*ket_cal + \
                        mustard*mus_cal + onion*onion_cal
                    print(dog, "\t", bun, "\t", ketchup, "\t", \
                        "\t", mustard, "\t", onion, "\t", total_cal)
                    count += 1

countdown_sec = int(input("How many seconds?"))

for i in range(countdown_sec, 0, -1):
    print(i, end="")
    for j in range(0, i):
        print("*", end="")
    print()
    time.sleep(1)
print("BLAST OFF")
