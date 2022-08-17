c = float(input())
if int(c) == c:
    c = int(c)
l = int(input())
answer = 0
for i in range(l):
    h, m = map(float, input().strip().split(' '))
    answer += float(h)*float(m)
print("%.7f" % (answer*c))
