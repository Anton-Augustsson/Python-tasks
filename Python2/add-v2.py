ducks = ["knatte", "fnatte", "tjatte"]
composers = ["mozart", "bache"]

def add(prompt, strings):
    strings.append(input(prompt))
    return strings

print(f"       Ankor: {ducks}")
print(f"Kompositörer: {composers}")
print()

alias1 = add("Lägg till en anka: ", ducks)

print(f"       Ankor: {ducks}")
print(f"      alias1: {alias1}")
print()

alias2 = add("Lägg till en kompositör: ", composers)

print(f"Kompositörer: {composers}")
print(f"      alias2: {alias2}")
print()
