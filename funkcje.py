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
        
        
    
