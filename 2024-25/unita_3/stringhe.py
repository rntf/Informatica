stringa = "abracadabra cadabra"

if "abra" in stringa:
    if stringa.startswith("abra"):
        print("abra è all'inizio")

    if stringa.endswith("abra"):
        print("abra è ala fine")

    posizione = stringa.find("abra")
    print(f"La prima occorrenza di 'abra' è alla posizione {posizione}")

    posizione2 = stringa.find("abra", posizione + 1)
    print(f"La seconda occorrenza di 'abra' è alla posizione {posizione2}")

else:
    print("abra non è nella stringa")