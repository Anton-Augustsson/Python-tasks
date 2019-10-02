options2 = {"r":"Try again", "q":"Quit"}
options1 = {"a":"Add item", "l":"List items", "q":"Log out"}

def menu(title, prompt, options):
    print(title)

    for n in options:
        print(f"    {n}) {options[n]}")

    while True:
     o = input(prompt)
     if o in options:
         return o
         #break
     
    
o = menu("Select an action", "Option: ", options1)

print(f"You selected option {o}) {options1[o]}")
print()

o = menu("What do you want to do?", "Option: ", options2)

print(f"You selected option {o}) {options2[o]}" )
