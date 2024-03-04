nama = input("Masukkan nama: ")
tempat_lahir = input("Masukkan tempat lahir: ")
tanggal_lahir = input("Masukkan tanggal lahir: ")
tahunlahir = int(input("Masukkan tahun lahir: "))
jeniskelamin = input("Masukkan jenis kelamin (Laki_laki/Perempuan): ")
nilaiinggris = int(input("Masukkan nilai Bahasa Inggris: "))
nilaimtk = int(input("Masukkan nilai Matematika: "))
nilaiindo = int(input("Masukkan nilai Bahasa Indonesia: "))

usia = 2024 - tahunlahir
ratarata = (nilaiinggris + nilaimtk + nilaiindo) / 3
if ratarata >=80 and jeniskelamin == "laki_laki":
	saranjurusan = "teknik informatika"
elif ratarata >=80 and jeniskelamin == "perempuan":
	saranjurusan = "sistem informasi"
else :
	saranjurusan = "dkv"


print("nama :",nama)
print("umur :",usia)
print("nilai rata rata :",ratarata)
print("penjurusan tepat :",saranjurusan)


	