import random, funkcje
rank = []
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

while chose != "4":
    print(menu)
    chose = input("Chcę: ")
    
    if chose == "1":
        points = 0
        for i in range(3):
            
            hint = 0
            god = funkcje.mix(GODS)
            
            new_god = funkcje.jumble(god)
            print("Wylosowałeś tego boga \"", new_god.upper())
            print("Odgadniesz jego imię?")
            print("Aby zakończyć grę bez zgadywania naciśnij Enter")

            answer = None

            while answer != god and answer != "":
                
                answer = input("Moja odpowiedź to: ")
            
                if answer != god and answer != "":
                    print("Niestety nie")
                    ask = input("Chcesz podpowiedź? (Tak/Nie) ")

                    if ask == "Tak":
                        print("Imię tego boga zaczyna się na", god[0], "a kończy na", god[-1])
                        hint += (len(god) / 3)

                    else:
                        print("Słusznie, szkoda punktów")

                elif answer == god:
                    print("Brawo, prawidłowa odpowiedź to", god, ".")
                    score = len(god) * 10 - float(hint * 10)
                    points += score

        player_name = input("Jak Cię zwą wybrańcze bogów? ")
        entry = (player_name, points)
        rank.append(entry)

        print("Uzyskałeś łącznie", points, "punktów.")

    elif chose == "2":
        funkcje.instruction()
        
    elif chose == "4":
        print("Dowidzenia")
        print(rank)

input()
