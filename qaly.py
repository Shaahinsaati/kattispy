N = int(input())
sum = 0
if 1<= N <= 100:
    for i in range(0, N):
        q, y = map(float,input().strip().split(' '))
        if 0 < q <=1 and 0<y<=100:
            sum += q * y
print("%.3f" % sum)