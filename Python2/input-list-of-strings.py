def view(description, strings):
    print(description)
    for n in range(len(strings)):
        print(f"    {n + 1}) {strings[n]}")

def add(prompt, strings):
    strings.append(input(prompt))
    return strings

strings = []
times = int(input('n = '))
for n in range(times):
    add("Lägg till en sträng: ", strings)

view(f"Du har matat in följande {times} strängar", strings)
