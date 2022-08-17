n = int(input())
counter = 0
for i in range(0,n):
    a,b,c = map(int,input().strip().split(' '))
    if a==1 and b==1 or a==1 and c==1 or b==1 and c==1:
        counter +=1
print(counter)