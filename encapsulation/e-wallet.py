class Wallet:
    def __init__(self,nama,no_rekening,saldoAwal):
        self.nama = nama
        self.no_rekening = no_rekening
        self.__saldo = saldoAwal if saldoAwal >= 0 else 0

    
    # getter saldo
    def get_saldo(self):
        return self.__saldo
    
    # setter saldo 
    def top_up(self,jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"top up berhasil,saldo anda {self.__saldo}")
        else:
            print("jumlah top up harus lebih dari 0")

    def bayar(self,jumlah):
        if jumlah > self.__saldo:
            print(f"anda harus membayar {jumlah},saldo anda tidak cukup")
        elif jumlah <=0:
            print("jumlah harus lebih dari 0")
        else:
            self.__saldo -= jumlah
            print(f"pembayaran berhasil, saldo anda {self.__saldo}")
        
    def transfer (self,akun_tujuan,jumlah):
        if jumlah > self.__saldo:
            print(f"anda harus membayar {jumlah},saldo anda tidak cukup")
        elif jumlah <=0:
            print("jumlah harus lebih dari 0")
        else:
            self.__saldo -= jumlah
            akun_tujuan.__saldo += jumlah
            print(f"transfer berhasil,anda transfer sebesar {jumlah}")

    
# contoh penggunaan
udin = Wallet("udin",111,10000)
pardi = Wallet("pardi",222,20000)
print(f"saldo awal udin {udin.get_saldo()}")
print(f"saldo awal pardi {pardi.get_saldo()}")
udin.top_up(5000)
udin.bayar(1000)
udin.transfer(pardi,2000)
print(f"saldo udin sekaran {udin.get_saldo()}")
print(f"saldo pardi sekarang {pardi.get_saldo()}")