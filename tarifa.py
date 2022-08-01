
x,n = int(input()),int(input())
#get x and n (x is first month and n is number of the months)
result = x*(n+1)
for i in range(n):
    result -= int(input())
print(result)