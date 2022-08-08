import random, funkcje
rank = []
chose = None
text_file = open("gods.txt", "r")
GODS = text_file.readlines()

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
            god = god[0:-1]
            
            new_god = funkcje.jumble(god)
            print("\nWylosowałeś tego boga \"", new_god.upper())
            print("Odgadniesz jego imię?")
            print("Aby zakończyć grę bez zgadywania naciśnij Enter")

            answer = None

            while answer != god and answer != "":
                
                answer = input("\nMoja odpowiedź to: ")
            
                if answer != god and answer != "":
                    print("Niestety nie")
                    ask = input("\nChcesz podpowiedź? (Tak/Nie) ")

                    if ask == "Tak":
                        print("Imię tego boga zaczyna się na", god[0], "a kończy na", god[-1])
                        hint += (len(god) / 3)

                    else:
                        print("Słusznie, szkoda punktów")

                elif answer == god:
                    print("Brawo, prawidłowa odpowiedź to", god, ".")
                    score = len(god) * 10 - float(hint * 10)
                    points += score

        player_name = input("\nJak Cię zwą wybrańcze bogów? ")
        entry = (points, player_name)
        rank.append(entry)
        rank.sort(reverse = True)
        rank = rank[:5]

        print("Uzyskałeś łącznie", points, "punktów.")

    elif chose == "2":
        funkcje.instruction()

    elif chose == "3":
        for entry in rank:
            points, player_name = entry
            print(points, "\t", player_name)
        
    elif chose == "4":
        print("Dowidzenia")

input()
