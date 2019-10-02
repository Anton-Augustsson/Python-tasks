n = 40  # antal gånger som den ska köra

for n in range(1, n +1):
    if (n % 15 == 0):
        print('flipp blipp')
        
    elif (n % 5 == 0):
        print('blipp')
        
    elif (n % 3 == 0):
        print('flipp')
        
    else:
        print(n)

#exec(open("flippblipp-v1.py").read())
