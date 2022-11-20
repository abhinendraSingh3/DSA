n=int(input())
l=list(n)
for i in range(len(n)):
  k=l[i]
  j=i-1
  while j>=0 and k<l[j]:
    l[j+1]=l[j]
    j=j-1
  else:
    l[j+1]=k
    print("sorted list",l)
    
    
#--------------or--------------#


def insertionSort(myList):
    for i in range (1,len(myList)):
        current_element=myList[i]
        pos=i
        while current_element<myList[pos-1] and pos>0:
            myList[pos]=myList[pos-1]
            pos=pos-1
        myList[pos]=current_element
    
l1=[5,2,6,9,1]
#if you want to take input from the user then 
#n=int(input("enter some number"))
#l1=list(n)
insertionSort(l1)
print(l1)
