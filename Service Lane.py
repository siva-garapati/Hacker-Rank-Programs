n,t = map(int,input().split())
wid=list(map(int,input().split()))
for _ in range(t):
    i,j=map(int,input().split())
    print(min(wid[i:j+1]))
