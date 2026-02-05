from barang_elektronik import BarangElektronik

class Smartphone(BarangElektronik):
    def __init__(self, nama, stok, harga_dasar, kamera):
        super().__init__(nama, stok, harga_dasar)
        self.kamera = kamera

    def hitung_harga_total(self, jumlah):
        pajak = self.get_harga_dasar() * 0.05
        return (self.get_harga_dasar() + pajak) * jumlah

    def tampilkan_detail(self, jumlah):
        pajak = self.get_harga_dasar() * 0.05
        subtotal = self.hitung_harga_total(jumlah)

        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        print(f" Harga Dasar: Rp {self.get_harga_dasar():,} | Pajak(5%): Rp {int(pajak):,}")
        print(f" Beli: {jumlah} unit | Subtotal: Rp {int(subtotal):,}")
