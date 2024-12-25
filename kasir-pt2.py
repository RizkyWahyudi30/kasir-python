menu = {
    "Ayam goreng"           : 8000,
    "Nasi bakar cumi-cumi"  : 13000,
    "Nasi bakar ayam suir"  : 13000,
    "Nasi bakar teri pedas" : 11000,
    "Es teh manis"          : 4000,
    "Es teh tawar"          : 3000,
    "Sayur lodeh"           : 5000, 
}
print("=============== Daftar Menu Makanan Warung ===============")
# pengulangan
for i, (nama, harga) in enumerate(menu.items(), start=1):
    print(f"Daftar menu {i}, {nama} \t Harga : {harga}")
print("Pembelian diatas Rp20.000,- mendapat potongan 10%")
print("======================================================")

# variable untuk menyimpan pesanan
pesanan = {}
# input pesanan
while True:
    beli = input("Pilih menu (ketik 'selesai' jika selesai) : ")
    if beli.lower() == "selesai":
        break
    
    if beli not in menu:
        print("Menu yang tidak ditemukan, silahkan pilih lagi.")
        continue

    jumlah = int(input(f"Jumlah pesanan untuk {beli} : "))
    if beli in pesanan:
        pesanan[beli] += jumlah
    else:
        pesanan[beli] = jumlah

# perhitungan total harga
bayar = sum(jumlah * menu[item] for item, jumlah in pesanan.items())

# pengkondisian diskon
if bayar > 20000:
    diskon = bayar * 10/100
    total = bayar - diskon
else :
    total = bayar

# hasil
print("=============== Total Pembelian ===============")
for item, jumlah in pesanan.items():
    print(f'{item} (x{jumlah}) - Rp{jumlah * menu[item]}')
print(f"Total harga : Rp{bayar}")
print(f"Diskon : Rp{diskon}")
print(f"Total harga yang harus dibayar : Rp{total}")