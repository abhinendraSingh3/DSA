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
