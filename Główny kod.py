import random, funkcje
chose = None
GODS =["Khorne", "Slanesh", "Nurgle",
       "Tzeentch", "Malal", "Khaine",
       "Sigmar", "Morr", "Ulryk",
       "Grungi", "Grimir", "Valaya",
       "Rogaty Szczur", "Matka Nocy", "Ursun"]

print("\t\t\t\abogowie warhammera".upper())

menu = """  WYBIER CO CHCESZ ZROBIĆ

        1 - nowa gra
        2 - instrukcja
        3 - ranking
        4 - koniec gry"""

while chose != 4:
    print(menu)
    chose = int(input("Chcę: "))
    
    if chose == 1:
        hint = 0
        god = funkcje.mix(GODS)
        score = len(god) * 10 - hint
        new_god = funkcje.jumble(god)
        print("Wylosowałeś tego boga \"", new_god.upper())
        print("Odgadniesz jego imię?")
        print("Aby zakończyć grę bez zgadywania naciśnij Enter")

        answer = None

        while answer != god and answer != "":
            answer = input("Moja odpowiedź to: ".capitalize())
            
            if answer != god:
                print("Niestety nie")
                ask = input("Chcesz podpowiedź? (Tak/Nie) ")

                if ask == "Tak":
                    print("Imię tego boga zaczyna się na", god[0], "a kończy na", god[-1])
                    hint = len(god)/3 * 10

                else:
                    print("Słusznie, szkoda punktów")

            elif answer == god:
                print("Brawo, prawidłowa odpowiedź to", god, "uzyskałeś", score, "punktów.")
        
    elif chose == 4:
        print("Dowidzenia")

input()
