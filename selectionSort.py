# list=[43,2,6,1,67,23,65]
# for i in range(len(list)):
#     minVal=min(list[i:])
#     minInd=list.index(minVal,i)
#     list[i],list[minInd]=list[minInd],list[i]
# print(list) 

#-----or------#
list=[43,2,6,1,67,23,65]\

for i in range(len(list)):
    minVal=i

    for j in range(i+1,len(list)):
        if list[minVal]>list[j]:
            minVal=j
            
    #swapping
    list[i],list[minVal]=list[minVal],list[i]

for i in range(len(list)):
    print("%d" %list[i],end=" ")
