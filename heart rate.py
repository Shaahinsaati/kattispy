n = int(input())

for i in range(n):
    b,p = map(str,input().strip().split(' '))
    b,p = int(b),float(p)
    v = 60*(b/p)
    u = 60/p
    print("%.4f %.4f %.4f" %(v-u,v ,v+u))
