import time
import random

# Tulis kode mu di bawah
print("PERMAINAN BATU GUNTING KERTAS")
SkorAnda = 0
SkorKomputer = 0
while True:
    pilihan = input("Masukkan pilihan kamu: (Batu, Gunting, Kertas) ")
    komputer = random.randint(1,3)
    if komputer == 1:
        komputer = "Batu"
    elif komputer == 2:
        komputer = "Gunting"
    else:
        komputer = "Kertas"
    time.sleep(3)
    print("Batu,")
    time.sleep(1)
    print("Gunting,")
    time.sleep(1)
    print("Kertas!")
    time.sleep(1)
    print("Kamu memilih",pilihan,"dan komputer memilih",komputer)
    if (pilihan == "Kertas" and komputer == "Batu") or (pilihan == "Gunting" and komputer == "Kertas" or (pilihan == "Batu" and komputer == "Gunting")):
        print("Kamu Menang!!!")
        SkorAnda = SkorAnda + 1
    elif pilihan == komputer:
        print("Kita Seri!!!")
    else:
        print("Kamu Kalah!!!")
        SkorKomputer = SkorKomputer + 1
    print("Skor Anda:",SkorAnda)
    print("Skor Komputer:",SkorKomputer)
    print("\n\n")
