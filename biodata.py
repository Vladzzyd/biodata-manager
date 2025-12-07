#KODE WARNA
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

riwayat_biodata = []
ulang = True
data_fungsi = ("input", "show", "delete", "edit", "quit")
pengulang = ("y","n")

def border():
    return CYAN + "="*50 + RESET

def judul(judul):
    print(border())
    print(CYAN + judul.center(50) + RESET)
    print(border())

def input_angka(nomor):
    while True:
        try:
            return int(input(nomor))
        except ValueError:
            print(RED + "ERROR: hanya bisa memasukkan angka!!" + RESET)

def input_biodata():
    judul("INPUT BIODATA")
    nama = input("masukkan nama anda               : ").title().strip()
    umur = input_angka("masukkan usia anda               : ")
    alamat = input("masukkan alamat lengkap anda     : ").title().strip()
    while True:
        nomor = input("masukkan nomor telepon aktif anda: ").strip()
        if nomor.isdigit():
            break
        print(RED + "ERROR: nomor harus berupa angka!" + RESET)
    email = input("masukkan e-mail aktif anda       : ").strip()

    hasil = {
        "nama":nama,
        "umur": umur,
        "alamat": alamat,
        "nomor": nomor,
        "email": email}
    return hasil

def tampilkan_biodata(data):
    print(border())
    print(YELLOW + "DATA BIODATA TERBARU".center(50) + RESET)
    print(border())

    print(GREEN + f"Nama   : {data['nama']}")
    print(GREEN + f"Umur   : {data['umur']}")
    print(GREEN + f"Alamat : {data['alamat']}")
    print(GREEN + f"Nomor  : {data['nomor']}")
    print(GREEN + f"Email  : {data['email']}")
    print(border(),"\n")

def tampilkan_riwayat():
    if not riwayat_biodata:
        print("belum ada riwayat biodata!!")
        return
    
    print(border())
    print(YELLOW + "RIWAYAT BIODATA".center(50) + RESET)
    print(border())

    for i, data in enumerate(riwayat_biodata, start=1):
        print(CYAN + f"\nData ke-{i}" + RESET)
        print(GREEN + f"Nama   : {data['nama']}")
        print(GREEN + f"Umur   : {data['umur']}")
        print(GREEN + f"Alamat : {data['alamat']}")
        print(GREEN + f"Nomor  : {data['nomor']}")
        print(GREEN + f"Email  : {data['email']}")
    print(f"\n{border()}")

def biodata():
    print(border())
    print(YELLOW + "DATA BIODATA".center(50) + RESET)
    print(border())

    for i, data in enumerate(riwayat_biodata, start=1):
        print(GREEN + f"\n{i}.{RESET} {data['nama']} - {data['alamat']} - {data['nomor']}")
    print(border())

def hapus_biodata():
    if not riwayat_biodata:
        print(RED + "tidak ada data yang tersedia!!" + RESET)
        return
    
    biodata()
    while True:
        hapus = input_angka("masukkan nomor data yang mau di hapus (0 for quit): ") - 1
        
        if 0 <= hapus < len(riwayat_biodata):
            riwayat_biodata.pop(hapus)
            print(GREEN + "data berhasil dihapus!\n" + RESET)
            break

        elif hapus == -1:
            print("tidak ada data yang dihapus!\n")
            break

        else:
            print(RED + "nomor tidak valid!\n" + RESET)

def edit_biodata():
    if not riwayat_biodata:
        print(RED + "tidak ada data yang tersedia!!" + RESET)
        return
    
    while True:
        biodata()
        pilih = input_angka("pilih nomor data yang mau di edit (0 for quit): ") - 1
        
        if pilih == -1:
            print("tidak ada data yang diedit!\n")
            break

        if not 0 <= pilih < len(riwayat_biodata):
            print(RED + "nomor tidak valid!\n" + RESET)
            continue
        
        data = riwayat_biodata[pilih]

        print("pilih field yang mau diedit:")
        fields = ["nama","umur","alamat","nomor","email"]
        for i ,field in enumerate(fields, start=1):
            print(f"{i}. {field}")

        while True:
            pilih_field = input_angka("pilih field: ") - 1
            if 0 <= pilih_field < len(fields):
                break
            print(RED + "field tidak valid" + RESET)

        field = fields[pilih_field]

        if field == "umur":
            data_baru = input_angka(f"masukkan data baru untuk {field}: ")
        elif field == "nomor":
            while True:
                data_baru = input(f"masukkan data baru untuk {field}: ").strip()
                if data_baru.isdigit():
                    break
                print(RED + "ERROR: nomor harus berupa angka!" + RESET)

        else:
            data_baru = input(f"masukkan data baru untuk {field}: ").strip()
        
        data[field] = data_baru
        print(GREEN + "data berhasil diupdate!" + RESET)

        while True:
            pengulangan = input("masih ada yang mau diedit? (y/n): ").lower().strip()
            if pengulangan in pengulang:
                break
        
        if pengulangan == "n":
            break

while ulang:
    print(border())
    print(YELLOW + "FUNGSI YANG TERSEDIA".center(50) + RESET)
    print(border())

    for i, item in enumerate(data_fungsi, start=1):
        print(f"{i}. {item}")
    while True:
        fungsi = input("masukkan fungsi : ").lower().strip()
        if fungsi not in data_fungsi:
            print(RED + "fungsi tidak tersedia! coba lagi!" + RESET)
        
        elif fungsi in data_fungsi:
            break

    if fungsi == "input":
        hasil = input_biodata()
        riwayat_biodata.append(hasil)
        tampilkan_biodata(hasil)

    elif fungsi == "show":
        tampilkan_riwayat()

    elif fungsi == "delete":
        hapus_biodata()

    elif fungsi == "edit":
        edit_biodata()

    elif fungsi == "quit":
        ulang = False