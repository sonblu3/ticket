petugas = input("Masukan Nama Petugas :")

print("-------------------- ARMADA SS --------------------")
print("---------------------------------------------------------")
print("| KODE TIKET | TUJUAN | HARGA |")
print("---------------------------------------------------------")
print("|JFG647 | PNK – STG | Rp. 300.000 |")
print("|KL3435 | PNK – MLW | Rp. 250.000 |")
print("|UYR899 | PNK – KPH | Rp. 400.000 |")
print("|EBY246 | PNK – SGU | Rp. 150.000 |")
print("---------------------------------------------------------")

nama_pelanggan = input("Masukan Nama Pelanggan: ")
harga_ticket = 0
tujuan = ""

masukan_kode = input("Masukan Kode Nya: ")
if masukan_kode == 'JFG647':
    harga_ticket = 300000
    tujuan = "PNK – STG"
    print("Harga nya itu Rp. 300.000")
elif masukan_kode == 'KL3435':
    harga_ticket == 250000
    tujuan = "PNK – MLW"
    print("Harga nya itu Rp.250.000")
elif masukan_kode == 'UYR899':
    harga_ticket == 400000
    tujuan = "PNK – KPH"
    print("Harga nya itu Rp.400.000")
elif masukan_kode == 'EBY246':
    harga_ticket == 150000
    tujuan = "PNK – SGU"
    print("Harga nya itu Rp.150.000")
else:
    print("Pilih Kode Yg Benar")
    exit()

if harga_ticket > 0:
    banyak_ticket = int(input("Masukan Banyak Ticket: "))
    total_harga = banyak_ticket * harga_ticket

diskon = 0
if total_harga >= 750000:
    diskon = 0.05
elif total_harga >= 500000:
    diskon = 0.02

total_diskon = total_harga * diskon
total_harga_setelah_diskon = total_harga - total_diskon

print(f"Total harga sebelum diskon: Rp. {total_harga}:,")
if diskon > 0:
    print(f"Diskon: {diskon * 100}% (Rp. {int(total_diskon):,})")
print(f"Total harga setelah diskon: Rp. {int(total_harga_setelah_diskon):,}")

bayar = int(input("Bayar: Rp. "))
kembalian = bayar - total_harga_setelah_diskon

if kembalian > 0:
    print(f"Total bayar : Rp. {bayar:,}")
    print(f"Kembalian nya adalah: Rp. {kembalian:,}")
else:
    print("Uang kamu kurang tolol, bayar lg anjg. ")

print("======================================")
print("STRUK TIKET")
print("======================================")

print(f" Nama Pelanggan :{nama_pelanggan}: ")
print(f"Tujuan {tujuan}")
print(f" Banyak Ticket: {banyak_ticket}: ")

print("-------------------------------------------------------------")
print(f" Total Harga: {total_harga_setelah_diskon: }")
print(f"Diskon nya adalah: {diskon: }")
print(f"Bayar: {bayar: }")
print(f"Kembalian: {kembalian: }")

print("-------------------------------------------------------------")
print(f"Petugas: {petugas}")

print("======================================")
print("TERIMA KASIH")
print("======================================")
