def login(users):
    while True:
        User = input("User: ")
        Password = input("Password: ")
        if User in users and Password == users[User]:
            return User
        else:
            print("Invalid username or password")
            
users1 = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
users2 = {"foo":"123", "bar":"hello", "foobar":"hello123"}

user = login(users1)

print(f"Welcome {user}")

user = login(users2)

print(f"Welcome {user}")
