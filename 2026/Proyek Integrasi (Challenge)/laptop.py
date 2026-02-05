from barang_elektronik import BarangElektronik

class Laptop(BarangElektronik):
    def __init__(self, nama, stok, harga_dasar, processor):
        super().__init__(nama, stok, harga_dasar)
        self.processor = processor

    def hitung_harga_total(self, jumlah):
        pajak = self.get_harga_dasar() * 0.10
        return (self.get_harga_dasar() + pajak) * jumlah

    def tampilkan_detail(self, jumlah):
        pajak = self.get_harga_dasar() * 0.10
        subtotal = self.hitung_harga_total(jumlah)

        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")
        print(f" Harga Dasar: Rp {self.get_harga_dasar():,} | Pajak(10%): Rp {int(pajak):,}")
        print(f" Beli: {jumlah} unit | Subtotal: Rp {int(subtotal):,}")
