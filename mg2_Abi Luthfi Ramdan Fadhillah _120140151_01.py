## Program untuk mengelola data buku dengan class.

#Nama   :Abi Luthfi Ramdan Fadhillah
#nim    :120140151
#kelas  : PBO RA

#membuat class Tokobuku
class Tokobuku :
    __list_buku = []
    #konstruktor
    def _init_(self) :
        self.__list_buku = [] # berisi nama, genre, penulis dan tahun
    
    #menu inputan
    def input_buku(self) :
        self.nama = input("Masukkan nama buku : ")
        self.genre = input("Masukkan genre buku : ")
        self.pengarang = input("Masukkan nama pengarang : ")
        self.tahun = input("Masukkan tahun terbit : ")

        #menampung data inputan dalam dictionary
        data_buku = {"nama": self.nama, "genre": self.genre, "pengarang": self.pengarang, "tahun": self.tahun}
        return data_buku
    
    #menambah daftar buku
    def tambah_buku(self,) :
        data_buku = self.input_buku()
        self.__list_buku.append(data_buku)

        if self.__list_buku :
            print("Data buku berhasil ditambahkan")

    #menampilkan daftar buku
    def tampil_buku(self) :
        if self.__list_buku :
            for i in self.__list_buku :
                print(i["nama"], "\t",i["genre"],"\t", i["pengarang"],"\t", i["tahun"])
        else :
            print("Data buku kosong")
    
    #mengupdate data buku
    def edit_buku(self) :
        if self.__list_buku :
            index = int(input("Masukkan nomor buku yang akan diedit : "))
            self.__list_buku[index-1] = self.input_buku()
        else :
            print("Data buku kosong")
    #menghapus data buku
    def hapus_buku(self) :
        if self.__list_buku :
            index = int(input("Masukkan nomor buku yang akan dihapus : "))
            del self.__list_buku[index]
        else :
            print("Data buku kosong")

#menu inputan jumlah data buku yang akan di tampung
n = int(input("Masukkan jumlah buku mula-mula : "))

tokobuku = Tokobuku()
while n > 0 :
    tokobuku.tambah_buku()
    n -= 1

ulang = 0
while ulang != 5 :
#menu pemilihan daftar buku
    print("1. Tambah data buku")
    print("2. Lihat list buku" )
    print("3. Modifikasi buku lama")
    print("4. Hapus buku lama")
    print("5. Keluar promgram")
    ulang = int(input("Masukan nomor input : "))

    if ulang == 1 :
        tokobuku.tambah_buku()
    elif ulang == 2 :
        tokobuku.tampil_buku()
    elif ulang == 3 :
        tokobuku.edit_buku()
    elif ulang == 4 :
        tokobuku.hapus_buku()
    elif ulang == 5 :
        print("Terima kasih telah menggunakan program ini")
    else :
        print("Pilihan tidak tersedia")