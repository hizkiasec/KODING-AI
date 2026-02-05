from abc import ABC, abstractmethod

class BarangElektronik(ABC):
    def __init__(self, nama, stok, harga_dasar):
        self.nama = nama
        self.__stok = stok
        self.__harga_dasar = harga_dasar

    # Getter stok
    def get_stok(self):
        return self.__stok

    # Getter harga dasar
    def get_harga_dasar(self):
        return self.__harga_dasar

    # Setter stok dengan validasi
    def tambah_stok(self, jumlah):
        if self.__stok + jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({self.__stok + jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {self.__stok} unit.")

    @abstractmethod
    def tampilkan_detail(self, jumlah):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass
