"""
+ ------------------------------------------------ +
|  Nama Lengkap    : Muhammad Ali Pratama Putra    |
|  NIM             : 5220411416                    |
|  Prodi           : Informatika                   |
+ ------------------------------------------------ +
"""

import datetime
class Database():
    def __init__(self, host: str, user: str, passwd: str, db: str):
        self.host = host
        self.user = user
        self.passwd =passwd
        self.db = db
        self.nama_tabel = ''
    def name_tabel(self, nama: str):
        self.nama_tabel = nama
    def create(self, kolom: list, value: str):
        if len(kolom) == len(value):
            for i in range(len(kolom)):
                kolom[i].append(value[i])
    def read(self, kolom: list):
        if len(kolom) > 0:
            return [tuple(x) for x in zip(*kolom)]
        else:
            return None
    def update(self, kolom: list, value: list, index: int):
        for i in range(len(kolom)):
            kolom[i][index] = value[i]
    def delete(self, kolom: list, index:int):
        for i in range(len(kolom)):
            kolom[i].pop(index)

class Db_task(Database):
    def __init__(self, host: str, user: str, passwd: str, db: str):
        super().__init__(host, user, passwd, db)
        self.urutan = 0
        self.id = []
        self.nama_task = []
        self.tanggal = []
        self.deadline = []
        self.status = []
        self.id_kategori = []
    def timestamp(self, rentang_hari: int = 0):
        return str(datetime.datetime.now() + datetime.timedelta(rentang_hari))
    def ubah_status(self, id: int, status: bool):
        try:
            self.status[self.id.index(id)] = status
        except:
            pass
    def tambah_task(self, nama_task: str, tanggal: str, deadline: str, id_kategori: int):
        self.urutan += 1
        self.id.append(self.urutan)
        self.nama_task.append(nama_task)
        self.tanggal.append(tanggal)
        self.deadline.append(deadline)
        self.id_kategori.append(id_kategori)
        self.status.append(False)

class Db_account(Database):
    def __init__(self, host: str, user: str, passwd: str, db: str):
        super().__init__(host, user, passwd, db)
        self.urutan = 0
        self.id = []
        self.nama_akun = []
        self.email = []
        self._passwd = []
    def tambah_akun(self, nama_lengkap: str, email: str, passwd: str):
        self.urutan += 1
        self.id.append(self.urutan)
        self.nama_akun.append(nama_lengkap)
        self.email.append(email)
        self._passwd.append(passwd)
    def show_password(self):
        return self._passwd

class Db_categories(Database):
    def __init__(self, host: str, user: str, passwd: str, db: str):
        super().__init__(host, user, passwd, db)
        self.urutan = 0
        self.id = []
        self.nama_kategori = []
    def tambah_kategori(self, nama_kategori: str):
        self.urutan += 1
        self.id.append(self.urutan)
        self.nama_kategori.append(nama_kategori)

class User():
    def __init__(self, nama_lengkap: str, email: str, password: str, db_akun: object):
        self.nama_lengkap = nama_lengkap
        self.email = email
        self.__password = password
        self.session = False
        db_akun.tambah_akun(self.nama_lengkap, self.email, self.__password)
    def show_password(self):
        return self.__password

def auth_account(email_input: str, passwd_input: str, db_akun: object):
     return email_input in db_akun.email and passwd_input in db_akun.show_password()
