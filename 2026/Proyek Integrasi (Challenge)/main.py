from laptop import Laptop
from smartphone import Smartphone
from transaksi import proses_transaksi

print("--- SETUP DATA ---")

# Buat produk
laptop1 = Laptop("ROG Zephyrus", 0, 20000000, "Ryzen 9")
hp1 = Smartphone("iPhone 13", 0, 15000000, "12MP")

# Update stok
laptop1.tambah_stok(10)
hp1.tambah_stok(-5)  # ditolak
hp1.tambah_stok(20)

# Keranjang belanja user
keranjang = [
    (laptop1, 2),   # beli 2 Laptop
    (hp1, 1)        # beli 1 Smartphone
]

# Cetak transaksi
proses_transaksi(keranjang)
