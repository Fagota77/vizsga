gyumolcsok = ['alma','körte','barack','szilva','eper']

gyumolcsok = sorted(gyumolcsok)

for gyumolcs in gyumolcsok:
    if gyumolcs.startswith('a'):
        print(gyumolcs)


def osszead(a, b):
    return a + b


class Kutya:
    def __init__(self, nev, kor, faj):
        self.nev = nev
        self.kor = kor
        self.faj = faj
