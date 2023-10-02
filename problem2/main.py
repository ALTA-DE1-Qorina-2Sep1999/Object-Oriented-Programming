class Kubus():
    def __init__(self, sisi):
        self.sisi = sisi
    
    def calculate_volume(self):
        return (round(self.sisi * self.sisi * self.sisi))

class Balok():
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
    
    def calculate_volume(self):
        return (round(self.panjang * self.lebar * self.tinggi))
    
class Tabung():
    def __init__(self, jari_jari, tinggi):
        self.phi = 3.14
        self.jari_jari = jari_jari
        self.tinggi = tinggi

    def calculate_volume(self):
        return int(round(self.phi * pow(self.jari_jari, 2) * self.tinggi))
    
if __name__ == "__main__":
    kubus = Kubus(10)
    balok = Balok(3, 6, 10)
    tabung = Tabung(7, 10)
    
    print("Volume")
    print("Kubus:", kubus.calculate_volume())
    print("Balok:", balok.calculate_volume())
    print("Tabung:", tabung.calculate_volume())