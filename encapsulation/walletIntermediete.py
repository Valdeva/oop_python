class Wallet:
    def __init__(self,nama,nomer,saldoAwal,pin):
        self.nama = nama
        self.nomer = nomer
        self.__saldo = saldoAwal if saldoAwal > 0 else 0
        self.__pin = pin
        self.__status = "aktif"

    # property saldo
    @property
    def saldo(self):
        return self.__saldo
    
    # getter status akun
    @property
    def status(self):
        return self.__status
    
    # controller akun
    # cek pin
    def _cek_pin(self, pin):
        return self.__pin == pin
    
    # blokir akun
    def blokir_akun(self):
        self.__status = "blokir"
        print("Akun telah diblokir")

    # aktifkan akun
    def aktifkan_akun(self):
        self.__status = "aktif"
        print("Akun telah diaktifkan")


    # method untuk menambah saldo
    def topup(self, jumlah):
        if self.__status != "aktif":
            print("Akun tidak aktif. Silakan aktifkan akun terlebih dahulu.")
            return
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Berhasil menambahkan saldo sebesar {jumlah}")
        else:
            print("Jumlah topup harus lebih dari 0")

    # method untuk mengurangi saldo
    def bayar(self, jumlah, pin):
        if self.__status != "aktif":
            print("Akun tidak aktif. Silakan aktifkan akun terlebih dahulu.")
            return
        if not self._cek_pin(pin):
            print("PIN salah. Transaksi dibatalkan.")
            return
        if jumlah <= 0:
            print("Jumlah pembayaran harus lebih dari 0")
        elif jumlah > self.__saldo:
            print("Saldo tidak mencukupi")
        else:
            self.__saldo -= jumlah
            print(f"Berhasil melakukan pembayaran sebesar {jumlah}")

    # method untuk menerima transfer
    def _terima_transfer(self, jumlah):
        self.__saldo += jumlah

    # method transfer saldo ke wallet lain
    def transfer(self, tujuan_wallet, jumlah, pin):
        if self.__status != "aktif":
            print("Akun tidak aktif. Silakan aktifkan akun terlebih dahulu.")
            return
        if tujuan_wallet.status != "aktif":
            print("Akun tujuan tidak aktif. Transfer dibatalkan.")
            return
        if not self._cek_pin(pin):
            print("PIN salah. Transaksi dibatalkan.")
            return
        if jumlah <= 0:
            print("Jumlah transfer harus lebih dari 0")
        elif jumlah > self.__saldo:
            print("Saldo tidak mencukupi")
        else:
            self.__saldo -= jumlah
            tujuan_wallet._terima_transfer(jumlah)
            print(f"Berhasil mentransfer saldo sebesar {jumlah} ke {tujuan_wallet.nama}")

    
# contoh penggunaan class
walletA = Wallet("Alice", "WA001", 5000, "1234")
walletB = Wallet("Bob", "WB001", 3000, "5678")
print(f"Saldo awal wallet A adalah {walletA.saldo}")
print(f"Saldo awal wallet B adalah {walletB.saldo}")
walletB.blokir_akun()
walletA.blokir_akun()
walletA.topup(2000)
walletA.aktifkan_akun()
walletA.topup(2000)
walletA.bayar(1000, "1234")
walletA.transfer(walletB, 5000, "1234")
walletB.aktifkan_akun()
walletA.transfer(walletB, 1500, "12")
walletA.transfer(walletB, 5000, "1234")
print(f"Saldo wallet A sekarang adalah {walletA.saldo}")
print(f"Saldo wallet B sekarang adalah {walletB.saldo}")
