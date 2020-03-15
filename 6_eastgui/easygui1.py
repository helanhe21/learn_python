import easygui
#flavor = easygui.buttonbox("您选择哪种口味？", choices=['原味','草莓','巧克力'])
flavor = easygui.choicebox("您选择哪种口味？", choices=['原味','草莓','巧克力'])
easygui.msgbox("您选择了" + flavor+"口味")
