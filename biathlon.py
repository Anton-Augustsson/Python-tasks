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

    return 0 ##flyttade run då det är lättare att förstå context om det är rätt från början



def closed():

    return 1



def is_open(target):

    if(target == open()): ## ändrade till att referera till funktionerna då detta var efterfrågat

        return True

    else:

        return False



def is_closed(target):

    if(target == closed()): ## se ovan

        return True ## bytte plats på true och false då detta är mer logiskt

    else:

        return False



def new_targets():

    list = [open(), open(), open(), open(), open()] ## startar med alla öppna

    #for n in range(5):

    #    list.append(closed())

        

    return list



def close_target(target, targets):
    
    targets[target] = closed()
    
    return targets



def hits(targets):
    counter = 0
    
    ##print() ?????
    for x in range(len(targets)):
        
        if(is_closed(targets[x]) == True): ## ifall den är stängd är sant går countern upp vilket är anledning till ovanstående ändring
            
            counter+=1
            
    return counter
            
   
    
def target_to_string(target):
    
    if(is_open(target) == True):
        
        return "* "
    
    elif(is_closed(target) == True):
        
        return "O "
    
    

def targets_to_string(targets):
    
    s = ""
    
    for x in range(len(targets)):
        
        s = s + target_to_string(targets[x])
        
    return s
    


def view_targets(targets):
    
    print()

    print("0 1 2 3 4")
    
    print()
    
    print(targets_to_string(targets))
          
    return None
        
            

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
