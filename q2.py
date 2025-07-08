n = int(input())
l=[]
 
for _ in range(n):
    p,q=map(int, input().split())
    l.append((p,q))
l.sort()
for i in range(1, n):
    if l[i-1][1]>l[i][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")