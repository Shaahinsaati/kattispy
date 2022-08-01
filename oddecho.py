number = int(input())
list_vorodiha = []
for i in range(number):
    vorodi = input()
    list_vorodiha.append(vorodi)
for i in range(1,len(list_vorodiha)+1):
    if i%2 != 0:
        print(list_vorodiha[i-1])