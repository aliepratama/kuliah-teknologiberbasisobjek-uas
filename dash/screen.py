"""
+ ------------------------------------------------ +
|  Nama Lengkap    : Muhammad Ali Pratama Putra    |
|  NIM             : 5220411416                    |
|  Prodi           : Informatika                   |
+ ------------------------------------------------ +
"""

import time
import os
import questionary
import rich
from rich.console import Console
from rich.progress import track
from rich.panel import Panel
from rich.table import Table

console = Console(width = 90)

def menu_01():
    os.system('cls')
    console.print('Selamat Datang', style='#af1d1e blink bold', justify='center')
    console.print('Selamat Datang di Aplikasi DASH', justify='center')
    print('')
def menu_02():
    email = questionary.text("Masukkan Email Anda").ask()
    passwd = questionary.password("Masukkan Password Anda").ask()
    print('')
    return [email, passwd]
def pilihan_01_01():
    pilihan = ('🚗 Masuk','📖 Registrasi','❌ Keluar')
    choise = pilihan.index(questionary.select(
        'Ada yang bisa kami bantu? 👋',
        choices=pilihan
    ).ask())
    return choise
def menu_03():
    nama = questionary.text("Masukkan Nama Lengkap Anda").ask()
    email = questionary.text("Masukkan Email").ask()
    pass1 = questionary.password("Masukkan Password").ask()
    pass2 = questionary.password("Masukkan Konfirmasi Password").ask()
    print('')
    if pass1 != pass2:
        console.print('Gagal', style='#af1d1e blink bold')
    else:
        return [nama, email, pass1]
def menu_04(nama_lengkap: str):
    os.system('cls')
    console.print(f'Selamat Datang {nama_lengkap}', style='#af1d1e blink bold', justify='center')
    print('')
    pilihan = ('❌ Keluar', '📥 Buat Task','📖 Lihat Task', '🖋 Edit Task', '🗑 Hapus Task', '🔖 Ubah Status')
    choise = pilihan.index(questionary.select(
        'Silahkan pilih menu',
        choices=pilihan
    ).ask())
    return choise
def menu_05(kategori: list):
    os.system('cls')
    console.print('Buat Task Baru', style='#af1d1e blink bold', justify='center')
    print('')
    nama = questionary.text("Masukkan Nama Task").ask()
    deadline = int(questionary.text("Deadline berapa hari ke depan?").ask())
    pilihan = [i for i in kategori]
    jawaban = [i[1] for i in kategori]
    id_kategori = pilihan[jawaban.index(questionary.select(
        'Silahkan pilih kategori',
        choices=jawaban
    ).ask())][0]
    return (nama, deadline, id_kategori + 1)
def menu_06(data: list, db_category:list, back_button: bool = True):
    os.system('cls')
    id_category = [i[0] for i in db_category]
    table = Table(title="Riwayat Seluruh Transaksi")
    table.add_column("ID", style="cyan", no_wrap=True, width=5)
    table.add_column("Nama Task", style="magenta", no_wrap=True)
    table.add_column("Tanggal", style="green", no_wrap=True)
    table.add_column("Deadline", style="cyan", no_wrap=True)
    table.add_column("ID Kategori", style="magenta", no_wrap=True)
    table.add_column("Status", style="green", no_wrap=True, width=10)
    for i in data:
        table.add_row(str(i[0]), str(i[1]), str(i[2]), str(i[3]), str(db_category[id_category.index(int(i[4]))][1]), str('Selesai' if i[5] == True else 'Belum'))
    console.print(table, justify="center")
    print('')
    if back_button:
        questionary.select('',choices=['⬅ Kembali']).ask()
def menu_07(kategori: list):
    id_task = int(questionary.text("Silahkan masukkan id task").ask())
    nama = questionary.text("Masukkan Nama Task").ask()
    deadline = int(questionary.text("Deadline berapa hari ke depan?").ask())
    pilihan = [i for i in kategori]
    jawaban = [i[1] for i in kategori]
    id_kategori = pilihan[jawaban.index(questionary.select(
        'Silahkan pilih kategori',
        choices=jawaban
    ).ask())][0]
    return [id_task, nama, deadline, id_kategori + 1]
def menu_08():
    return int(questionary.text("Silahkan masukkan id task").ask())
def menu_09():
    pilihan_id = int(questionary.text("Silahkan masukkan id task").ask())
    status = questionary.select(
        'Silahkan ubah status',
        choices=['Selesai', 'Belum']
    ).ask()
    if status == 'Selesai':
        return (pilihan_id, True)
    else:
        return (pilihan_id, False)
def login_load():
    for i in track(range(20), description="Autentikasi Akun..."):
        time.sleep(0.075)
def register_load():
    for i in track(range(20), description="Membuat Akun..."):
        time.sleep(0.075)
def save_load():
    for i in track(range(20), description="Menyimpan Data..."):
        time.sleep(0.075)
def bool_alert(bool: bool, anchor = True):
    if anchor == bool:
        console.print('Berhasil', style='#673ab7 blink bold')
    else:
        console.print('Gagal', style='#af1d1e blink bold')
def delay(seconds: int):
    time.sleep(seconds)