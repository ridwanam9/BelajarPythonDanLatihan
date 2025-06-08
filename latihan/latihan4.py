class Kalkulator:
    def tambah(self, a, b):
        print(f"{a} + {b} = {a + b}")

    def kurang(self, a, b):   
        print(f"{a} - {b} = {a - b}")
        
    def kali(self, a, b):
        print(f"{a} * {b} = {a * b}")     

    def bagi(self, a, b):
        if b != 0:
            print(f"{a} / {b} = {a / b}")
        else:
            print("Tidak bisa dibagi dengan 0")


kalkulator = Kalkulator()
kalkulator.tambah(3, 4)
kalkulator.kurang(3, 4)
kalkulator.kali(3, 4)
kalkulator.bagi(3, 4)
kalkulator.bagi(3, 0)