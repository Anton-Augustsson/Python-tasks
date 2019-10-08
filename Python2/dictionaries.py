users = {"nisse":"apa", "bosse":"ko", "stina":"t-rex"}
data = {"nisse":["luva", "vante"], "bosse":["spik", "skruv", "hammare"], "stina":["tidsmaskin"]}

def view(description, strings):
    print(description)
    for n in strings:
        print(f"    {n}) {strings[n]}")


print('Användare')
for n in users:
    print(f"    {n}")

view("Användare och Lösenord", users)
view("Användare och deras data", data)

andvändare = input('Användare: ')
if andvändare in data:
    print(f"Data lagrat för {andvändare}: {data[andvändare]}")
else:
    print(f"Användare: {andvändare} finns inte")


#exec(open("dictionaries.py").read())
