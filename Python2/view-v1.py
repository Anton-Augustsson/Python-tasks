names = ["nisse", "stina", "bosse", "mimmi"]

def good():
    x = 1
    for n in names:
        print(f"    {x}) {n}")
        x += 1

def better():
    for n in range(len(names)):
        print(f"    {n + 1}) {names[n]}")

better()
