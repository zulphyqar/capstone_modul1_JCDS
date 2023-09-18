from tabulate import tabulate
from colorama import Fore, Back, Style, init
init(autoreset=True)  # agar tereset warna setelah diganti


# ===========================================================================================================================
# Data Utama Rental Mobil
database_mobil = [
    {'kode_mobil': 101, 'brand':'toyota', 'tipe':'avanza', 
     'jenis':'mvp', 'tahun':'2020', 'harga_sewa': 350000, 
     'kapasitas':'7', 'transmisi':'AT' },

    {'kode_mobil': 102, 'brand':'honda', 'tipe':'crv', 
     'jenis':'suv', 'tahun':'2018', 'harga_sewa': 650000, 
     'kapasitas':'7', 'transmisi':'AT' },

    {'kode_mobil': 103, 'brand':'mitsubishi', 'tipe':'xpander', 
     'jenis':'mvp', 'tahun':'2019', 'harga_sewa': 350000, 
     'kapasitas':'7', 'transmisi':'MT' },

    {'kode_mobil': 104, 'brand':'daihatsu', 'tipe':'sirion',
     'jenis':'hatchback', 'tahun':'2021', 'harga_sewa': 250000, 
     'kapasitas':'5', 'transmisi':'MT' },

    {'kode_mobil': 105, 'brand':'toyota', 'tipe':'fortuner',
     'jenis':'suv', 'tahun':'2023', 'harga_sewa': 700000,
     'kapasitas':'7', 'transmisi':'AT' },

    {'kode_mobil': 106, 'brand':'mazda', 'tipe':'3',
     'jenis':'hatchback', 'tahun':'2022', 'harga_sewa': 700000,
     'kapasitas':'5', 'transmisi':'AT' },

    {'kode_mobil': 107, 'brand':'honda', 'tipe':'city', 
     'jenis':'sedan', 'tahun':'2018', 'harga_sewa':450000, 
     'kapasitas':'5', 'transmisi':'MT' }
]

# ===========================================================================================================================
# (1) FUNGSI UNTUK MENAMPILKAN MENU MOBIL
# ---------------------------------------------------------------------------------------------------------------------------
# menu untuk menampilkan mobil berdasarkan kondisi tertentu
def menu_lihat_mobil():
    while True:
        print('''
-----------------------------------------
|        Menu tampilan mobil            |
|---------------------------------------|
| 1. Lihat Semua Mobil                  |
| 2. Lihat Mobil Secara Spesifik        |
| 3. Lihat Mobil per-Values             |
| 4. Urutkan Mobil Berdasarkan Values   |
| 5. Kembali ke menu utama              |
-----------------------------------------
                ''')                    
        pilihan_menu = input("Pilih menu (1-5): ")

        if pilihan_menu.isdigit() == False :
            print('Input harus berupa angka')
        else : 
            if pilihan_menu == '1':
                lihat_semua_mobil()
        
            elif pilihan_menu == '2' :
                lihat_mobil_tertentu()
            
            elif pilihan_menu == '3':
                if len(database_mobil) == 0:
                    print(Fore.YELLOW + Style.BRIGHT + "\nDaftar mobil kosong.\n")
                elif len(database_mobil) != 0 :                       
                    menu_lihat_mobil_values()
            
            elif pilihan_menu == '4':
                if len(database_mobil) == 0:
                    print(Fore.YELLOW + Style.BRIGHT + "\nDaftar mobil kosong.\n")
                elif len(database_mobil) != 0 :                
                    sort_mobil()

            elif pilihan_menu == '5':
                kembali_menu_utama()
            
            else :
                print('Masukkan input dengan benar\n')
                
# ---------------------------------------------------------------------------------------------------------------------------
# (1.1) fungsi untuk menampilkan semua mobil
def lihat_semua_mobil():
    if len(database_mobil) == 0:
        print(Fore.YELLOW + Style.BRIGHT + "\nDaftar mobil kosong.\n")
    elif len(database_mobil) != 0 :
        print("=============Daftar Mobil===================")
        print(tabulate(database_mobil, headers='keys', tablefmt='grid'))

# ---------------------------------------------------------------------------------------------------------------------------
# (1.2) Fungsi Menampilkan mobil tertentu
def lihat_mobil_tertentu():
    if len(database_mobil) == 0:
        print(Fore.YELLOW + Style.BRIGHT + "\nDaftar mobil kosong.\n")
    elif len(database_mobil) != 0 :
        kode_mobil_tertentu = input('Masukkan kode mobil: ')    
        if kode_mobil_tertentu.isdigit() == False:
            print(Fore.RED + Style.BRIGHT + '\ninput harus berupa angka')
        else :
            kode_mobil_tertentu = int(kode_mobil_tertentu)
            for mobil in database_mobil:
                if int(kode_mobil_tertentu) == int(mobil['kode_mobil']):
                    print(f"\nKode Mobil: {mobil['kode_mobil']}") 
                    print(f"Brand: {mobil['brand']}") 
                    print(f"Tipe: {mobil['tipe']}") 
                    print(f"Jenis: {mobil['jenis']}") 
                    print(f"Tahun: {mobil['tahun']}")
                    print(f"Harga Sewa: {mobil['harga_sewa']}")
                    print(f"Kapasitas: {mobil['kapasitas']}")
                    print(f"Transmisi: {mobil['transmisi']}") 
            if int(kode_mobil_tertentu) > mobil['kode_mobil'] or int(kode_mobil_tertentu) < 101:
                print('''
    Kode yang Anda masukkan tidak ada dalam rental mobil kami. 
    Mungkin suatu saat kami akan menggunakan kode tersebut!
                    ''')

# ---------------------------------------------------------------------------------------------------------------------------             
# (1.3) Fungsi Menu untuk menampilkan mobil berdasarkan Values
def menu_lihat_mobil_values():
    while True:
        print('''
-----------------------------------------
|       Lihat Mobil per-Values          |
|---------------------------------------|
| 1. Lihat Mobil Berdasarkan Brand      |
| 2. Lihat Mobil Berdasarkan Transmisi  |
| 3. Lihat Mobil Berdasarkan Jenis      |
| 4. Lihat Mobil Berdasarkan Kapasitas  |
| 5. Kembali ke Menu Lihat Mobil        |
-----------------------------------------
                ''')                    
        pilihan_menu = input("Pilih menu (1-5): ")

        if pilihan_menu.isdigit() == False :
            print(Fore.RED + Style.BRIGHT + 'Input harus berupa angka')
        else : 
            if pilihan_menu == '1':
                brand = input("Masukkan brand mobil yang ingin dicari: ")
                hasil_filter = filter_mobil_berdasarkan_brand(brand)
                output_kondisi_mobil(hasil_filter)

            elif pilihan_menu == '2':
                transmisi = input("Masukkan jenis transmisi (AT/MT): ")
                hasil_filter = filter_mobil_berdasarkan_transmisi(transmisi)
                output_kondisi_mobil(hasil_filter)

            elif pilihan_menu == '3':
                jenis = input("Masukkan jenis mobil yang ingin dicari: ")
                hasil_filter = filter_mobil_berdasarkan_jenis(jenis)
                output_kondisi_mobil(hasil_filter)

            elif pilihan_menu == '4':
                kapasitas = input("Masukkan kapasitas mobil (5/7): ")
                hasil_filter = filter_mobil_berdasarkan_kapasitas(kapasitas)
                output_kondisi_mobil(hasil_filter)

            elif pilihan_menu == '5':
                menu_lihat_mobil()
            
            else:
                print('Masukkan input dengan benar')

# ---------------------------------------------------------------------------------------------------------------------------             
# (1.3.1) Fungsi untuk menampilkan mobil berdasarkan brand
def filter_mobil_berdasarkan_brand(brand):
    hasil_filter = []
    for mobil in database_mobil:
        if mobil['brand'].lower() == brand.lower():
            hasil_filter.append(mobil)
    return hasil_filter

# ---------------------------------------------------------------------------------------------------------------------------
# (1.3.2) Fungsi untuk menampilkan mobil berdasarkan transmisi
def filter_mobil_berdasarkan_transmisi(transmisi):
    hasil_filter = []
    for mobil in database_mobil:
        if mobil['transmisi'].upper() == transmisi.upper():
            hasil_filter.append(mobil) 
    return hasil_filter

# ---------------------------------------------------------------------------------------------------------------------------
# (1.3.3) Fungsi untuk mencari mobil berdasarkan jenis
def filter_mobil_berdasarkan_jenis(jenis):
    hasil_filter = []
    for mobil in database_mobil:
        if mobil['jenis'].lower() == jenis.lower():
            hasil_filter.append(mobil)
    return hasil_filter

# ---------------------------------------------------------------------------------------------------------------------------
# (1.3.4) Fungsi untuk mencari mobil berdasarkan kapasitas
def filter_mobil_berdasarkan_kapasitas(kapasitas):
    hasil_filter = []
    for mobil in database_mobil:
        if mobil['kapasitas'].lower() == kapasitas.lower():
            hasil_filter.append(mobil)
    return hasil_filter

# ---------------------------------------------------------------------------------------------------------------------------
# (1.4) Fungsi untuk mengurutkan mobil secara ascending/descending berdasarkan value
def sort_mobil():
    pilihan_sort = input('Urutkan mobil berdasarkan (brand/tipe/jenis/tahun/harga_sewa/kapasitas/transmisi): ').lower()

    if pilihan_sort not in ['brand', 'tipe', 'jenis', 'tahun', 'harga_sewa', 'kapasitas', 'transmisi']:
        print(Fore.BLUE + Style.BRIGHT + 'Pilihan sort tidak valid.')
        return

    urutan = input('Pilih urutan (ascending/descending): ').lower()
    if urutan not in ['ascending', 'descending']:
        print(Fore.BLUE + Style.BRIGHT + 'Pilihan urutan tidak valid.')
        return

    reverse_sort = urutan == 'descending'

    def values_sort(mobil):
        return mobil[pilihan_sort]

    sorted_mobil = sorted(database_mobil, key=values_sort, reverse=reverse_sort)

    print("=======================Daftar Mobil============================")
    print(tabulate(sorted_mobil, headers='keys', tablefmt='grid'))

# ===========================================================================================================================

# ===========================================================================================================================
# (2) FUNGSI UNTUK MENU MENAMBAHKAN MOBIL BARU
# ---------------------------------------------------------------------------------------------------------------------------
def menu_tambah_mobil(): # Fungsi Create
    while True:
        print('''
-----------------------------------------
|        Menu Tambah Mobil              |
|---------------------------------------|
| 1. Tambah Mobil                       |
| 2. Kembali ke Menu Utama              |
-----------------------------------------
                ''')                    
        pilihan_menu = input("Pilih menu (1-2): ")

        if pilihan_menu.isdigit() == False :
            print('\nInput harus berupa angka')
        else : 
            if pilihan_menu == '1':
                tambah_mobil()

            elif pilihan_menu == '2' :
                kembali_menu_utama()
            
            else:
                print(Fore.RED + Style.BRIGHT + '\nMasukkan input dengan benar')

# ------------------------------------------------------------------------------------------------------------------------
# (2.1) Fungsi Menambah data satu-persatu 
def tambah_mobil():
    while True:
        kode_mobil_baru = input('Masukkan kode mobil baru harus di atas 100: ')
        if kode_mobil_baru.isdigit() == False:
            print(Fore.RED + Style.BRIGHT + 'Input harus berupa angka')
            menu_tambah_mobil()

        kode_mobil_baru = int(kode_mobil_baru)
        if kode_mobil_baru <= 100:
            print(Fore.RED + Style.BRIGHT + 'Kode mobil harus di atas 100')
            menu_tambah_mobil()

        for mobil in database_mobil:
            if mobil['kode_mobil'] == kode_mobil_baru:
                print('\nMobil tersebut telah tersedia')
                print(Fore.RED + Style.BRIGHT + 'Tidak dapat menambahkan kode yang telah ada\n')
                menu_tambah_mobil()
        else:

            while True:
                brand = input('Brand mobil: ')
                if brand.isalnum() == False and brand.replace(' ' , '').isalnum() == False:
                    print(Fore.RED + Style.BRIGHT + '\nBrand harus berupa huruf')
                else:
                    break
            
            while True:
                tipe = input('Tipe mobil: ')
                if tipe.isalnum() == False and tipe.replace(' ' , '').isalnum() == False:
                    print(Fore.RED + Style.BRIGHT + '\nTipe harus berupa huruf')
                else:
                    break

            while True:    
                jenis = input('Jenis mobil: ')
                if jenis.isalpha() == False:
                    print(Fore.RED + Style.BRIGHT + '\nJenis harus berupa huruf')
                else:
                    break
            while True:
                tahun = input('Tahun mobil: ')
                if tahun.isdigit() == False:
                    print(Fore.RED + Style.BRIGHT + '\nTahun harus berupa angka')
                else:
                    break

            while True:
                harga_sewa = input('Harga sewa: ')
                if harga_sewa.isdigit() == False:
                    print(Fore.RED + Style.BRIGHT + '\nHarga sewa harus berupa angka')
                else:
                    break

            while True:
                kapasitas = input('Kapasitas mobil (5/7): ')
                if kapasitas not in ['5', '7']:
                    print(Fore.RED + Style.BRIGHT + '\nKapasitas harus berupa angka 5 atau 7')
                else:
                    break

            while True:
                transmisi = input('Transmisi mobil (AT/MT): ').upper()
                if transmisi not in ['AT', 'MT']:
                    print(Fore.RED + Style.BRIGHT + '\nTransmisi harus AT atau MT')
                else:
                    break  # Keluar dari loop input transmisi jika input valid

            save_data = input('Simpan data mobil baru? (y/n): ').lower()
            if save_data == 'y':
                database_mobil.append(
                    {
                        'kode_mobil': kode_mobil_baru,
                        'brand': brand,
                        'tipe': tipe,
                        'jenis': jenis,
                        'tahun': tahun,
                        'harga_sewa': harga_sewa,
                        'kapasitas': kapasitas,
                        'transmisi': transmisi
                    })
                print(Fore.BLUE + Style.BRIGHT + '\nMobil baru telah tersimpan')

            break  # Keluar dari loop input utama setelah data berhasil disimpan
         
# ===========================================================================================================================
# ===========================================================================================================================
# (3) FUNGSI UNTUK MENU UPDATE MOBIL
# ---------------------------------------------------------------------------------------------------------------------------

def menu_update_mobil():
    while True:
        print('''
-----------------------------------------
|        Menu update mobil              |
|---------------------------------------|
| 1. Update Mobil                       |
| 2. Update Mobil Per-Values            |
| 3. Kembali ke Menu Utama              |
-----------------------------------------
                ''')                    
        pilihan_menu = input("Pilih menu (1-3): ")

        if pilihan_menu.isdigit() == False :
            print(Fore.RED + Style.BRIGHT + 'Input harus berupa angka')
        else : 
            if pilihan_menu == '1':
                if len(database_mobil) == 0:
                    print(Fore.YELLOW + Style.BRIGHT + "\nDaftar mobil kosong.\n")
                elif len(database_mobil) != 0 :                
                    update_mobil()
            elif pilihan_menu == '2' :
                if len(database_mobil) == 0:
                    print(Fore.YELLOW + Style.BRIGHT + "\nDaftar mobil kosong.\n")
                elif len(database_mobil) != 0 :                
                    update_mobil_satuan()        
            elif pilihan_menu == '3' :
                kembali_menu_utama()
            else:
                print(Fore.RED + Style.BRIGHT + 'Masukkan input dengan benar')

# --------------------------------------------------------------------------------------------------------------------------- 
# (3.1) Fungsi Mengedit dan Update data Mobil yang sudah ada 

def update_mobil():
    while True:
        kode_mobil_ganti = input('Masukkan kode mobil yang ingin diperbarui: ')
        if kode_mobil_ganti.isdigit() == False:
            print(Fore.RED + Style.BRIGHT + 'Input harus berupa angka')
            continue

        kode_mobil_ganti = int(kode_mobil_ganti)
        for mobil in database_mobil:
            if mobil['kode_mobil'] == kode_mobil_ganti:
                print(f"\nKode Mobil: {mobil['kode_mobil']}") 
                print(f"Brand: {mobil['brand']}") 
                print(f"Tipe: {mobil['tipe']}") 
                print(f"Jenis: {mobil['jenis']}") 
                print(f"Tahun: {mobil['tahun']}")
                print(f"Harga Sewa: {mobil['harga_sewa']}")
                print(f"Kapasitas: {mobil['kapasitas']}")
                print(f"Transmisi: {mobil['transmisi']}") 

                while True:
                    brand = input('Brand mobil (Enter untuk tidak mengubah): ')
                    if brand.isalnum() == False and brand.replace(' ' , '').isalnum() == False:
                        print(Fore.RED + Style.BRIGHT + 'Brand harus berupa huruf atau angka')
                    else:
                        break

                while True:
                    tipe = input('Tipe mobil (Enter untuk tidak mengubah): ')
                    if tipe.isalnum() == False and tipe.replace(' ' , '').isalnum() == False:
                        print(Fore.RED + Style.BRIGHT + 'Tipe harus berupa huruf atau angka')
                    else:
                        break

                while True:
                    jenis = input('Jenis mobil (Enter untuk tidak mengubah): ')
                    if jenis and not jenis.isalpha():
                        print(Fore.RED + Style.BRIGHT + 'Jenis harus berupa huruf')
                    else:
                        break

                while True:
                    tahun = input('Tahun mobil (Enter untuk tidak mengubah): ')
                    if tahun and not tahun.isdigit():
                        print(Fore.RED + Style.BRIGHT + 'Tahun harus berupa angka')
                    else:
                        break

                while True:
                    harga_sewa = input('Harga sewa (Enter untuk tidak mengubah): ')
                    if harga_sewa and not harga_sewa.isdigit():
                        print(Fore.RED + Style.BRIGHT + 'Harga sewa harus berupa angka')
                    else:
                        break

                while True:
                    kapasitas = input('Kapasitas mobil (5/7/Enter untuk tidak mengubah): ')
                    if kapasitas and kapasitas not in ['5', '7']:
                        print(Fore.RED + Style.BRIGHT + 'Kapasitas harus berupa angka 5 atau 7')
                    else:
                        break

                while True:
                    transmisi = input('Transmisi mobil (AT/MT/Enter untuk tidak mengubah): ').upper()
                    if transmisi and transmisi not in ['AT', 'MT']:
                        print(Fore.RED + Style.BRIGHT + 'Transmisi harus AT atau MT')
                    else:
                        break

                if brand:
                    mobil['brand'] = brand
                if tipe:
                    mobil['tipe'] = tipe
                if jenis:
                    mobil['jenis'] = jenis
                if tahun:
                    mobil['tahun'] = tahun
                if harga_sewa:
                    mobil['harga_sewa'] = harga_sewa
                if kapasitas:
                    mobil['kapasitas'] = kapasitas
                if transmisi:
                    mobil['transmisi'] = transmisi

                print('Data mobil telah diperbarui.')
                
                print(f"\nKode Mobil: {mobil['kode_mobil']}") 
                print(f"Brand: {mobil['brand']}") 
                print(f"Tipe: {mobil['tipe']}") 
                print(f"Jenis: {mobil['jenis']}") 
                print(f"Tahun: {mobil['tahun']}")
                print(f"Harga Sewa: {mobil['harga_sewa']}")
                print(f"Kapasitas: {mobil['kapasitas']}")
                print(f"Transmisi: {mobil['transmisi']}") 
                
                break
        else:
            print(Fore.RED + Style.BRIGHT + 'Perintah Update Salah, Pilih Menu Update Kembali')
        break 

#------------------------------------------------------------------------------------------------------------------
# (3.2) Fungsi Mengedit dan Update data Mobil yang sudah ada berdasarkan Values

def update_mobil_satuan():
    kode_mobil_update = input('Masukkan kode mobil yang ingin diperbarui: ')
    
    if kode_mobil_update.isdigit() == False:
        print(Fore.RED + Style.BRIGHT + 'Input harus berupa angka')
        return
    
    kode_mobil_update = int(kode_mobil_update)
    
    for mobil in database_mobil:
        if mobil['kode_mobil'] == kode_mobil_update:
            
            print(f"\nKode Mobil: {mobil['kode_mobil']}") 
            print(f"Brand: {mobil['brand']}") 
            print(f"Tipe: {mobil['tipe']}") 
            print(f"Jenis: {mobil['jenis']}") 
            print(f"Tahun: {mobil['tahun']}")
            print(f"Harga Sewa: {mobil['harga_sewa']}")
            print(f"Kapasitas: {mobil['kapasitas']}")
            print(f"Transmisi: {mobil['transmisi']}") 
            values = input('Masukkan update data berdasarkan (brand/tipe/jenis/tahun/harga_sewa/kapasitas/transmisi): ').lower()
            
            if values == 'brand':
                brand_baru = input('Masukkan brand baru: ').lower()
                mobil['brand'] = brand_baru

            elif values == 'tipe':
                tipe_baru = input('Masukkan tipe baru: ').lower()
                mobil['tipe'] = tipe_baru

            elif values == 'jenis':
                jenis_baru = input('Masukkan jenis baru: ').lower()
                mobil['jenis'] = jenis_baru
            
            elif values == 'tahun':
                tahun_baru = input('Masukkan tahun baru: ')
                mobil['tahun'] = tahun_baru
            
            elif values == 'harga_sewa':
                harga_sewa_baru = input('Masukkan harga sewa baru: ')
                mobil['harga_sewa'] = harga_sewa_baru
            
            elif values == 'kapasitas':
                kapasitas_baru = input('Masukkan kapasitas baru (5/7): ')
                if kapasitas_baru in ['5', '7']:
                    mobil['kapasitas'] = kapasitas_baru
                else:
                    print(Fore.RED + Style.BRIGHT + 'Kapasitas harus berupa angka 5 atau 7')
            
            elif values == 'transmisi':
                transmisi_baru = input('Masukkan transmisi baru (AT/MT): ')
                if transmisi_baru.upper() in ['AT', 'MT']:
                    mobil['transmisi'] = transmisi_baru.upper()
                else:
                    print(Fore.RED + Style.BRIGHT + 'Transmisi harus AT atau MT')
            
            else:
                print(Fore.RED + Style.BRIGHT + 'Input tidak valid. Data tidak diperbarui.')
                break
            
            print(Fore.BLUE + Style.BRIGHT + 'Data mobil telah diperbarui.')
            
            print(f"\nKode Mobil: {mobil['kode_mobil']}") 
            print(f"Brand: {mobil['brand']}") 
            print(f"Tipe: {mobil['tipe']}") 
            print(f"Jenis: {mobil['jenis']}") 
            print(f"Tahun: {mobil['tahun']}")
            print(f"Harga Sewa: {mobil['harga_sewa']}")
            print(f"Kapasitas: {mobil['kapasitas']}")
            print(f"Transmisi: {mobil['transmisi']}") 
            break
    else:
        print(Fore.RED + Style.BRIGHT + 'Mobil dengan kode tersebut tidak ditemukan.')

# ===========================================================================================================================
# ===========================================================================================================================
# (4) FUNGSI MENU UNTUK MENGHAPUS MOBIL BERDASARKAN KODE MOBIL
# ---------------------------------------------------------------------------------------------------------------------------

def menu_delete_mobil():
    while True:
        print('''
---------------------------------------------
|        Menu Hapus Stok Mobil              |
|-------------------------------------------|
| 1. Menghapus Mobil Sesuai Kode Mobil      |
| 2. Menghapus Semua Mobil                  |
| 3. Mengembalikan Mobil yang baru dihapus  |
| 4. Kembali ke Menu Utama                  |
---------------------------------------------
                ''')                    
        pilihan_menu = input("Pilih menu (1-4): ")

        if pilihan_menu.isdigit() == False :
            print(Fore.RED + Style.BRIGHT + 'Input harus berupa angka')
        else : 
            if pilihan_menu == '1':
                if len(database_mobil) == 0:
                    print(Fore.YELLOW + Style.BRIGHT + "\nDaftar mobil kosong.\n")
                elif len(database_mobil) != 0 :   
                    delete_mobil()
            
            elif pilihan_menu == '2' :
                delete_semua_mobil()
            
            elif pilihan_menu == '3' :
                if len(database_mobil) == 0:
                    print(Fore.YELLOW + Style.BRIGHT + "\nDaftar mobil kosong.\n")
                elif len(database_mobil) != 0 :   
                    recover_mobil()        
            
            elif pilihan_menu == '4' :
                kembali_menu_utama()
            
            else:
                print('Masukkan input dengan benar')

# --------------------------------------------------------------------------------------------------------------------------- 
# (4.1) Fungsi untuk menghapus mobil berdasarkan kode_mobil

def delete_mobil(): 
    while True:
        kode_mobil_del = input('Masukkan kode mobil yang ingin dihapus: ')
        
        if kode_mobil_del.isdigit() == False:
            print(Fore.RED + Style.BRIGHT + 'Input harus berupa angka')
        else:
            kode_mobil_del = int(kode_mobil_del)
            
            for mobil in database_mobil:
                if mobil['kode_mobil'] == kode_mobil_del:
                    print(f"\nMobil dengan kode {kode_mobil_del} akan dihapus dari database.")
                    konfirmasi = input('Apakah Anda yakin? (y/n): ')
                    if konfirmasi.lower() == 'y':
                        database_mobil_recyclebin.append(mobil) # Simpan mobil ke recycle bin
                        database_mobil.remove(mobil)  # Menghapus mobil dari database_mobil
                        print(f"Mobil dengan kode {kode_mobil_del} telah dihapus.")
                        print("=============Daftar Mobil===================")
                        print(tabulate(database_mobil, headers='keys', tablefmt='grid'))
                    elif konfirmasi.lower() == 'n':
                        break
                    else :
                        print(Fore.RED + Style.BRIGHT + 'Masukkan Input dengan benar')
            else:
                print(f"Mobil dengan kode mobil {kode_mobil_del} tidak ditemukan dalam database mobil.")

        lanjutkan = input('Apakah Anda ingin menghapus mobil lain? (y/n or anykey): ').lower()
        if lanjutkan != 'y':
            break

# --------------------------------------------------------------------------------------------------------------------------- 
# (4.2) Fungsi untuk delete semua mobil dalam

def delete_semua_mobil():
    hapus_semua_mobil = input('Anda yakin ingin menghapus semua mobil dari database? (y/n): ')
    if hapus_semua_mobil.lower() == 'y':
        database_mobil.clear()
        print(Fore.YELLOW + Style.BRIGHT + 'Semua mobil telah dihapus dari database.')
    elif hapus_semua_mobil.lower() == 'n':
        print('Semua Mobil Tidak Jadi Dihapus.')
    else:
        print('Masukkan input yang valid (y/n) untuk mengkonfirmasi penghapusan semua mobil.')

# --------------------------------------------------------------------------------------------------------------------------- 
# (4.3) Fungsi untuk membuat recovery (recycle bin) pada data yang baru saja dihapus

database_mobil_recyclebin = []  # Recycle bin

def recover_mobil():
    print("=============Daftar Mobil===================")
    print(tabulate(database_mobil_recyclebin, headers='keys', tablefmt='grid'))
    while True:
        kode_mobil_recover = input('Masukkan kode mobil yang ingin dikembalikan: ')

        if kode_mobil_recover.isdigit() == False:
            print(Fore.RED + Style.BRIGHT + 'Input harus berupa angka')
        else:
            kode_mobil_recover = int(kode_mobil_recover)

            for mobil in database_mobil_recyclebin:
                if mobil['kode_mobil'] == kode_mobil_recover:
                    print(f"\nMobil dengan kode {kode_mobil_recover} akan dikembalikan ke database utama.")
                    konfirmasi = input('Apakah Anda yakin? (y/n): ')
                    if konfirmasi.lower() == 'y':
                        database_mobil.append(mobil)  # Mengembalikan mobil ke database utama
                        database_mobil_recyclebin.remove(mobil)  # Menghapus mobil dari recycle bin
                        print(Fore.BLUE + Style.BRIGHT + f"Mobil dengan kode {kode_mobil_recover} telah dikembalikan ke database utama.")
                    elif konfirmasi.lower() == 'n':
                        break
                    else:
                        print(Fore.RED + Style.BRIGHT + 'Masukkan input dengan benar')
            else:
                print(f"Mobil dengan kode {kode_mobil_recover} tidak ditemukan dalam recycle bin.")

        lanjutkan = input('Apakah Anda ingin mengembalikan mobil lain? (y/n or anykey): ').lower()
        if lanjutkan != 'y':
            break

# ===========================================================================================================================
# ===========================================================================================================================
# (5) FUNGSI MENU UNTUK BIAYA SEWA MOBIL
#----------------------------------------------------------------------------------------------------------------------------
def menu_sewa_mobil(): # Fungsi Sewa Mobil
    while True:
        print('''
-----------------------------------------
|        Menu Sewa Mobil                |
|---------------------------------------|
| 1. Biaya Sewa Mobil                   |
| 2. Kembali ke Menu Utama              |
-----------------------------------------
                ''')                    
        pilihan_menu = input("Pilih menu (1-2): ")

        if pilihan_menu.isdigit() == False :
            print(Fore.RED + Style.BRIGHT + '\nInput harus berupa angka')
        else : 
            if pilihan_menu == '1':
                if len(database_mobil) == 0:
                    print(Fore.YELLOW + Style.BRIGHT + "\nDaftar mobil kosong.\n")
                elif len(database_mobil) != 0 :   
                    biaya_sewa()
            elif pilihan_menu == '2' :
                kembali_menu_utama()
            
            else:
                print(Fore.RED + Style.BRIGHT + '\nMasukkan input dengan benar')
# ---------------------------------------------------------------------------------------------------------------------------
# (5.1) Fungsi menghitung biaya sewa mobil

def biaya_sewa():
    print("=============Daftar Mobil===================")
    print(tabulate(database_mobil, headers='keys', tablefmt='grid'))
    while True:
        hari_sewa = input('Sewa berapa hari? ')
        if hari_sewa.isdigit() == False:
            print(Fore.RED + Style.BRIGHT + 'Input harus berupa angka.')
            continue
        hari_sewa = int(hari_sewa)

        kode_mobil_sewa = input('Pilih mobil yang ingin disewa (kode_mobil): ')
        if kode_mobil_sewa.isdigit() == False:
            print(Fore.RED + Style.BRIGHT + 'Kode mobil harus berupa angka.')
            continue
        kode_mobil_sewa = int(kode_mobil_sewa)

        for mobil in database_mobil:
            if kode_mobil_sewa == mobil['kode_mobil']:
                harga_sewa = mobil['harga_sewa']
                biaya_rental = harga_sewa * hari_sewa

                print(f"\nKode Mobil: {mobil['kode_mobil']}") 
                print(f"Brand: {mobil['brand']}") 
                print(f"Tipe: {mobil['tipe']}") 
                print(f"Jenis: {mobil['jenis']}") 
                print(f"Tahun: {mobil['tahun']}")
                print(f"Harga Sewa: {mobil['harga_sewa']}")
                print(f"Kapasitas: {mobil['kapasitas']}")
                print(f"Transmisi: {mobil['transmisi']}") 

                print(Fore.BLUE + Style.BRIGHT + f"\nBiaya sewa mobil {mobil['brand']} {mobil['tipe']} selama {hari_sewa} hari adalah: {biaya_rental}")
                return
        else:
            print(Fore.RED + Style.BRIGHT + 'Mobil dengan kode tersebut tidak ditemukan.')
        
        lanjut = input('Ingin menghitung biaya sewa lagi? (y/n or anykey): ').lower()
        if lanjut != 'y':
            break

# ===========================================================================================================================
# ===========================================================================================================================
# Tambahkan opsi ini di dalam menu_utama() atau menu lainnya sesuai kebutuhan.            
# Fungsi untuk pilihan dan menu

def kembali_menu_utama():
    while True :
        ke_menu_utama = input('Apakah anda yakin untuk kembali ke menu utama?(y/n)' )
        if ke_menu_utama.lower() == 'y':
            menu_utama()
        elif ke_menu_utama.lower() == 'n':
            break
        else :
            print('masukkan input dengan benar')

def output_kondisi_mobil(hasil_filter):
    # if len(database_mobil) == 0:
    #     print(Fore.YELLOW + Style.BRIGHT + 'Data Mobil Telah Terhapus Semua')
    if hasil_filter:
        print("=======================Daftar Mobil============================")
        print(tabulate(hasil_filter, headers='keys', tablefmt='grid'))
    else:
        print('opsi yang anda masukkan tidak tersedia di rental kami')

def keluar_program():
    keluar = input('Apakah anda yakin untuk keluar program? (y/n)')
    if keluar.lower() == 'y':
        exit()
    elif keluar.lower() == 'n':
        menu_utama()
    else:
        print('masukkan input dengan benar')

def data_kosong():
    if len(database_mobil) == 0:
        print(Fore.YELLOW + Style.BRIGHT + "\nDaftar mobil kosong.\n")
    elif len(database_mobil) != 0 :
        print()

# ==========================================================================================================================
# ==========================================================================================================================

# Menu utama aplikasi
def menu_utama():
    while True:
        print('''
|---------------------------|
|   Rental Mobil std        |
|---------------------------|
| 1. Lihat Mobil            |
| 2. Tambah Mobil           |
| 3. Update Data Mobil      |
| 4. Hapus Stok Mobil       |
| 5. Biaya Sewa Mobil       |
| 6. Keluar Program         |
|---------------------------|
            ''')
        
        pilihan_menu = input("Pilih menu (1-6): ")

        if pilihan_menu.isdigit() == False :
            print('Input harus berupa angka')
        elif pilihan_menu.isdigit() == True :
            pilihan_menu = int(pilihan_menu)

            if pilihan_menu == 1:
                menu_lihat_mobil()
            
            elif pilihan_menu == 2:
                menu_tambah_mobil()

            elif pilihan_menu == 3:
                menu_update_mobil()

            elif pilihan_menu == 4:
                menu_delete_mobil()
            
            elif pilihan_menu == 5 :
                menu_sewa_mobil()
        
            elif pilihan_menu == 6:
                keluar_program()

            else:
                print(Fore.RED + Style.BRIGHT + 'Masukkan input dengan benar')

menu_utama()

#==========================================================================================================================
#========================================================================================================================== 