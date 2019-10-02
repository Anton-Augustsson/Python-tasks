ducks = ["knatte", "fnatte", "tjatte"]

def vissa_lista():
    print(f"Lista med ankor: {ducks}")

vissa_lista()

svar = input('Lägg till en anka: ')
ducks.append(svar)

vissa_lista()

# exec(open("add-v1.py").read())
