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
    score = int(input("Masukan Score: "))
    stars = 0
    if score >= 80:
        stars = 3
    elif score > 45 and score < 80:
        stars = 2
    else:
        stars = 1
    print("Selamat anda mendapatkan bintang", stars)
if __name__ == '__main__':
    main()