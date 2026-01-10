class Kendaraan:
    def hitung_pajak(self):
        raise NotImplementedError("Method harus dioverride")

class Mobil(Kendaraan):
    def hitung_pajak(self):
        pajak = 100
        return f"Pajak Mobil: {pajak} IDR"
class Motor(Kendaraan):
    def hitung_pajak(self):
        pajak = 50
        return f"Pajak Motor: {pajak} IDR"

avaza = Mobil()
nmax = Motor()
print(avaza.hitung_pajak())  # Output: Pajak Mobil: 100 IDR
print(nmax.hitung_pajak())   # Output: Pajak Motor: 50 IDR