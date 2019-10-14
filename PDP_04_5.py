"""
==========================
NAMA        : DHEVAN MUHAMAD ANTHAREZA
NIM         : A11.2019.12293
KELOMPOK    : A11.4118
TANGGAL     : 07-10-2019
===========================
"""
sangu = int(input("Masukan Sangu : "))
if sangu < 1200000: print("input tidak valid")
else: 
    sisa = sangu - (1200000)
    if(sisa < 500000):
        print("gak bisa konser")
    elif(sisa < 1000000):
        print("ikut konser biasa")
    else:
        print("ikut konser vip")