g, t, n = list(map(int, input().split()))
if 5000 <= g <= 25000 and 3000<= t <= 12000 and 1<=n<=100:
    arr = list(map(int, input().split()))
    print(9 * (g - t) // 10 - sum(arr))