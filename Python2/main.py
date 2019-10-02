def menu(title, prompt, options):
    print(title)

    for n in options:
        print(f"    {n}) {options[n]}")

    while True:
     o = input(prompt)
     if o in options:
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
        if User in users and Password == users[User]:
            return User
        else:
            print("Invalid username or password")
            o = menu("What do you want to do?", "Option: ", options2)
            if(str(o) == "q"):
                break

def user_actions(user, items):
    view(f"Wellcome {user}", items)
    while True:
        o = menu("select an action", "Option: ", options1)
        if(o == "a"):
            add("Add item: ", items)
            view("These are your items", items)
        elif(o == "l"):
            view("These are your items", items)
        else:
            return items


def main(users):
    while True:
        o = menu("Welcome to Lagra (TM) ", "Options: ", options3)
        if(o == "q"):
            break
        user = login(users)
        items = data[user]
        user_actions(user, items)

options3 = {"l":"Log in", "q":"Quit"}
options2 = {"r":"Try again", "q":"Quit"}
options1 = {"a":"Add item", "l":"List items", "q":"Log out"}
users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
data  = {"nisse":["luva", "vante"],  "stina":[], "bosse":["gräs", "mjölk"]}

main(users)
