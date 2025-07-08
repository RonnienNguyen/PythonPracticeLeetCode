a = int(input())
for i in range(a):
    sumN = 0
    b = input()
    c = input().split()
    for i in c:
        sumN+=int(i)
    if((sumN**0.5)%1 != 0):
        print("NO")
    else:
        print("YES")