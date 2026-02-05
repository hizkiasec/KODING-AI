class Hero:

    # Constructor
    def __init__(self, name, hp_awal, attack_power):
        self.name = name
        self.attack_power = attack_power
        
        # HP Private
        self.__hp = hp_awal

    # GETTER: melihat HP
    def get_hp(self):
        return self.__hp

    # SETTER: mengubah HP dengan validasi
    def set_hp(self, nilai_baru):

        if nilai_baru < 0:
            self.__hp = 0     # HP tidak boleh negatif
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    # Menampilkan info hero
    def info(self):
        print(f"Hero: {self.name} | HP: {self.get_hp()} | Power: {self.attack_power}")

    # Method menyerang
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    # Method menerima damage
    def diserang(self, damage):
        sisa = self.get_hp() - damage
        self.set_hp(sisa)
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.get_hp()}")


# CLASS MAGE: pewarisan dari Hero
class Mage(Hero):

    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)
        self.mana = mana

    def info(self):
        print(f"{self.name} [Mage] | HP: {self.get_hp()} | Mana: {self.mana}")

    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)
        else:
            print(f"{self.name} gagal skill! Mana tidak cukup.")


# --- Main Program ---
hero1 = Hero("Layla", 100, 15)
hero2 = Hero("Zilong", 120, 20)

hero1.info()
hero2.info()

print("\n--- Pertarungan Dimulai ---\n")
hero1.serang(hero2)
hero2.serang(hero1)

print("\n--- Update Class Hero ---")

eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)

eudora.info()
eudora.serang(balmond)
eudora.skill_fireball(balmond)

print(f"Mencoba akses paksa: {hero1._Hero__hp}")
