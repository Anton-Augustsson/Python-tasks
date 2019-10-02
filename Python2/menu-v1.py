options = {"a":"Add item", "l":"List items", "q":"Log out"}

def view(description, strings):
    print(description)
    for n in strings:
        print(f"    {n}) {strings[n]}")

view("Du har matat in följande n strängar", options)

while True:
     o = input("Option: ")
     if o in options:
         print(f"You selected option {o}) {options[o]}")
         break
