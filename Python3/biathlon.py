from random import randint

#exec(open("biathlon.py").read())

def splash():
    print(' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n             Biathlon \n           one hit a way \n\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
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
