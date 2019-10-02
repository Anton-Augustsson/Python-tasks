def move(n, From, To):  # Blir mer lättläst i hanoi
    print(str(n) + ":  " + From + " ==> " + To)
               
def hanoi(n, From, To, Extra):
    if(n==1):
        move(n, From, To) 
    else:
        hanoi(n-1, From, Extra, To)  # Ändrar plats Extra till To så att ursprungs platsen och mål ändras beroende på flytt
        move(n, From, To)
        hanoi(n-1, Extra, To, From)  # Samma som inan det tre stegen för hur man flyttar skivorna
                
def start():  # Så man förstår vad bokstäverna representerar
    print('\n\n')
    print('   |    |    |')
    print('   |    |    |')
    print('   |    |    |')
    print('   A    B    C')
    print('\n\n')


start()
hanoi(9, 'A', 'C', 'B')
