import random, easygui
secret = random.randint(1, 100)
guss = 0
tries = 0
easygui.msgbox("""玩个猜数字游戏
1到99之间有个数，猜猜它是多少？""")

while guss != secret and tries < 6:
    guss = easygui.integerbox("你猜是多少")
    if not guss:
        break
    if guss < secret:
        easygui.msgbox("您猜的数字小了:"+str(guss))
    if guss > secret:
        easygui.msgbox("您猜的数字大了:"+str(guss))
    tries += 1

if guss == secret:
    easygui.msgbox("您猜对了")
elif tries >= 6:
    easygui.msgbox("您的机会用完了, Game OVER!")
else:
    easygui.msgbox("你没有输入数字，Game Over!")
