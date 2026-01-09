class Akun:
    def __init__(self, nama,saldo):
        self.nama = nama
        self.saldo = saldo 

    def cek_saldo(self):
        return self.saldo
    
    def setor(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            print(f"Berhasil menyetor sejumlah {jumlah}")
        else:
            print("Jumlah setor harus lebih dari 0")

# inheritance class Tabungan dari class Akun
class Tabungan(Akun):
    def hitung_bunga(self, persentase):
        if persentase > 0:
            bunga = self.saldo * (persentase / 100)
            self.saldo += bunga
            print(f"Bunga sebesar {bunga} telah ditambahkan ke saldo")
        else:
            print("Persentase bunga harus lebih dari 0")

# contoh penggunaan class
tabungan_andi = Tabungan("Andi", 1000000)
print(f"Saldo awal Andi: {tabungan_andi.cek_saldo()}")
tabungan_andi.setor(500000)
tabungan_andi.hitung_bunga(5)