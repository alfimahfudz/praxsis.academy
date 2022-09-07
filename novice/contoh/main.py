print("program kasir sederhana")

total1 = 0
jenis1 = ""
porsi = 0
gelas = 0

program = "jalan"

while program == "jalan":

	def fungsimakanan():
		global total1
		global porsi
		global jenis1
		print("~paket ramadhan~")
		print("1. sirup marjan - Rp15000")
		print("2. kurma - Rp18000")
		print("3. khong guan - Rp49000")
		print("4. tango - 21000")
		nomor = int(input("Masukan Pilihan: "))
		satuan = int(input("Berapa satuan: "))

		if nomor == 1:
			total1 = satuan * 15000
			print(satuan, " porsi Nasi Goreng Telur = Rp", total1)
			jenis1 = ("Nasi Goreng")
		elif nomor == 2:
			total1 = satuan * 8000
			print(satuan, " porsi Soto = Rp", total1)
			jenis1 = ("Soto")
		elif nomor == 3:
			total1 = satuan * 9000
			print(satuan, " porsi Mie Ayam = Rp", total1)
			jenis1 = ("Mie Ayam")
		elif nomor == 4:
			total1 = satuan * 11000
			print(satuan, " porsi bakso = Rp", total1)
			jenis1 = ("bakso")
		else:
			print("Pilihan tidak ada, silahkan masukan")
	fungsimakanan()

	total2 = 0
	jenis2 = ""


	def fungsiminuman():
		global total2
		global jenis2
		global gelas
		print("~Menu Minuman~")
		print("1. Es teh - Rp2000")
		print("2. Es jeruk - Rp3500")
		print("3. Es kopi - Rp4000")
		nomor = int(input("Masukan Pilihan: "))
		gelas = int(input("Berapa Gelas: "))
		
		if nomor == 1:
			total2 = gelas * 2000
			print(gelas, " Es Teh = Rp", total2)
			jenis2 = (" Gelas Es Teh")
		elif nomor == 2:
			total2 = gelas * 3500
			print(gelas, " Gelas Es Jeruk = Rp", total2)
			jenis2 = ("Es Jeruk")
		elif nomor == 3:
			total2 = gelas * 4000
			print(gelas, " Gelas Es Kopi = Rp", total2)
			jenis2 = ("Es Kopi")
		else:
			print("Pilihan tidak ada, silahkan masukan lagi!!")
			fungsiminuman()

	fungsiminuman()

	totalsemua = 0
	totalsemua = total1 + total2
	print("Total harus Dibayar: Rp", totalsemua)
	uang = int(input("Uang Tunai Pembeli: Rp."))
	kembalian = int(uang - totalsemua)
	print("Kembalian :", kembalian)

	print("=======================================")
	print("==========S T R U K   B E L I==========")
	print("=======================================")
	print(" Beli       : ", porsi, jenis1, "-", total1)
	print("              ", gelas, jenis2, "-", total2)
	print(" Tagihan    : Rp.", totalsemua)
	print(" Uang       : Rp.", uang)
	print(" Kembalian  : Rp.", kembalian)
	print("=======================================") 

	beli = str(input("Apakah anda akan membeli lagi? [yes/no] : "))

	if beli == "yes":
		pass
	elif beli == "no":
		break