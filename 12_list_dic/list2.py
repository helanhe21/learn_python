friends = ["json","hary","yy","lili"]
print(friends)
friends.pop()

new_friends = friends[:]
print(new_friends)

names = []
for i in range(0, 5):
    name = input("please enter a name: ")
    names.append(name)
print("The name are", names)
names.sort()
print(names)
print("The third name you entered is :", names[2])

index_replace = int(input("which name do you want to replace,please input the index(1-5)"))
if(index_replace > 5 or index_replace < 1):
    print("you input a error index")
else:
    new_name = input("please input a new name: ")
    names[index_replace-1] = new_name
    print(names)
