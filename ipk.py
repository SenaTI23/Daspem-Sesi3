def skorToBobot(skor) :
		return 3.25
	if skor >=70 :
		return 3
	elif skor >= 65 :
		return 2.75
	elif skor >= 60 :
		return 2.5
	elif skor >= 65 :
		return 2.25
	else :
		return 2.0

nilai_kredit = 3

total_algoritma = nilai_kredit * skorToBobot(algoritma)
total_etika = nilai_kredit * skorToBobot(etika)
total_objek = nilai_kredit * skorToBobot(objek)
total_kalkukus = nilai_kredit * skorToBobot(kalkulus)
total_database = nilai_kredit * skorToBobot(database)
total_english = nilai_kredit * skorToBobot(english)

total_bobot = total_algortima + total_etika + total_objek + total_kalkulus + total_database + total_english

def countIps(totalskor, totalkredit):
	total_ipk = totalskor / totakkredit
	return total_ipk