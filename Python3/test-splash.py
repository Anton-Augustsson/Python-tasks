import time

###########################  Me having fun with welcome splash screen
def splash():
    print(' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n             Biathlon \n           one hit a way \n\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
def splash_extra():    #standard_print_stuff("")
    times = 20
    for n in range(times):
        some_cool_prtint_stuff(n)

    print_blancks(50)   
    #standard_print_stuff()
    print_blancks(20)

def some_cool_prtint_stuff(times):
    for n in range(times):
        time.sleep(0.1)
        ble= "                                                    "
        
        for _ in range(n):
            #ble += "        "
            ble = ble[:-n]
            
        standard_print_stuff(ble)
        print_blancks(20)
        #for c in range(n):
        #    ble +=   game_title[c] 
        #print(ble)

def standard_print_stuff(n):
    #print(' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n             Biathlon \n           one hit a way \n\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'{n} ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n{n}             Biathlon \n{n}           one hit a way \n\n{n} ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def print_blancks(times):
    for _ in range(times):
        print('\n\n')
        
game_title = ['B', 'i', 'a', 't', 'h', 'l', 'o', 'n']
#splash_extra()

###########################


