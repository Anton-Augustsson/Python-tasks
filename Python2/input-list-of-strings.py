def view(description, strings):
    print(description)
    for n in range(len(strings)):
        print(f"    {n + 1}) {strings[n]}")

def add(prompt, strings):
    strings.append(input(prompt))
    return strings

strings = []

for n in range(int(input('n = '))):
    add("Lägg till en sträng: ", strings)

view("Du har matat in följande n strängar", strings)
