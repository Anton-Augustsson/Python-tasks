def fråga():
    svar = input("skriv smeknamn: ")
    Quit = input("ge upp: ")
    return svar, Quit

def main():
    print("q för quit")
    while True:
        svar, Quit = fråga()
        if(svar == "bosse"):
            print("du gissade rätt")
            break
        elif(Quit == "q"):
            print("quit")
            break
        else:
            print("wrong")

main()
