vorodi = input()
if vorodi[0] == 'h' and vorodi[-1] == 'y' and len(vorodi)>2:
    ecount = 2*(len(vorodi)-2)
    print('h'+ecount*'e'+'y')
