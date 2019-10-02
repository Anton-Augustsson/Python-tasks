sträng = "gandalf"
le = len(sträng)
s = input('hur många gissningar vill du ha? ')

try:
    for n in ranger(s):
        gissning = input('gissa stäng: ')
    lg = len(gissning)
    if(lg < le):
        print('för kort')
    elif(lg > le):
        print('det var lite och ta i')
    else:
        if(sträng == gissning):
            print('hur fan visste du det')
            #break
        else:
            print('bra läng i alla fall')
            if(input('quit? (y)  ') == 'y'):
                print('ok')
                #break

except:
    print('I dont think you wrot a number')
#hile True:
