def gabungan():
    string = ""
bar = 1

x = input('Masukkan angka : ')
print ('\n')
while bar < x:
	kol = bar
	while kol > 1:
		string = string + '   '
		kol = kol - 1
	kiri = 0
	while kiri <= (x - bar):
		string = string + ' * '
		kiri = kiri + 1	
	kanan = kiri	
	while kanan > 1:
		string = string + " * "
		kanan = kanan - 1

	if (bar+1) <= x:
		string = string + "\n\n"
	bar = bar + 1

bar = x-1	
# Looping Baris
while bar >= 0:
	# Looping Kolom Spasi Kosong
	kol = bar
	while kol > 0:
		string = string + "   "
		kol = kol - 1
	# Looping Kolom Bintang Sisi Kiri	
	kiri = 1
	while kiri < (x - (bar-1)):
		string = string + " * "
		kiri = kiri + 1		
	# Looping Kolom Bintang Sisi Kanan
	kanan = 1
	while kanan < kiri -1:
		string = string + " * "
		kanan = kanan + 1	

	string = string + "\n\n"
	bar = bar - 1
print (string)
    menu()

def matematika():
    
    menu()
    
def keluar():
    kuar = input('Apakah Yakin Akan Keluar? [yes/no] : ')
    if kuar == "no" :
        menu()
    else
    exit
    
def menu():
    print '========= MENU ========='
    print '1. Pola Segitiga Gabungan'
    print '2. Matematika'
    print '3. Exit'
    print '========================'
    pil = input('Masukkan Pilihan Anda  : ')
    if pil==1:
        gabungan()
        menu()

    elif pil==2:
        matematika()
        menu()

    elif pil==3:
        keluar()

    else:
        print 'PILIHAN TIDAK TERSEDIA'
menu()
