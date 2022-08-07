import random

def mix(sets):
    """wybór boga do odgadnięcia"""
    word = random.choice(sets)
    return word

def jumble(i):
    g = ""
    while i:
        j = random.randrange(len(i))
        g += i[j]
        i = i[:j]+i[(j+1):]
        g = g.upper()
    return g

def instruction():
    print("""
    Bogowie domagają się twojej atencji wybrańcze.
    Najpierw los wybierze, którego Boga imię masz odgadnąć.
    Zostaną Ci pokazane wszystkie runy, które tworzą jego imię,
    lecz w losowej kolejności. Jeśli okaże się to zatrudne,
    możesz poprosić o wskazówkę, lecz łaski bogów nie będą aż tak hojne.""")
          
        
        
    
