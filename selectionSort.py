list=[43,2,6,1,67,23,65]
for i in range(len(list)):
    minVal=min(list[i:])
    minInd=list.index(minVal,i)
    list[i],list[minInd]=list[minInd],list[i]
print(list)    
