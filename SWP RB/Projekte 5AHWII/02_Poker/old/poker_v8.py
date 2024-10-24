#FALSCH
#% mit flush
import random

# Definition der Kartenwerte und Symbole
kartenwerte = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
symbole = ['♠', '♥', '♦', '♣']
pokerkarten = [wert + symbol for wert in kartenwerte for symbol in symbole]

# Methode, um die Positionen von zwei Elementen in einer Liste zu vertauschen
def vertausche_zwei_index(liste, index1, index2):
    if 0 <= index1 < len(liste) and 0 <= index2 < len(liste):
        liste[index1], liste[index2] = liste[index2], liste[index1]

# Methode, um eine Zufallszahl in einem bestimmten Bereich zu generieren
def generiere_zufallszahl(minimum, maximum):
    return random.randint(minimum, maximum)

# Methode zur Überprüfung der Pokerhand
def ueberpruefe_pokerhand(hand):
    kartenwert_count = {}  # Ein leeres Wörterbuch, um die Anzahl der Karten jedes Werts zu zählen
    kartenwert_list = []  # Eine leere Liste, um die Werte der Karten umzuwandeln und zu sortieren
    symbole_count = {}  # Ein Wörterbuch, um die Anzahl der Karten jedes Symbols zu zählen

    # Zähle die Anzahl der Karten jedes Werts und jedes Symbols und wandele die Werte in numerische Werte um
    for karte in hand:
        # Ermittle den Wert der Karte, indem der Index des Wertes in der Liste 'kartenwerte' gefunden wird
        kartenwert = kartenwerte.index(karte[0]) + 1
        kartenwert_count[kartenwert] = kartenwert_count.get(kartenwert, 0) + 1
        kartenwert_list.append(kartenwert)

        # Zähle die Anzahl der Karten jedes Symbols
        symbol = karte[1]
        symbole_count[symbol] = symbole_count.get(symbol, 0) + 1

    # Sortiere die Kartenwerte in aufsteigender Reihenfolge
    kartenwert_list.sort()

    # Prüfe auf verschiedene Pokerhände in absteigender Reihenfolge der Handwertigkeit
    if 5 in symbole_count.values() and kartenwert_list[-1] - kartenwert_list[0] == 4 and kartenwert_list[-1] == 14:
        return "Royal Flush"
    elif 5 in symbole_count.values() and kartenwert_list[-1] - kartenwert_list[0] == 4:
        return "Straight Flush"
    elif 4 in kartenwert_count.values():
        return "Vierling"
    elif 3 in kartenwert_count.values() and 2 in kartenwert_count.values():
        return "Full House"
    elif 5 in symbole_count.values():
        return "Flush"
    elif kartenwert_list[-1] - kartenwert_list[0] == 4:
        return "Straight"
    elif 3 in kartenwert_count.values():
        return "Drilling"
    elif 2 in kartenwert_count.values() and len(set(kartenwert_list)) == 3:
        return "Zwei Paare"
    elif 2 in kartenwert_count.values():
        return "Paar"
    else:
        return "High Card"

# Hier erstellen wir ein Wörterbuch, um die Häufigkeit der Pokerkombinationen zu verfolgen
ergebnisse = {
    "Royal Flush": 0,
    "Straight Flush": 0,
    "Vierling": 0,
    "Full House": 0,
    "Flush": 0,
    "Straight": 0,
    "Drilling": 0,
    "Zwei Paare": 0,
    "Paar": 0,
    "High Card": 0
}

# Anzahl der Ziehungen
anzahl_ziehungen = 1000

# Jetzt spielen wir das Spiel 1000 Mal
for _ in range(anzahl_ziehungen):
    gezogene_karten = []
    for i in range(5):
        zufallsindex = generiere_zufallszahl(0, len(pokerkarten) - 1)
        gezogene_karten.append(pokerkarten[zufallsindex])
        vertausche_zwei_index(pokerkarten, zufallsindex, len(pokerkarten) - 1 - i)

    hand_text = ueberpruefe_pokerhand(gezogene_karten)
    ergebnisse[hand_text] += 1

# Ausgabe der Ergebnisse in Prozent
for kombination, anzahl in ergebnisse.items():
    prozentanteil = (anzahl / anzahl_ziehungen) * 100
    print(f"{kombination}: {prozentanteil:.2f}%")
