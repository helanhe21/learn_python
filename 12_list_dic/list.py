family = ["Dad", "Mom", "Brother", "Sister"]
family.append("dd")
print(family[2:5])

name_list = []
for i in range(0, 5):
    name = input("请输入一个名字：")
    name_list.append(name)

print("名字列表包括:")
for j in name_list:
    print(j, " ")

replace_index = int(input("想替换哪一个名字（1~5）："))
name_new = input("请输入新的名字：")
name_list[replace_index-1] = name_new

print("名字列表包括:")
for j in name_list:  
    print(j, " ")

family.sort()
print(family)