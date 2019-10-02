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

def user_actions(user, items):
    view(f"Wellcome {user}", items)
    menu("select an action", "option", items)
    
user1 = "nisse"
user2 = "bosse"

items1 = ["luva", "vante"]
items2 = ["hammare", "skruv", "spik"]

user_actions(user1, items1)
print(f"Goodbye {user1}, your items: {items1}")
print()

user_actions(user2, items2)
print(f"Goodbye {user2}, your items: {items2}")
print()
