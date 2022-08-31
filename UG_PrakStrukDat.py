#71210749 #31082022

print("Kalkulator")

import os
while(True):
     print("1. Penambahan")
     print("2. Pengurangan")
     print("3. Perkalian")
     print("4. Pembagian")
     pilihan=(input("Masukkan pilihan anda : "))

     if pilihan=="q" or pilihan=="Q":
          os.system("cls")
     else:
         x=int(input("Masukkan nilai pertama : "))
         y=int(input("Masukkan nilai kedua : "))
         if pilihan=="1":
            def penjumlahan(x,y):
                 print("Hasil penjumlahannya yaitu : ",(x+y))
            penjumlahan(x,y)
         elif pilihan=="2":
            def pengurangan(x,y):
                print("Hasil pengurangannya yaitu : ",(x-y))
            pengurangan(x,y)
         elif pilihan=="3":
            def perkalian(x,y):
                print("Hasil perkaliannya yaitu : ",(x*y))
            perkalian(x,y)
         elif pilihan=="4":
            def pembagian(x,y):
                print("Hasil pembagianya yaitu : ",(x/y))
            pembagian(x,y)
         elif pilihan=="q" or pilihan=="Q":
            os.system("cls")


