print(3*'=','tugas pertemuan 9','='*3)
print('| Nama\t: Devi Rahmania\t|\n| NIM\t: 312110206\t|\n| Kelas\t: TI.21.C5\t|')
print(25*'=','\n')
a = [2, 4, 6, 8, 10]                                                        #buat list sebanyak 5 elemen
print(" a = [2, 4, 6, 8, 10 ]\n")          

print(3*'=','akses',3*'=') 
print('elemen ke 3 adalah', a[2])                                           # tampilkan elemen ke 3 ,
del a[1:4]                                                                  # ambil elemen ke 2-4
print('setelah elemen 2 sampai 4 diambil maka menjadi',a)                                                              
del a[1]                                                                    # ambil elemen terakhir
print('setelah elemen terakhir diambil maka menjadi',a,"\n")                                                              

print(3*'=','ubah',3*'=')                                                      
a = [2, 4, 6, 8, 10]                                                        
a [3] =  9                                                                  #ubah elemen ke 4 dengan nilainya , 
print('setelah merubah elemen ke-4 maka menjadi', a)
a [3:5] = 12, 14                                                              #ubah elemen ke 4- terakhir
print('setelah merubah elemen ke-4 sampai terakhir maka menjadi', a,'\n')
print(3*'=','tambah',3*'=')
a = [2, 4, 6, 8, 10] 
b = []
b.extend (a[0:2])                                                           #ambil 2 bagian dari list pertama (a) dan jadikan list ke 2 B
print ('hasil setelah mengambil 2 bagian elemen a maka b=', b)
b.append('enam')                                                         #- tambah list b dengan nilai string
print('setelah menambah string pada elemen b hasilnya', b)
b.extend([8, 10, 12])                                                       #- tambah list b dengan 3 nilai
print('setelah menambah 3 nilai menjadi', b)
c=a+b                                                                       #- gabungkan list b dan list a
print('hasil penggabungan list a dan b hasilnya',c)