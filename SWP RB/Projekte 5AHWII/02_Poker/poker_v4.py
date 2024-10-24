#mit tqdm
from tqdm import tqdm
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

#timer
def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


@timer
def main():
    pokerkarten = [wert + symbol for wert in kartenwerte for symbol in symbole]

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

    anzahl_ziehungen = 1000000

    # tqdm für die Fortschrittsanzeige verwenden ("for _ in range(anzahl_ziehungen):")
    for _ in tqdm(range(anzahl_ziehungen), desc="Ziehungen werden durchgeführt"):
        gezogene_karten = []
        for i in range(5):
            zufallsindex = generiere_zufallszahl(0, len(pokerkarten) - 1)
            gezogene_karten.append(pokerkarten[zufallsindex])
            vertausche_zwei_index(pokerkarten, zufallsindex, len(pokerkarten) - 1 - i)

        hand_text = ueberpruefe_pokerhand(gezogene_karten)
        ergebnisse[hand_text] += 1

    for kombination, anzahl in ergebnisse.items():
        prozentanteil = (anzahl / anzahl_ziehungen) * 100
        print(f"{kombination}: {prozentanteil:.3f}% ({anzahl})")

if __name__ == "__main__":
    main()
