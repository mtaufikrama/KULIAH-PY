nama = raw_input("Masukkan Nama : ")
npm = input("Masukkan NPM : ")
kelas = raw_input("Masukkan Kelas : ")
uu = input ("Masukkan Nilai UU : ")
uts = input ("Masukkan Nilai UTS : ")
nilai = (0.5*uu)+(0.5*uts)
print "=========================="

print "Nama",nama,"dengan NPM",npm,"dari Kelas",kelas
if nilai >= 91:
    print "Nilai Anda",nilai
    print "Anda dapat Grade A"
elif nilai >= 81:
    print "Nilai Anda",nilai
    print "Anda dapat Grade B"
elif nilai >= 71:
    print "Nilai Anda",nilai
    print "Anda dapat Grade C"
elif nilai >= 60:
    print "Nilai Anda",nilai
    print "Anda dapat Grade D"
else :
    print "Nilai Anda",nilai
    print "Anda dapat Grade E"
