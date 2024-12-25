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
for i in menu:
    print("Daftar menu : ", i, "\t Harga : ", menu[i])
print("Pembelian diatas Rp20.000,- mendapatkan potongan 10%")
print("==========================================================")
beli = input("Pilih menu : ")
jumlah = int(input("Jumlah pesanan : "))
bayar = jumlah * menu[beli]

# pengkondisian
if bayar > 20000:
    diskon = bayar * 10/100
    total = bayar - diskon
else :
    total = bayar

print("=============== Total Pembelian ===============")
print("Menu yang dipesan            : ", beli)
print("Jumlah yang dipesan          : ", jumlah)
print("Total harga                  : ", bayar)
print("Total yang harus dibayar     : ", total)
