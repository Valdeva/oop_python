class BankAccount:
    def __init__(self,nama,saldoAwal):
        self.nama = nama
        self.__saldo = saldoAwal

    # getter saldo
    def get_saldo(self):
        return self.__saldo
    
    #setter saldo
    def setor_saldo(self,jumlah):
        if jumlah > 0 :
            self.__saldo += jumlah 
            print(f"saldo anda sekarang berjumlah {self.__saldo}")
        else:
            print("jumlah harus lebih dari 0")

    def tarik_saldo(self,jumlah):
        if jumlah > self.__saldo :
            print("saldo tidak mencukupi")
        elif jumlah <= 0:
            print(" jumlah yang ditarik harus lebih dari 0")
        else:
            self.__saldo -= jumlah
            print(f"saldo anda sekarang berjumlah {self.__saldo}")

    
# contoh penggunaan
accUdin = BankAccount("udin",1000)
print(f"saldo awal anda {accUdin.get_saldo()}")
accUdin.setor_saldo(500)
accUdin.tarik_saldo(700)
