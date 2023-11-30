from abc import ABC


class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    def __str__(self):
        return f'Szobaszám: {self.szobaszam}, Ár: {self.ar}'


class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, klima):
        self.klima = klima
        super().__init__(ar, szobaszam)


class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam, kilatas):
        self.kilatas = kilatas
        super().__init__(ar, szobaszam)

        
class Szalloda:
    def __init__(self, nev, szobak, foglalasok):
        self.nev = nev
        self.szobak = szobak
        self.foglalasok = foglalasok

    def foglal(self, szoba, datum):
        self.foglalasok.append(Foglalas(szoba))
        return szoba.ar

    def lemond(self, foglalas):

        pass

    def foglalasok_lista(self):
        return self.foglalasok


class Foglalas:
    def __init__(self, szoba):
        self.szoba = szoba


sz1 = EgyagyasSzoba('50000 Ft', 9, False)
sz2 = EgyagyasSzoba('96000 Ft', 17, True)
sz3 = KetagyasSzoba('30000 Ft', 15, 'Park')
sz4 = KetagyasSzoba('40000 Ft', 19, 'Tengerparti')

szalloda = Szalloda('Hotel Barcika ******', [sz1, sz2, sz3, sz4], [])

szalloda.foglal(sz1, '2023.12.12')
szalloda.foglal(sz3, '2023.12.16')

print(f'{szalloda.nev}')
print(f'1. foglalás')
print(f'2. lemondás')
print(f'3. listázás')
print(f'4. kilépés')
print(f'')

while True:
    try:
        menupont = int(input('Válassz a listából: '))

        if menupont == 1:
            try:
                szobaszam = int(input('Válassz szobát: '))

                for szoba in szalloda.szobak:
                    if szoba.szobaszam == szobaszam:
                        foglalas_datum = input('Dátum: ')
                        szalloda.foglal(szoba, foglalas_datum)
                        break
            except ValueError:
                print("A megadott érték nem szám")

        if menupont == 3:
            for foglalas in szalloda.foglalasok:
                print(foglalas.szoba)

        if menupont == 4:
            break
    except ValueError:
        print("A megadott érték nem szám")

