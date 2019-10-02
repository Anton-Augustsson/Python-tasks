users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}

def login(users):
    while True:
        User = input("User: ")
        Password = input("Password: ")
        if User in users and Password == users[User]:
            break
        else:
            print("Invalid username or password")

login(users)
