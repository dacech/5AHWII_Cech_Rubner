#Ziehung

import random
kartenwerte = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
symbole = ['♠', '♥', '♦', '♣']

pokerkarten = [wert + symbol for wert in kartenwerte for symbol in symbole]

# Methode, um 2 Indizes zu vertauschen
def vertausche_zwei_index(liste, index1, index2):
    if 0 <= index1 < len(liste) and 0 <= index2 < len(liste):
        liste[index1], liste[index2] = liste[index2], liste[index1]
    else:
        print("Ungültige Indexpositionen")

# Methode für Zufallszahl innerhalb eines Bereichs
def generiere_zufallszahl(minimum, maximum):
    return random.randint(minimum, maximum)

# Ziehe 5 Pokerkarten
for i in range(5):
    zufallsindex = generiere_zufallszahl(0, len(pokerkarten) - 1)
    vertausche_zwei_index(pokerkarten, zufallsindex, len(pokerkarten) - 1 - i)

letzte_fuenf_karten = pokerkarten[-5:]
print(letzte_fuenf_karten)

