def kali():
    x = input('Masukkan Angka Pertama : ')
    y = input('Masukkan Angka Kedua   : ')
    z = x*y
    print 'Hasil Perkalian        :',z
    menu()

def bagi():
    x = input('Masukkan Angka Pertama : ')
    y = input('Masukkan Angka Kedua   : ')
    z = x/y
    print 'Hasil Pembagian        :',z
    menu()

def menu():
    print '========= MENU ========='
    print '1. Perkalian'
    print '2. Pembagian'
    print '3. Exit'
    print '========================'
    pil = input('Masukkan Pilihan Anda  : ')
    if pil==1:
        kali()
        menu()

    elif pil==2:
        bagi()
        menu()

    elif pil==3:
        exit()
        menu()

    else:
        print 'PILIHAN ANDA TIDAK TERSEDIA!!'
menu()
