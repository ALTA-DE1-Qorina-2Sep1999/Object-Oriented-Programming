class Ongkos():
    def __init__ (self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat

    def volume_barang (self):
        return (round(self.panjang * self.lebar * self.tinggi))
    
    def ongkir(self):
        volume = self.volume_barang()
        if volume <= 50:
            return 5000
        elif volume > 50:
            return 
        berat_pembulatan = round(self.berat)
        bayar = berat_pembulatan * 5000
        if volume == 50 and berat_pembulatan == 1:
            return 5000
        elif volume > 50 and berat_pembulatan >= 1:
            return bayar
        else:
            return None

if __name__ == "__main__":
    volume = Ongkos(5, 2, 4, 1)
    print(f"Harga: Rp {volume.ongkir()}")