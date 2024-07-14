ListBarang  = [
    {
    'Kode item' : 'com112',
    'Nama item' : 'mouse',
    'Merk' : 'logitech',
    'Type'  : 'G403',
    'Harga' : 120000,
    'Stok' : 150
    },
    {
    'Kode item' : 'com113',
    'Nama item' : 'keyboard',
    'Merk' : 'Steelseries',
    'Type'  : 'M750 TKL',
    'Harga' : 1100000,
    'Stok' : 50
    },
    {
    'Kode item' : 'com114',
    'Nama item' : 'keyboard',
    'Merk' : 'Ajazz',
    'Type'  : 'Ak-303',
    'Harga' : 1500000,
    'Stok' : 30
    }
]



def menampilkanDaftarItem1():
    print('\n-----  List Stock Barang  -----\n')
    print(' '+'Nomor\t| Kode\t\t|  Nama\t\t|   Merk\t|  Type\t\t|  Harga\t|  Stok')
    for i in range(len(ListBarang)):
        print('   {}\t| {}\t|  {}\t|   {}\t|  {}\t\t|  {}\t|  {}\t'.format(i+1,ListBarang[i]['Kode item'],ListBarang[i]['Nama item'],ListBarang[i]['Merk'],ListBarang[i]['Type'],ListBarang[i]['Harga'],ListBarang[i]['Stok']))



def tampilanKode():
        kodeItem = input('\n   Masukkan kode item : ').lower()
        print('\n----- List Stock Barang -----\n')
        print(' '+'Nomor\t| Kode\t\t|  Nama\t\t|   Merk\t|  Type\t\t|  Harga\t|  Stok')
        for i in range(len(ListBarang)):
            if kodeItem == ListBarang[i]['Kode item']:
                print('   {}\t| {}\t|  {}\t|   {}\t|  {}\t\t|  {}\t|  {}\t'.format(i+1,ListBarang[i]['Kode item'],ListBarang[i]['Nama item'],ListBarang[i]['Merk'],ListBarang[i]['Type'],ListBarang[i]['Harga'],ListBarang[i]['Stok']))
                break
        else:
            print('\n     "Data tidak ditemukan"')


def tampilanPencarian():
        Search = input('\n     Masukkan keyword : ').lower()
        print('\n----- List Stock Barang -----\n')
        print(' '+'Nomor\t| Kode\t\t|  Nama\t\t|   Merk\t|  Type\t\t|  Harga\t|  Stok')
        for i in range(len(ListBarang)):
            if  Search == ListBarang[i]['Nama item'] or Search == ListBarang[i]['Merk'] or Search == ListBarang[i]['Type']:
                print('   {}\t| {}\t|  {}\t|   {}\t|  {}\t\t|  {}\t|  {}\t'.format(i+1,ListBarang[i]['Kode item'],ListBarang[i]['Nama item'],ListBarang[i]['Merk'],ListBarang[i]['Type'],ListBarang[i]['Harga'],ListBarang[i]['Stok']))
            


def tampilanHarga():
        Harga1 = int(input('\n     Masukkan harga minimum : '))
        Harga2 = int(input('     Masukkan harga maksimum : '))
        print('\n----- List Stock Barang -----\n')
        print(' '+'Nomor\t| Kode\t\t|  Nama\t\t|   Merk\t|  Type\t\t|  Harga\t|  Stok')
        for i in range(len(ListBarang)):
            if Harga1 <= ListBarang[i]['Harga'] <= Harga2:
              print('   {}\t| {}\t|  {}\t|   {}\t|  {}\t\t|  {}\t|  {}\t'.format(i+1,ListBarang[i]['Kode item'],ListBarang[i]['Nama item'],ListBarang[i]['Merk'],ListBarang[i]['Type'],ListBarang[i]['Harga'],ListBarang[i]['Stok']))



def tampilanStok():
        Stok = int(input('\n     Masukkan stok maksimum yang dicari : '))
        print('\n----- List Stock Barang -----\n')
        print(' '+'Nomor\t| Kode\t\t|  Nama\t\t|   Merk\t|  Type\t\t|  Harga\t|  Stok')
        for i in range(len(ListBarang)):
            if ListBarang[i]['Stok'] <= Stok:
              print('   {}\t| {}\t|  {}\t|   {}\t|  {}\t\t|  {}\t|  {}\t'.format(i+1,ListBarang[i]['Kode item'],ListBarang[i]['Nama item'],ListBarang[i]['Merk'],ListBarang[i]['Type'],ListBarang[i]['Harga'],ListBarang[i]['Stok']))



def menampilkanDaftarItem2():
    while True:
        menuMenampilkanDaftarItem2 = input ('''
        1. Tampilkan data berdasar kode 
        2. Tampilkan data berdasar kata kunci
        3. Tampilkan data berdasar range harga
        4. Tampilkan data berdasar jumlah stok yang ada
        5. Kembali ke menu sebelumnya

        Silahkan Pilih sub-menu tampilan data [1-5] : ''')

        if menuMenampilkanDaftarItem2 == '1' :
            tampilanKode()
        elif menuMenampilkanDaftarItem2 == '2' :
            tampilanPencarian()
        elif menuMenampilkanDaftarItem2 == '3':
            tampilanHarga()
        elif menuMenampilkanDaftarItem2 == '4':
            tampilanStok()
        elif menuMenampilkanDaftarItem2 == '5':
            break


def ReadData():
    while True:
        pilihMenuRead = input('''
        1. Tampilkan data keseluruhan
        2. Tampilkan data berdasarkan kode tertentu
        3. Kembali ke menu utama

        Silahkan pilih sub-menu read data [1-3] : ''')

        if pilihMenuRead == '1' :
            menampilkanDaftarItem1()
        elif pilihMenuRead == '2' :
            menampilkanDaftarItem2()
        elif pilihMenuRead == '3' :
            break
            
def menambahDaftarItem():
    while True:
        inputKode = input('\n        Masukkan kode item : ').lower()
        inputItem = input('        Masukkan nama item : ').lower()
        inputMerk = input('        Masukkan nama merk : ').lower()
        inputType = input('        Masukkan nama type : ').lower()
        inputHarga = int(input('        Masukkan harga : '))
        inputStok = int(input('        Masukkan jumlah stok : '))
        tambahan = {
        'Kode item' : '{}'.format(inputKode),
        'Nama item' : '{}'.format(inputItem),
        'Merk' : '{}'.format(inputMerk),
        'Type' : '{}'.format(inputType),
        'Harga' : '{}'.format(inputHarga),
        'Stok' : '{}'.format(inputStok)
    }
        print('\n        Item yang ditambahkan adalah : ',tambahan)
        checkerCreate = input('\n        Apakah sudah benar? (Y/N) : ').lower()
        if checkerCreate == 'y':
            ListBarang.append(tambahan)
            print('\n        "Item berhasil ditambahkan"')
            break
        elif checkerCreate == 'n':
            print('\n        "Item tidak ditambahkan"')
            break
        else:
            break
        
            
def CreateData():
    while True:
        pilihMenuCreate = input('''
        1. Tambahkan data item baru
        2. Kembali ke menu utama
        
        Silahkan pilih sub-menu create data [1-2] : ''')
    
        if pilihMenuCreate == '1' :
            menambahDaftarItem()
        elif pilihMenuCreate == '2' :
            break


def Update():
    upCode = input('\n        Masukkan kode barang yang ingin diupdate : ')
    print('\n----- List Stock Barang -----\n')
    for i in range(len(ListBarang)):
        if upCode == ListBarang[i]['Kode item']:
            print(' '+'Nomor\t| Kode\t\t|  Nama\t\t|   Merk\t|  Type\t\t|  Harga\t|  Stok')
            print('   {}\t| {}\t|  {}\t|   {}\t|  {}\t\t|  {}\t|  {}\t'.format(i+1,ListBarang[i]['Kode item'],ListBarang[i]['Nama item'],ListBarang[i]['Merk'],ListBarang[i]['Type'],ListBarang[i]['Harga'],ListBarang[i]['Stok']))
            confupd = input('\n        Apakah data ini yang ingin diupdate? (Y/N) : ' ).lower()
            if confupd == 'y':
                while True:
                    pilihanMenuUpdate = input('''
                    1. Update kode item
                    2. Update nama item
                    3. Update merk item
                    4. Update type item
                    5. Update harga item
                    6. Update stock item
                    7. Update selesai
                    
                    Silahkan masukkan sub-menu update data (1-7) : ''')
                   
                    if pilihanMenuUpdate == '1':
                        ListBarang[i]['Kode item'] = input('\n        Update kode : ').lower()
                        print('\n        "Data berhasil diupdate"\n')
                        print(' '+'Nomor\t| Kode\t\t|  Nama\t\t|   Merk\t|  Type\t\t|  Harga\t|  Stok')
                        print('   {}\t| {}\t|  {}\t|   {}\t|  {}\t\t|  {}\t|  {}\t'.format(i+1,ListBarang[i]['Kode item'],ListBarang[i]['Nama item'],ListBarang[i]['Merk'],ListBarang[i]['Type'],ListBarang[i]['Harga'],ListBarang[i]['Stok']))
                    elif pilihanMenuUpdate == '2':
                        ListBarang[i]['Nama item'] = input('\n        Update nama : ').lower()
                        print('\n        "Data berhasil diupdate"\n')
                        print(' '+'Nomor\t| Kode\t\t|  Nama\t\t|   Merk\t|  Type\t\t|  Harga\t|  Stok')
                        print('   {}\t| {}\t|  {}\t|   {}\t|  {}\t\t|  {}\t|  {}\t'.format(i+1,ListBarang[i]['Kode item'],ListBarang[i]['Nama item'],ListBarang[i]['Merk'],ListBarang[i]['Type'],ListBarang[i]['Harga'],ListBarang[i]['Stok']))
                    elif pilihanMenuUpdate == '3':
                        ListBarang[i]['Merk'] = input('\n        Update merk : ').lower()
                        print('\n        "Data berhasil diupdate"\n')
                        print(' '+'Nomor\t| Kode\t\t|  Nama\t\t|   Merk\t|  Type\t\t|  Harga\t|  Stok')
                        print('   {}\t| {}\t|  {}\t|   {}\t|  {}\t\t|  {}\t|  {}\t'.format(i+1,ListBarang[i]['Kode item'],ListBarang[i]['Nama item'],ListBarang[i]['Merk'],ListBarang[i]['Type'],ListBarang[i]['Harga'],ListBarang[i]['Stok']))
                    elif pilihanMenuUpdate == '4':
                        ListBarang[i]['Type'] = input('\n        Update type : ').lower()
                        print('\n        "Data berhasil diupdate"\n')
                        print(' '+'Nomor\t| Kode\t\t|  Nama\t\t|   Merk\t|  Type\t\t|  Harga\t|  Stok')
                        print('   {}\t| {}\t|  {}\t|   {}\t|  {}\t\t|  {}\t|  {}\t'.format(i+1,ListBarang[i]['Kode item'],ListBarang[i]['Nama item'],ListBarang[i]['Merk'],ListBarang[i]['Type'],ListBarang[i]['Harga'],ListBarang[i]['Stok']))
                    elif pilihanMenuUpdate == '5':
                        ListBarang[i]['Harga'] = int(input('\n        Update harga : '))
                        print('\n        "Data berhasil diupdate"\n')
                        print(' '+'Nomor\t| Kode\t\t|  Nama\t\t|   Merk\t|  Type\t\t|  Harga\t|  Stok')
                        print('   {}\t| {}\t|  {}\t|   {}\t|  {}\t\t|  {}\t|  {}\t'.format(i+1,ListBarang[i]['Kode item'],ListBarang[i]['Nama item'],ListBarang[i]['Merk'],ListBarang[i]['Type'],ListBarang[i]['Harga'],ListBarang[i]['Stok']))
                    elif pilihanMenuUpdate == '6':
                        ListBarang[i]['Stok'] = int(input('\n        Update stok : '))
                        print('\n        "Data berhasil diupdate"\n')
                        print(' '+'Nomor\t| Kode\t\t|  Nama\t\t|   Merk\t|  Type\t\t|  Harga\t|  Stok')
                        print('   {}\t| {}\t|  {}\t|   {}\t|  {}\t\t|  {}\t|  {}\t'.format(i+1,ListBarang[i]['Kode item'],ListBarang[i]['Nama item'],ListBarang[i]['Merk'],ListBarang[i]['Type'],ListBarang[i]['Harga'],ListBarang[i]['Stok']))
                    elif pilihanMenuUpdate == '7':
                        break
            elif confupd == 'n':
                print('\n        "Data tidak diupdate"')
                break
            else:
                print('\n        "Perintah yang anda masukkan salah"')
                break


def UpdateData():
    while True:
        pilihMenuUpdate = input('''
        1. Update data
        2. Kembali ke menu utama
        
        Silahkan pilih Sub-Menu Create Data [1-2] : ''')

        if pilihMenuUpdate == '1' :
            Update()
        elif pilihMenuUpdate == '2':
            break


def Delete():
    while True:
        delCode = input('\n        Masukkan kode item barang yang ingin dihapus : ').lower()
        for i in range(len(ListBarang)):
            if delCode == ListBarang[i]['Kode item']:
                print('\n        Item yang ingin dihapus adalah : ', ListBarang[i])
                confDel = input('\n        Apakah yakin ingin menghapus data ini? (Y/N) : ').lower()
                if confDel == 'y':
                    del ListBarang[i]
                    print('\n        "Data berhasil dihapus"') 
                    break
                elif confDel == 'n':
                    print('\n        "Data tidak terhapus"')
                    break
                else:
                    print('\n        "Perintah yang anda masukkan salah"')
                    break

        else:
            print('\n        "Data tidak ditemukan"')
        break


def DeleteData():
    while True:
        pilihMenuDelete = input('''
        1. Delete Data
        2. Kembali ke menu utama
        
        Silahkan pilih Sub-Menu Create Data [1-2] : ''')

        if pilihMenuDelete == '1' :
            Delete()
        elif pilihMenuDelete == '2':
            break

print('''
    Nama    : Sena Denis Permana,
    Program : JCDSOL-015 PURWADHIKA
        ''')
while True:
    masukan = input('''
    Selamat Datang di Aplikasi Data Stok GoodGaming

        List Menu :

        1. Menampilkan Daftar Item
        2. Menambah Item
        3. Update Item
        4. Delete Item

        Masukkan angka menu yang ingin dijalankan (1-4) : ''')
    if masukan =='1':
        ReadData()
    if masukan == '2':
        CreateData()
    if masukan == '3':
        UpdateData()
    elif masukan =='4':
        DeleteData()
