tank_size = float(input("邮箱多少升？"))
persent = float(input("油还剩百分之多少？"))
liter_per_km = float(input("百公里油耗是多少升？"))
red_line = 5

distance_left = (tank_size - red_line)*persent / liter_per_km

if(distance_left >200):
    print("你还能开" + str(distance_left)+"公里")
    print("下一个油站离您200公里，你可以到下一个油站加油！")
else:
    print("下一个油站离您200公里, 你的油不够了，需要尽快加油")
