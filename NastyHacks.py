t = int(input())
for i in range(0,t):
    r,e,c = map(int,input().strip().split(' '))
    if e-r == c:
        print('does not matter')
    elif e-r<c:
        print('do not advertise')
    else:
        print('advertise')