def flippblipp(n):
    if(n % 15 == 0): # (n % 3 == 0 and n % 5 == 0):
        return 'flipp blipp'
        
    elif (n % 5 == 0):
        return 'blipp'
        
    elif (n % 3 == 0):
        return 'flipp'
        
    else:
        return str(n)

        
n = 15

for n in range(1, n + 1):
    svar = flippblipp(n) 
    print(svar)

# exec(open("flippblipp-v2.py").read())
