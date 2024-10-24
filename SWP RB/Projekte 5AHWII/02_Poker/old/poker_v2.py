#Farben erkennen

import random
# Definition der Kartenwerte und Symbole
kartenwerte = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
symbole = ['♠', '♥', '♦', '♣']
pokerkarten = [wert + symbol for wert in kartenwerte for symbol in symbole]

# Methode, um die Positionen von zwei Elementen in einer Liste zu vertauschen
def vertausche_zwei_index(liste, index1, index2):
    if 0 <= index1 < len(liste) and 0 <= index2 < len(liste):
        liste[index1], liste[index2] = liste[index2], liste[index1]
    else:
        print("Ungültige Indexpositionen")

# Methode, um eine Zufallszahl in einem bestimmten Bereich zu generieren
def generiere_zufallszahl(minimum, maximum):
    return random.randint(minimum, maximum)

# Methode zur Überprüfung der Pokerhand
def ueberpruefe_pokerhand(hand):
    symbole_in_hand = set()

    for karte in hand:
        if "♠" in karte:
            symbole_in_hand.add("Pik")
        elif "♥" in karte:
            symbole_in_hand.add("Herz")
        elif "♦" in karte:
            symbole_in_hand.add("Karo")
        elif "♣" in karte:
            symbole_in_hand.add("Kreuz")

    if not symbole_in_hand:
        return "Was hast du für eine Scheiße gebaut, damit du diese Fehlermeldung siehst?"
    else:
        ausgabe = "Sie haben "
        ausgabe += " und ".join(symbole_in_hand)
        return ausgabe


# Ziehe 5 Pokerkarten zufällig
gezogene_karten = []
for i in range(5):
    zufallsindex = generiere_zufallszahl(0, len(pokerkarten) - 1)
    gezogene_karten.append(pokerkarten[zufallsindex])
    vertausche_zwei_index(pokerkarten, zufallsindex, len(pokerkarten) - 1 - i)

print("Ihre Pokerhand: ", gezogene_karten)
ergebnis = ueberpruefe_pokerhand(gezogene_karten)
print(ergebnis)
