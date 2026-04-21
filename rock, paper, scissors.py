pkt_gracza1 = 0
pkt_gracza2 = 0

opcje = ['kamien', 'papier', 'nozyczki']

while pkt_gracza1 != 3 and pkt_gracza2 != 3:


    wybór_gracza_jest_poprawny = True
    while wybór_gracza_jest_poprawny:
        wybór_gracza1 = input('gracz1 co wybierasz ? ')
        if wybór_gracza1 in opcje:
            wybór_gracza_jest_poprawny = False

    wybór_gracza_jest_poprawny = True
    while wybór_gracza_jest_poprawny:
        wybór_gracza2 = input('gracz2 co wybierasz ? ')
        if wybór_gracza2 in opcje:
            wybór_gracza_jest_poprawny = False




    if (wybór_gracza1 == 'papier' and wybór_gracza2
            == 'kamien'
    or wybór_gracza1 == 'kamien' and wybór_gracza2
            == 'nozyczki'
    or wybór_gracza1 == 'nozyczki' and wybór_gracza2 == 'papier'):
            print('gracz1 wygrywa')
            pkt_gracza1 += 1

    elif wybór_gracza1 == wybór_gracza2:
        print('gracze zremisowali')
    else:
       print('gracz2 wygrywa')
       pkt_gracza2 += 1

if pkt_gracza1 > pkt_gracza2:
    print('Wygrałeś z graczem nr 2')
else:
    print('wygrałeś z graczem nr 1')
