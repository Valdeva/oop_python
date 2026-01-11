from abc import ABC, abstractmethod

class Wallet(ABC):
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
        return"Akun telah diblokir"

    # aktifkan akun
    def aktifkan_akun(self):
        self.__status = "aktif"
        return "Akun telah diaktifkan"


    # method untuk menambah saldo
    def topup(self, jumlah):
        if self.__status != "aktif":
            return "Akun tidak aktif. Silakan aktifkan akun terlebih dahulu."
        if jumlah > 0:
            self.__saldo += jumlah
            return f"Berhasil menambahkan saldo sebesar {jumlah}"
        else:
            return "Jumlah topup harus lebih dari 0"

    # method untuk mengurangi saldo
    def bayar(self, jumlah, pin):
        if self.__status != "aktif":
            return"Akun tidak aktif. Silakan aktifkan akun terlebih dahulu."
        if not self._cek_pin(pin):
            return "PIN salah. Transaksi dibatalkan."
        if jumlah <= 0:
            return"Jumlah pembayaran harus lebih dari 0"
        elif jumlah > self.__saldo:
            return "Saldo tidak mencukupi"
        else:
            self.__saldo -= jumlah
            return f"Berhasil melakukan pembayaran sebesar {jumlah}"

    # hitung fee transfer dan cashback menggunakan abstrak method
    @abstractmethod
    def _hitung_fee(self):
        pass
    @abstractmethod
    def _hitung_cashback(self):
        pass
    
    # method untuk menerima transfer
    def _terima_transfer(self, jumlah):
        self.__saldo += jumlah

    # method transfer saldo ke wallet lain
    def transfer(self, tujuan_wallet, jumlah, pin):
        if jumlah <= 0:
            return "Jumlah transfer harus lebih dari 0"

        if self.__status != "aktif":
            return "Akun tidak aktif"

        if tujuan_wallet.status != "aktif":
            return "Akun tujuan tidak aktif"

        if not self._cek_pin(pin):
            return "PIN salah"

        fee = self._hitung_fee()
        cashback = self._hitung_cashback()
        total_transfer = max(jumlah + fee - cashback, jumlah)

        if total_transfer > self.__saldo:
            return "Saldo tidak mencukupi"

        self.__saldo -= total_transfer
        tujuan_wallet._terima_transfer(jumlah)

        return f"Transfer {jumlah} ke {tujuan_wallet.nama} berhasil"


# class inheritence abstraction Wallet
class BasicWallet(Wallet):
    def __init__(self, nama, nomer, saldoAwal, pin):
        super().__init__(nama, nomer, saldoAwal, pin)

    def _hitung_fee(self):
        return 500  # biaya transfer untuk BasicWallet
    def _hitung_cashback(self):
        return 0  # cashback untuk BasicWallet
    
    

class PremiumWallet(Wallet):
    def __init__(self, nama, nomer, saldoAwal, pin):
        super().__init__(nama, nomer, saldoAwal, pin)

    def _hitung_fee(self):
        return 0  # biaya transfer untuk PremiumWallet    

    def _hitung_cashback(self):
        return 10000 # cashback untuk PremiumWallet setiap transfer


    
# membuat wallet
wallet1 = BasicWallet("Alice", "08123456789", 10000, "1234")
wallet2 = PremiumWallet("Bob", "08987654321", 5000, "5678")

print("=== SALDO AWAL ===")
print(f"{wallet1.nama}: {wallet1.saldo}")
print(f"{wallet2.nama}: {wallet2.saldo}")

print("\n=== COBA TRANSAKSI SAAT AKUN DIBLOKIR ===")
print(wallet1.blokir_akun())
print(wallet1.topup(5000))  # gagal karena diblokir

print("\n=== AKTIFKAN & TOPUP ===")
print(wallet1.aktifkan_akun())
print(wallet1.topup(5000))

print("\n=== COBA BAYAR DENGAN PIN SALAH ===")
print(wallet1.bayar(3000, "0000"))

print("\n=== BAYAR DENGAN PIN BENAR ===")
print(wallet1.bayar(3000, "1234"))

print("\n=== COBA TRANSFER KE AKUN TUJUAN YANG DIBLOKIR ===")
print(wallet2.blokir_akun())
print(wallet1.transfer(wallet2, 2000, "1234"))

print("\n=== AKTIFKAN AKUN TUJUAN & TRANSFER ===")
print(wallet2.aktifkan_akun())
print(wallet1.transfer(wallet2, 2000, "1234"))

print("\n=== SALDO AKHIR ===")
print(f"{wallet1.nama}: {wallet1.saldo}")
print(f"{wallet2.nama}: {wallet2.saldo}")

