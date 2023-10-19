'''
Naprogramuj hru Oko bere:

    Začínáš se skóre 0 bodů.
    V každém kole:
        Počítač vypíše, kolik máš bodů.
        Počítač se zeptá, jestli chceš pokračovat.
        Pokud byla odpověď „ne“:
            Hra končí.
        Jinak:
            Počítač „vybere kartu“ – náhodně vybere číslo od 2 do 10;
            vybranou hodnotu vypíše;
            přičte tuto hodnotu ke skóre.
        Pokud máš víc než 21 bodů:
            Počítač vypíše, že prohráváš;
            hra končí.
    Po skončení hry počítač vypíše dosažené skóre.
Cílem hry je neprohrát a získat přitom co nejvíc bodů, ideálně 21.
'''
from random import randrange

skore=0
while True:
    print(f'Máš {skore} bodů')
    dotaz = input('Chceš pokračovat?')
    if dotaz == 'ne':
        break
    else:
        hodnota = randrange(2,11)
        print(hodnota)
        skore = hodnota + skore
    if skore > 21:
        print('Prohrál jsi')
        break
print(f'Dosažené skóre je {skore}')
