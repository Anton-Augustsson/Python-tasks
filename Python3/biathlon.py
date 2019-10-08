from random import randint

#exec(open("biathlon.py").read())
import time

###########################  Me having fun with welcome splash screen
    
def blank_screen(times, sleep):
    for _ in range(times):
        time.sleep(sleep)
        print()
        
def logo(n):
    blank_screen(40, 0)
    print(f"{n}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n{n}             Biathlon \n{n}           one hit a way \n\n{n}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n", end="\r")
    blank_screen(40, 0)

def bouncing_logo(c):
    times = len(c)
    for n in range(times):
        s = times - n 
        c = c[:-1]  # Removes the length of the string one step at a time
        d = c  # Inorder to use d in loop 
        for _ in range(s):  # loops throw starting posistion to the left corner(end posistion)
            d = d[:-2]  # 2 makes it more natural
            time.sleep(0.005)
            print(f"{d}Biathlon {d}", end="\r")  # Makes the string go back and forth on the same plase 
    time.sleep(2)

def what_is(game_title):
    for n in game_title:
        time.sleep(0.5)
        print(f'Give me an {n}')

def it_is(game_title):
    time.sleep(1)
    print('\n WHAT IS IT?')
    for b in range(len(game_title)):
        time.sleep(0.1)
        a = ""
        for c in range(b):
            a +=   game_title[c] 
        print(a)
        
def splash_extra():
    game_title = ['B', 'i', 'a', 't', 'h', 'l', 'o', 'n']
    c = "                                               "
    what_is(game_title)  
    it_is(game_title)  
    bouncing_logo(c)  
    logo(c)  
    
###########################

def splash():
    splash_extra()
    #print(' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n             Biathlon \n           one hit a way \n\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
def open():
    return 1

def closed():
    return 0

def is_open(target):
    if(target == 1):
        return True
    else:
        return False

def is_closed(target):
    if(target == 1):
        return False
    else:
        return True

def new_targets():
    list = [closed(), closed(), closed(), closed(), closed()]
    #for n in range(5):
    #    list.append(closed())
        
    return list

def hits(targets):
    print()

def random_hit():
    value = randint(0,1)
    if(value == 1):
        return False
    else:
        return True

def shoot(targets, target):
    value = random_hit()
    if(value == True):
        print('Hit on closed target')
    else:
        print('Miss')

####################### Testfall
### Test is open
#a = open()
#b = closed()
#is_open(a)
#is_open(b)
#is_open(open())
#is_open(closed())

### Test is closed
#is_closed(a)
#is_closed(b)
#is_closed(open())
#is_closed(closed())

### Test new_target
#splash()
#print(new_targets())

### Test hits
#ts = new_targets()
#ts
#hits(ts)
#close_target(2, ts)

### Test random_hit
#for _ in range(5):
#    print(random_hit())

### Test Shoot
#ts = new_targets()
#view_targets(ts)
#shoot(ts, 0)
