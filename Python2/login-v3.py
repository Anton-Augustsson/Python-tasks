def menu(title, prompt, options):
    print(title)

    for n in options:
        print(f"    {n}) {options[n]}")

    while True:
        o = input(prompt)
        if o in options:
            return o
     

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


options2 = {"r":"Try again", "q":"Quit"}
options1 = {"a":"Add item", "l":"List items", "q":"Log out"}
users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}

user = login(users)

#exec(open("login-v3.py").read())
