class Barang:
    def __init__(self,nama_barang,kode_barang,stok_awal):
        self.nama = nama_barang
        self.kode = kode_barang
        self.__stok = stok_awal if stok_awal >= 0 else 0


    # getter stok barang
    def cek_stok(self):
        return self.__stok
    
    # setter stok barang
    def tambah_stok(self,jumlah):
        if jumlah > 0 :
            self.__stok += jumlah
            print(f"berhasil menambah kan stok sejumlah {jumlah}")
        else :
            print (" jumlah barang harus lebih dari 0")

    def kurangi_stok(self, jumlah):
        if jumlah <= 0:
            print("jumlah barang harus lebih dari 0")
        elif jumlah > self.__stok:
            print("stok tidak mencukupi")
        else:
            self.__stok -= jumlah
            print(f"berhasil mengurangi stok sejumlah {jumlah}")


# contoh penggunaan class
beras = Barang("Beras", "BR001", 100)
gula = Barang("Gula", "GL001", 150)
print(f"stok awal beras adalah {beras.cek_stok()}")
print(f"stok awal gula adalah {gula.cek_stok()}")
beras.tambah_stok(1000)
gula.kurangi_stok(50)
print(f"stok beras sekarang adalah {beras.cek_stok()}")
print(f"stok gula sekarang adalah {gula.cek_stok()}")