# Kirjoita luokka nimeltä ”auto”. Luokasta tulee löytyä muuttujat merkki, väri, paino, vuosimalli, kilometrit,
# hinta. Lisää muuttujien merkki, väri, paino, vuosimalli ja kilometrit arvot itse. Voit keksiä muuttujien arvot
# itse. Autot tulee lisätä listaan. 

class auto:
    def __init__(self):
        self.autot = "Volvo","Toyota","Bmw"
        self.väri = "Pinkki", "Sininen", "Musta"
        self.paino = [1000, 1200, 2000]
        self.vuosimalli = [1980, 2006, 1995]
        self.kilometrit = [20000, 122000, 1500000]
        self.hinta = []
    
    def lasku(self):
        self.ikä = 2022 - self.vuosimalli[i]
        self.ikäkerroin = 1 + (1 / self.ikä) * 100
        self.kmkerroin = 1 + (1 / self.kilometrit[i]) * 10000 * 100
        self.hintalaskuri = (self.ikäkerroin + self.kmkerroin) * 1000       
        self.hinta.append(round(self.hintalaskuri))

auto = auto()

for i in range(len(auto.autot)):
    auto.lasku()
    print("Merkki:",auto.autot[i],"Väri:",auto.väri[i],"Paino:",str(auto.paino[i])+"kg "+"Vuosimalli:",auto.vuosimalli[i],"Kilometrit:",str(auto.kilometrit[i])+"km","Hinta:",auto.hinta[i])
