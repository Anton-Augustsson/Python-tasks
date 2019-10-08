
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

####################### Testfall
#a = open()
#b = closed()
#is_open(a)
#is_open(b)
#is_open(open())
#is_open(closed())

#is_closed(a)
#is_closed(b)
#is_closed(open())
#is_closed(closed())

#splash()
#print(new_targets())
