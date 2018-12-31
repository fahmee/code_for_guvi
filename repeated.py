N=int(int(input()))
c=False
a=sorted([int(i) for i in input().split()])
for i in set(a):
    if(a.count(i)>1):
        print(i,end=" ")
        c=True
if(c==False):
    print("unique")
