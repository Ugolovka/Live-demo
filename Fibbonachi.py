list_1 = [18, 42, 23, 10, 66]
list_2 =[]
while len(list_1)>0:
    min= list_1[0]
    for i in range (0, len(list_1)):
        if list_1[i]<min:
            min = list_1[i]
    list_2.append(min)
    list_1.remove(min)
print(list_2)