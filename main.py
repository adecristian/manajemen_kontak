"Program Manajemen Kontak"

def membuka_kontak(path='kontak.txt'):
    with open(path, mode='r') as file:
        kontak = file.readlines()
    return kontak

def menyimpan_kontak(path='kontak.txt', isi=[]):
    with open(path, mode='w') as file:
        file.writelines(isi)


class Kontak:
    def __init__(self):
        # self.kontak = []
        self.kontak = membuka_kontak()


    def melihat_kontak(self):
        # melihat semua kontak
        # pass
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                # print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
                print(f'{num}. ' + item)
        else:
            print("Kontak masih kosong")
            return 1

    def menambah_kontak(self):
        nama = input("Masukkan Nama Kontak yang baru: ")
        HP = input("Masukkan No HP Kontak yang baru: ")
        email = input("Masukkan email Kontak yang baru: ")
        # kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
        # self.kontak.append(kontak_baru)

        kontak_baru = f'{nama} ({HP}, {email})' + '\n'
        self.kontak.append(kontak_baru)

        print("Kontak baru berhasil ditambahkan!")

    def menghapus_kontak(self):
        # print("\n")
        # if kontak:
        #     for num, item in enumerate(kontak, start=1):
        #         print(f'{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        # else:
        #     print("Kontak masih kosong")
        #     continue
        if self.melihat_kontak() == 1 :
            return
        else:
            try:
                i_hapus = int(input("Masukkan nomor Kontak yang akan dihapus: "))
                del self.kontak[i_hapus - 1]
                print("Kontak yang dimaksud berhasil dihapus!")
            except:
                print("Input yang Anda masukkan salah!")


    def keluar_kontak(self):
        menyimpan_kontak(isi=self.kontak)

# kontak1 = {'nama' : 'Andi', 'HP' : '0812235444', 'email' : 'andi@python.com'}
# kontak2 = {'nama' : 'Ani', 'HP' : '0817654321', 'email' : 'ani@python.com'}
# kontak = [kontak1, kontak2]

kontak_kantor = Kontak()
kontak_keluarga = Kontak()


while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("Masukkan pilihan menu Kontak (1,2,3 atau 4): ")

    if pilihan == '1':
        kontak_kantor.melihat_kontak()

    elif pilihan == '2':
        # menambahkan kontak
        # pass
        kontak_kantor.menambah_kontak()

    elif pilihan == '3':
        # menghapus kontak
        # pass
        kontak_kantor.menghapus_kontak()

    elif pilihan == '4':
        # keluar dari kontak
        kontak_kantor.keluar_kontak()
        break
    else:
        print("Anda memasukkan pilihan yang salah!")
