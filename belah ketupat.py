batas = input("Masukkan Jumlah Perulangan : ")
for i in range (1, batas+1, 1):
    spasi = " " * (batas-i)
    bintang = "* " * i
    print spasi, bintang

for i in range (batas-1, 0, -1):
    spasi = " " * (batas-i)
    bintang = "* " * i
    print spasi, bintang
