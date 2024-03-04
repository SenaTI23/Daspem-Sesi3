hasilnilai = int(input("masukan hasil ujian :"))

if hasilnilai <=50:
	nilai = "E"
elif hasilnilai >=50 and hasilnilai <=60 :
	nilai = "D"
elif hasilnilai >=60 and hasilnilai <=70 :
	nilai = "C"
elif hasilnilai >=70 and hasilnilai <=80 :
	nilai = "B"
else :
	nilai = "A"


print("Nilai :",nilai)