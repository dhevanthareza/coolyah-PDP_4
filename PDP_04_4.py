"""
==========================
NAMA        : DHEVAN MUHAMAD ANTHAREZA
NIM         : A11.2019.12293
KELOMPOK    : A11.4118
TANGGAL     : 07-10-2019
===========================
"""
suhuFah = float(input("Masukan suhu dalam fahrenheit : "))
celcius = 5/9 * (suhuFah-32)
if(celcius >= 100):
    print("Mendidih")
elif(celcius <= 0):
    print("mebeku")
else:
    print("biasa")