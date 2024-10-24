import random
import functools
import time
from collections import Counter


#global :(
kartenwerte = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
symbole = ['♠', '♥', '♦', '♣']

def vertausche_zwei_index(liste, index1, index2):
    if 0 <= index1 < len(liste) and 0 <= index2 < len(liste):
        liste[index1], liste[index2] = liste[index2], liste[index1]
def generiere_zufallszahl(minimum, maximum):
    return random.randint(minimum, maximum)
def wert_zu_zahl(wert):
    """Konvertiert Kartenwerte in numerische Werte"""
    kartenwert_mapping = {
        '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
        '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }
    return kartenwert_mapping[wert]

def ueberpruefe_pokerhand(hand):
    kartenwert_count = Counter([karte[0:-1] for karte in hand])
    symbole_count = Counter([karte[-1] for karte in hand])
    kartenwerte_sortiert = sorted([wert_zu_zahl(karte[0:-1]) for karte in hand])

    ist_flush = max(symbole_count.values()) == 5
    ist_straight = kartenwerte_sortiert[-1] - kartenwerte_sortiert[0] == 4 and len(set(kartenwerte_sortiert)) == 5
    ist_royal = ist_straight and 10 in kartenwerte_sortiert and 14 in kartenwerte_sortiert

    if ist_flush and ist_royal:
        return "Royal Flush"
    elif ist_flush and ist_straight:
        return "Straight Flush"
    elif 4 in kartenwert_count.values():
        return "Vierling"
    elif 3 in kartenwert_count.values() and 2 in kartenwert_count.values():
        return "Full House"
    elif ist_flush:
        return "Flush"
    elif ist_straight:
        return "Straight"
    elif 3 in kartenwert_count.values():
        return "Drilling"
    elif list(kartenwert_count.values()).count(2) == 2:
        return "Zwei Paare"
    elif 2 in kartenwert_count.values():
        return "Paar"
    else:
        return "High Card"

# Testfall für Royal Flush
test_hand_royal_flush = ['10♠', 'J♠', 'Q♠', 'K♠', 'A♠']
ergebnis = ueberpruefe_pokerhand(test_hand_royal_flush)
print(f"Testhand: {test_hand_royal_flush} -> Ergebnis: {ergebnis}")

