"""
+ ------------------------------------------------ +
|  Nama Lengkap    : Muhammad Ali Pratama Putra    |
|  NIM             : 5220411416                    |
|  Prodi           : Informatika                   |
+ ------------------------------------------------ +
"""

from dash import system
from dash import screen as sc
import os

db_akun = system.Db_account('localhost', 'root', '', 'db_dash')
db_aktivitas = system.Db_task('localhost', 'root', '', 'db_dash')
db_kategori = system.Db_categories('localhost', 'root', '', 'db_dash')
kategori = ('Biasa', 'Penting', 'Urgent')
[db_kategori.tambah_kategori(i) for i in kategori]
    
def login():
    data = sc.menu_02()
    auth = system.auth_account(data[0], data[1], db_akun)
    sc.login_load()
    sc.bool_alert(True, auth)
    sc.delay(3)
    return auth
def register():
    global user
    data = sc.menu_03()
    user = system.User(data[0], data[1], data[2], db_akun)
    sc.register_load()
    sc.bool_alert(True)
    sc.delay(3)
def buat_task():
    kategori = db_kategori.read([db_kategori.id, db_kategori.nama_kategori])
    data = sc.menu_05(kategori)
    db_aktivitas.tambah_task(data[0], db_aktivitas.timestamp(), db_aktivitas.timestamp(data[1]), data[2])
    sc.save_load()
    sc.bool_alert(True)
    sc.delay(3)
def read_task():
    data = db_aktivitas.read([db_aktivitas.id, db_aktivitas.nama_task, db_aktivitas.tanggal, db_aktivitas.deadline, db_aktivitas.id_kategori, db_aktivitas.status])
    sc.menu_06(data, db_kategori.read([db_kategori.id, db_kategori.nama_kategori]))
def edit_task():
    os.system('cls')
    data = db_aktivitas.read([db_aktivitas.id, db_aktivitas.nama_task, db_aktivitas.tanggal, db_aktivitas.deadline, db_aktivitas.id_kategori, db_aktivitas.status])
    kategori = db_kategori.read([db_kategori.id, db_kategori.nama_kategori])
    sc.menu_06(data, db_kategori.read([db_kategori.id, db_kategori.nama_kategori]), False)
    pilihan = sc.menu_07(kategori)
    db_aktivitas.update([db_aktivitas.nama_task, db_aktivitas.deadline, db_aktivitas.id_kategori], [pilihan[1], db_aktivitas.timestamp(pilihan[2]), pilihan[3]], db_aktivitas.id.index(int(pilihan[0])))
    sc.save_load()
    sc.bool_alert(True)
    sc.delay(3)
def delete_task():
    os.system('cls')
    data = db_aktivitas.read([db_aktivitas.id, db_aktivitas.nama_task, db_aktivitas.tanggal, 
                              db_aktivitas.deadline, db_aktivitas.id_kategori, db_aktivitas.status])
    sc.menu_06(data, db_kategori.read([db_kategori.id, db_kategori.nama_kategori]), False)
    pilihan_hapus = sc.menu_08()
    db_aktivitas.delete([db_aktivitas.id, db_aktivitas.nama_task, db_aktivitas.tanggal, db_aktivitas.deadline, db_aktivitas.status, db_aktivitas.id_kategori], db_aktivitas.id.index(int(pilihan_hapus)))
    sc.save_load()
    sc.bool_alert(True)
    sc.delay(3)
def ubah_status():
    os.system('cls')
    data = db_aktivitas.read([db_aktivitas.id, db_aktivitas.nama_task, db_aktivitas.tanggal, 
                              db_aktivitas.deadline, db_aktivitas.id_kategori, db_aktivitas.status])
    sc.menu_06(data, db_kategori.read([db_kategori.id, db_kategori.nama_kategori]), False)
    data_status = sc.menu_09()
    db_aktivitas.ubah_status(int(data_status[0]), data_status[1])
    sc.save_load()
    sc.bool_alert(True)
    sc.delay(3)
def dashboard():
    while True:
        pilihan = sc.menu_04(user.nama_lengkap)
        if pilihan == 0:
            break
        elif pilihan == 1:
            buat_task()
        elif pilihan == 2:
            read_task()
        elif pilihan == 3:
            edit_task()
        elif pilihan == 4:
            delete_task()
        elif pilihan == 5:
            ubah_status()
def menu():
    global db_akun
    sc.menu_01()
    pilihan = sc.pilihan_01_01()
    if pilihan == 0:
        login_result = login()
        if login_result:
            dashboard()
        else:
            menu()
    elif pilihan == 1:
        register()
        menu()
menu()