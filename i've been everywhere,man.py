n = int(input())

for i in range(n):
    t = int(input())
    places = set()
    
    for j in range(t):
        p = input().strip()
        places.add(p)
        
    print(len(places))