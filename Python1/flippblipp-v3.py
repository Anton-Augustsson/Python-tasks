def flippblipp(n):
    if (n % 15 == 0): # samma som (n % 3 == 0 and n % 5 == 0):
        return 'flipp blipp'
        
    elif (n % 5 == 0):
        return 'blipp'
        
    elif (n % 3 == 0):
        return 'flipp'
        
    else:
        return str(n)

n = 1
print(n)

while True:
    n = n + 1

    svar = input('Nästa: ').lower().strip()  # konverteras till små boxstäver och tar bort mellanslag
    facit = flippblipp(n)
    
    if(svar != facit.strip()):
        #print('Fel - ' + facit + '\n\n' + 'Game Over' + '\n')
        print(f"Fel - {facit}\n\nGame Over \n")
        break

# exec(open("flippblipp-v3.py").read())
