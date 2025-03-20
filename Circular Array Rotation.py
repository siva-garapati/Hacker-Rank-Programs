n,k,q = map(int,input().split())

a = list(map(int,input().split()))

queries = [int(input()) for i in range(q)]

for i in range(k):
    a.insert(0,a.pop())
    
for i in queries:
    print(a[i])
