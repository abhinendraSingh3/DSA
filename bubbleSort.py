list1=[23,12,43,65,1]
for i in range(len(list1)-1):
    for j in range(len(list1)-1):
        if list1[j]>list1[j+1]:
            #swapping
            list1[j],list1[j+1]=list1[j+1],list1[j]
print(list1)             
