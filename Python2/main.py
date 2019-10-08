def menu(title, prompt, options):
    print(title)

    for n in options:  # Printing the items
        print(f"    {n}) {options[n]}")

    while True:
     o = input(prompt) 
     if o in options:  # cecks for valid otion
         return o
         #break

def view(description, strings):
    print(description)
    for n in range(len(strings)):
        print(f"    {n + 1}) {strings[n]}")

def add(prompt, strings):
    strings.append(input(prompt))
    return strings

def login(users):
    while True:
        User = input("User: ")
        Password = input("Password: ")
        if User in users and Password == users[User]:  # Ceck user and the user pasword is corect
            return User
        else:
            print("Invalid username or password")
            o = menu("What do you want to do?", "Option: ", options2)  # option for continuing
            if(str(o) == "q"):  # q is for quiting the login prosess 
                break

def user_actions(user, items):
    view(f"Wellcome {user}", items)
    while True:
        o = menu("select an action", "Option: ", options1)
        if(o == "a"):  # add item
            add("Add item: ", items)
            view("These are your items", items)
        elif(o == "l"):   # list items
            view("These are your items", items)
        else:
            return items


def main(users):
    while True:
        o = menu("Welcome to Lagra (TM) ", "Options: ", options3)
        if(o == "q"):  # q is for quit 
            break
        user = login(users)
        items = data[user]
        user_actions(user, items)

# The dictunaries
options3 = {"l":"Log in", "q":"Quit"}
options2 = {"r":"Try again", "q":"Quit"}
options1 = {"a":"Add item", "l":"List items", "q":"Log out"}
users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
data  = {"nisse":["luva", "vante"],  "stina":[], "bosse":["gräs", "mjölk"]}

# Calling the main funktion
main(users)
