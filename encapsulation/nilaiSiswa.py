class Siswa:
    def __init__(self,nama,nim,nilaiAwal):
        self.nama = nama
        self.nim = nim
        self.__nilai = nilaiAwal

    # getter nilai
    def get_nilai(self):
        return self.__nilai
    
    # setter nilai
    def set_nilai(self, nilai_baru):
        if 0 <= nilai_baru <= 100:
            self.__nilai = nilai_baru
        else:
            print("nilai harus antara 0 sampai 100")

    
    # cek kelulusan
    def cek_lulus(self):
        if self.__nilai < 60:
            print(f"nilai anda {self.__nilai}, belum lulus")
        elif self.__nilai >= 60 and self.__nilai < 80:
            print(f"nilai anda {self.__nilai}, anda mengikuti ujian ulang")
        elif self.__nilai >= 80 and self.__nilai <= 100:
            print(f"nilai anda {self.__nilai}, anda lulus")
        else:
            print("nilai tidak sesuai")


# cntoh percobaan 

andi = Siswa("Andi", "S001", 75)
budi = Siswa("Budi", "S002", 45)
print(f"nilai awal andi adalah {andi.get_nilai()}")
print(f"nilai awal budi adalah {budi.get_nilai()}")
andi.set_nilai(90)
budi.set_nilai(88)
print(f"nilai andi sekarang adalah {andi.get_nilai()}")
print(f"nilai budi sekarang adalah {budi.get_nilai()}")
andi.cek_lulus()
budi.cek_lulus()