list1  = eval(input())
list2 = eval(input())
list3 = []
for i in range(len(list1)):
    if list1[i] % 2 != 0:
        list3.append(list1[i])
for i in range(len(list2)):
    if list2[i] % 2 == 0:
        list3.append(list2[i])
        
print(list3)