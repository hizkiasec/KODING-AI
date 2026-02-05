from abc import ABC, abstractmethod

# 1. Interface / Abstract Class (Blueprint)
class GameUnit(ABC):

    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass


# 2. Implementasi Class Konkret (Hero & Monster)
class Hero(GameUnit):

    def __init__(self, nama):
        self.nama = nama

    # Hero wajib bikin method serang
    def serang(self, target):
        print(f"Hero {self.nama} menebas {target}!")

    def info(self):
        print(f"Saya adalah Hero: {self.nama}")


class Monster(GameUnit):

    def __init__(self, jenis):
        self.jenis = jenis

    # Monster juga wajib bikin method serang
    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}!")

    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")


# -- Uji Coba --
# unit = GameUnit()  # ERROR! Tidak boleh membuat objek abstract class

h = Hero("Alucard")
m = Monster("Serigala")

h.info()
m.info()

h.serang("Serigala")
m.serang("Alucard")
