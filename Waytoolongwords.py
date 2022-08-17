n = int(input())
c= 0
for i in range(0,n):
    word = input()
    if len(word)>10:
        c = len(word[1:-1])
        if c>0:
            print(word[0]+str(c)+ word[-1])
    else:
        print(word)