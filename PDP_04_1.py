"""
==========================
NAMA        : DHEVAN MUHAMAD ANTHAREZA
NIM         : A11.2019.12293
KELOMPOK    : A11.4118
TANGGAL     : 07-10-2019
===========================
"""
import os,sys
def main():
    #kamus
    nilai = int(input("Masukan Nilai : "))
    #algorithm
    if nilai > 0:
        if nilai > 100:
            print("A")
        if nilai > 50 and nilai <= 100:
            print("B")
        else:
            print("C")
    else:
        if nilai > -100:
            print("D")
        else: 
            print("E")
if __name__ == '__main__':
    main()
