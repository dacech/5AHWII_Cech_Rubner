#anpassung royal flush
import random
import functools
import time

#global :(
kartenwerte = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
symbole = ['♠', '♥', '♦', '♣']

def vertausche_zwei_index(liste, index1, index2):
    if 0 <= index1 < len(liste) and 0 <= index2 < len(liste):
        liste[index1], liste[index2] = liste[index2], liste[index1]
def generiere_zufallszahl(minimum, maximum):
    return random.randint(minimum, maximum)
def ueberpruefe_pokerhand(hand):
    kartenwert_count = {}
    kartenwert_list = []
    symbole_count = {}

    for karte in hand:
        kartenwert = kartenwerte.index(karte[0]) + 1
        kartenwert_count[kartenwert] = kartenwert_count.get(kartenwert, 0) + 1
        kartenwert_list.append(kartenwert)

        symbol = karte[1]
        symbole_count[symbol] = symbole_count.get(symbol, 0) + 1

    kartenwert_list.sort()

    if 5 in symbole_count.values() and kartenwert_list[-1] - kartenwert_list[0] == 4 and 14 in kartenwert_list:
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

    for _ in range(anzahl_ziehungen):
        gezogene_karten = []
        for i in range(5):
            zufallsindex = generiere_zufallszahl(0, len(pokerkarten) - 1)
            gezogene_karten.append(pokerkarten[zufallsindex])
            vertausche_zwei_index(pokerkarten, zufallsindex, len(pokerkarten) - 1 - i)

        hand_text = ueberpruefe_pokerhand(gezogene_karten)
        ergebnisse[hand_text] += 1

    for kombination, anzahl in ergebnisse.items():
        prozentanteil = (anzahl / anzahl_ziehungen) * 100
        print(f"{kombination}: {prozentanteil:.3f}%")



if __name__ == "__main__":
    main()
