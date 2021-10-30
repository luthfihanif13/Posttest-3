#program kasir Luthfish Market
pilihan="y"
while pilihan=="y":
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("             Luthfish market            ")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(">>           Menu Pilihan             <<")
    print("----------------------------------------")
    print("list ikan    Nama Ikan         Harga    ")
    print("   1        Ikan Arwana    Rp. 1000000  ")
    print("   2        Ikan Pepper    Rp. 250000   ")
    print("   3        Ikan Nuptune   Rp. 50000    ")
    print("   4        Ikan Clarion   Rp. 75000    ")
    print("   5        Ikan Badut     Rp. 1000     ")
    print("========================================")

    hari = ["senin", "selasa", "rabu", "kamis", "jum'at", "sabtu", "ahad"]
    print(hari[0:7])
    hari=int(input("Masukkan Hari sesuai indeks tertera: "))
    #kode hari
    #senin  = 1 (diskon 10%) *hanya ikan arwana yang diskon:)
    #selasa = 2 
    #rabu   = 3
    #kamis  = 4 (diskon 25%) *hanya ikan clarion yang diskon:)
    #jum'at = libur(0)
    #sabtu  = 5
    #ahad   = 6
    nama = input("Nama pembeli :")
    pesan=str(input("masukkan list nomor ikan = "))
    jumlahpesan=int(input("masukkan jumlah pesanan ="))
    

    if pesan == "1":
        listnama= "Ikan Arwana"
        harga= (1000000*jumlahpesan)
        if jumlahpesan >= 1:
            diskon = int(harga*10/100)
            totalharga=int (harga-diskon)
        else:
            diskon = (0)
            totalharga= int(harga)
    elif pesan == "2":
        listnama= "Ikan Pepper"
        harga= (250000*jumlahpesan)
        if jumlahpesan >= 1:
            diskon = int(harga*0/100)
            totalharga=int (harga-diskon)
        else:
            diskon = (0)
            totalharga= int(harga)
    elif pesan == "3":
        listnama= "Ikan Nuptune"
        harga= (50000*jumlahpesan)
        if jumlahpesan >= 1:
            diskon = int(harga*0/100)
            totalharga=int (harga-diskon)
        else:
            diskon = (0)
            totalharga= int(harga)
    elif pesan == "4":
        listnama= "Ikan Clarion"
        harga= (750000*jumlahpesan)
        if jumlahpesan >= 1:
            diskon = int(harga*25/100)
            totalharga=int (harga-diskon)
        else:
            diskon = (0)
            totalharga= int(harga)
    elif pesan == "5":
        listnama= "Ikan Badut"
        harga= (1000*jumlahpesan)
        if jumlahpesan >= 1:
            diskon = int(harga*0/100)
            totalharga= int(harga-diskon)
        else:
            diskon = (0)
            totalharga= int(harga)
    else:
        listnama = "-"
        harga = "-"
        diskon = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan list menu yang tersedia, ingin mengulangi kembali y/t =")

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("             Luthfish market                ")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Nama         :", nama)
    print("Menu         :", listnama)
    print("Jumlah pesan :", jumlahpesan)
    print("harga        :", harga)
    print("Diskon       :", diskon)
    print("--------------------------------------------")
    print("Jumlah bayar :", totalharga)
    print("--------------------------------------------")
    pilihan=input("apakah anda ingin membeli kembali ? y/t =")
