list = [3,5,1,2,4,9,8,7,6]
for i in list:
    for j in range(len(list)-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print(list)