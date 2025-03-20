n=int(input())
l=list(map(int,input().split()))

while len(l)!=0:
    print(len(l))
    l=[i-min(l) for i in l if i-min(l)>0]
