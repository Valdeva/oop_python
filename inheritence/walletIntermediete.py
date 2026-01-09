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

    # hitung fee transfer dan cashback
    def _fee_transfer(self):
        return 0  # default tidak ada biaya transfer
    def _cashback(self):
        return 0  # default tidak ada cashback
    
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
        
        fee = self._fee_transfer()
        cashback = self._cashback()
        total_transfer = max(jumlah + fee - cashback, jumlah)


        if jumlah <= 0:
            print("Jumlah transfer harus lebih dari 0")
        elif total_transfer> self.__saldo:
            print("Saldo tidak mencukupi")
        else:
            self.__saldo -= total_transfer
            tujuan_wallet._terima_transfer(jumlah)
            print(f"Berhasil mentransfer saldo sebesar {jumlah} ke {tujuan_wallet.nama}")

# class inheritence
class BasicWallet(Wallet):
    def __init__(self, nama, nomer, saldoAwal, pin):
        super().__init__(nama, nomer, saldoAwal, pin)

    def _fee_transfer(self):
        return 500  # biaya transfer untuk BasicWallet
    
    
        
class PremiumWallet(Wallet):
    def __init__(self, nama, nomer, saldoAwal, pin):
        super().__init__(nama, nomer, saldoAwal, pin)

    def _cashback(self):
        return 10000 # cashback untuk PremiumWallet setiap transfer


    
# membuat wallet
wallet1 = BasicWallet("Alice", "08123456789", 10000, "1234")
wallet2 = PremiumWallet("Bob", "08987654321", 5000, "5678")

print("=== SALDO AWAL ===")
print(f"{wallet1.nama}: {wallet1.saldo}")
print(f"{wallet2.nama}: {wallet2.saldo}")

print("\n=== COBA TRANSAKSI SAAT AKUN DIBLOKIR ===")
wallet1.blokir_akun()
wallet1.topup(5000)  # gagal karena diblokir

print("\n=== AKTIFKAN & TOPUP ===")
wallet1.aktifkan_akun()
wallet1.topup(5000)

print("\n=== COBA BAYAR DENGAN PIN SALAH ===")
wallet1.bayar(3000, "0000")

print("\n=== BAYAR DENGAN PIN BENAR ===")
wallet1.bayar(3000, "1234")

print("\n=== COBA TRANSFER KE AKUN TUJUAN YANG DIBLOKIR ===")
wallet2.blokir_akun()
wallet1.transfer(wallet2, 2000, "1234")

print("\n=== AKTIFKAN AKUN TUJUAN & TRANSFER ===")
wallet2.aktifkan_akun()
wallet1.transfer(wallet2, 2000, "1234")

print("\n=== SALDO AKHIR ===")
print(f"{wallet1.nama}: {wallet1.saldo}")
print(f"{wallet2.nama}: {wallet2.saldo}")

