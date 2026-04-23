#import file/class
from mobil import Mobil
# import mobil

#Tipe Data
a = 10 #integer
b = 1.5 #float
c = "test" #string
d = True #boolean

#variabel
firstName = "Gibran"
lastName = "Syah"

#menampilkan output
print(firstName)
print(lastName)

#percabangan (if)
umur = 18
if umur >= 18 :
    print("dewasa")
else :
    print("masih kecil")

x = 1
match x :
    case 1 :
        print("Satu")
    case 2 :
        print("Dua")
    case _ :
        print("Kosong")

#perulangan (loop)
for i in range(5) :
    print(i)

z = 0 
while z < 5 :
    print(z)
    z += 1

nama = input("Masukan nama : ")
print("Halo ", nama)

#operasi matematika
e = 10
f = 3
print(e + f)
print(e - f)
print(e * f)
print(e / f)

#fungsi
def sapa(nama) :
    print("Halo", nama)

sapa("Andi")

#list (array sederhana)
buah = ["apel", "mangga", "jeruk"]
print(buah[0])

#Dictionary (key-value)
data = {"nama" : "Budi", "umur" : 20}
print(data["nama"])

#error handling
v = str("teks")
try :
    v + 12
except TypeError :
    print("tidak bisa gabungkan string dan angka")
except ValueError :
    print("input harus angka")
except : 
    print("error")
finally :
    print("finish")

#OOP
objek = Mobil("Honda")
objek.klakson()
print(objek.merk)