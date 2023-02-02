# APLIKASI MANAJEMEN TO-DO-LIST (DASH)
Nama: Muhammad Ali Pratama Putra

NIM: 5220411416

## Latar Belakang
Pada era digital saat ini, teknologi menjadi bagian yang tidak dapat dipisahkan dalam kehidupan sehari-hari. Salah satu teknologi yang sangat digemari adalah smartphone yang memungkinkan pengguna untuk melakukan berbagai aktivitas seperti browsing internet, berkomunikasi, hingga memanajemen aktivitas pekerjaan. Namun, masih banyak orang yang kesulitan dalam mengelola aktivitas pekerjaan mereka. Oleh karena itu, dalam mata kuliah Teknologi Berbasis Objek, saya dan kelompok ditugaskan untuk membuat rancangan aplikasi manajemen To-Do-List (DASH) yang dapat membantu pengguna dalam mengelola aktivitas pekerjaan mereka dengan mudah melalui smartphone. Laporan ini akan menjelaskan hasil ujian akhir semester kami yang meliputi proses perancangan GUI(Graphical User Interface) aplikasi, pembuatan class diagram, hingga hasil sederhana aplikasi yang kami buat dengan menggunakan paradigma OOP(Object Oriented Programming) di bahasa pemrograman Python. Nama DASH sendiri, merupakan akronim dari Daily Assisted Task for Human.

## Rumusan Masalah
Rumusan masalah dari kasus ini adalah bagaimana membuat aplikasi manajemen To-Do-List (DASH) yang dapat membantu pengguna dalam mengelola aktivitas pekerjaan dengan mudah melalui smartphone. Dalam proses pembuatan rancangan aplikasi ini, saya dan kelompok harus memperhatikan berbagai aspek seperti desain aplikasi yang user friendly, fitur yang dibutuhkan oleh pengguna, serta keamanan dan performa aplikasi. Selain itu, kami juga harus melakukan pengujian terhadap rancangan aplikasi yang kami buat untuk mengetahui apakah rancangan aplikasi tersebut dapat digunakan dengan baik dan dapat memenuhi kebutuhan pengguna. Oleh karena itu, dalam laporan ini saya akan memberikan solusi untuk mengatasi masalah yang dihadapi dalam proses pembuatan aplikasi dan juga menunjukkan hasil yang diperoleh dari aplikasi yang kami buat.

## Tujuan
Tujuan dari laporan ini adalah untuk menghasilkan rancangan aplikasi manajemen To-Do-List (DASH) yang dapat mempermudah pengguna dalam mengelola aktivitas pekerjaan melalui smartphone. Selain itu, laporan ini juga bertujuan untuk mengevaluasi kinerja dari aplikasi yang dibuat, menganalisis kebutuhan pengguna dan memberikan solusi atas masalah yang mungkin dihadapi dalam pembuatan aplikasi. Tujuan lainnya adalah memberikan saran untuk perbaikan dan pengembangan aplikasi di masa depan. Dengan demikian, laporan ini dapat digunakan sebagai referensi dalam pengembangan aplikasi manajemen To-Do-List (DASH) yang lebih baik.

## Class Diagram
Dalam tahap pembuatan UML class diagram, saya menggunakan pendekatan objek user dan beberapa database seperti database akun, task, dan kategori. Pertama, saya mengidentifikasi objek-objek yang digunakan dalam aplikasi, seperti user, task, dan kategori. Kemudian, saya menentukan atribut-atribut yang dimiliki oleh masing-masing objek tersebut. Setelah itu, saya menentukan relasi antar objek dan bagaimana objek-objek tersebut saling terkait satu sama lain. Langkah selanjutnya, saya menggambar diagram UML class untuk mewakili objek-objek dan relasi yang telah ditentukan sebelumnya. Dengan menggunakan UML class diagram dan use case diagram yang saya lampirkan pada laporan sebelumnya, saya dapat menyajikan struktur aplikasi secara jelas dan mudah dipahami oleh tim pengembangan. Berikut merupakan hasil rancangan class diagram saya:

![](https://i.ibb.co/9tc3Cxr/a.png)

Keterangan:

- Class Database memiliki 3 cabang anakan (interheritance) yaitu db_task, db_account, dan db_categories, sehingga atribut dan operasi dari parent dapat digunakan.

- Setiap operasi tambah_data() urutan pada masing-masing database akan bertambah nilai 1 (integer).

- Class User memiliki relasi non-class kepada Class db_account menggunakan operasi modular.

- Implementasi lebih jelas dapat dilihat pada source code.

# Implementasi
Dalam tahap implementasi class diagram ke pemrograman sederhana Python, saya mengimplementasikan class diagram yang telah dibuat sebelumnya dan membuat interaksi sederhana pada terminal. Pertama, saya mengubah diagram class menjadi kode Python dengan membuat class-class yang sesuai dengan objek yang digambarkan pada diagram dan menentukan atribut dan method yang sesuai. Kemudian, saya mengimplementasikan interaksi yang sederhana pada terminal, seperti input dan output, dan mengimplementasikan fitur-fitur yang telah ditentukan pada rancangan GUI. Fitur-fitur pada rancangan GUI dapat dilihat secara sederhana melalui Command Line Interface (CLI) yang telah dibuat. Dengan mengimplementasikan class diagram ke dalam kode Python, saya dapat mengubah rancangan aplikasi menjadi kode yang dapat dijalankan dan memudahkan proses pengembangan aplikasi.

# Mockup & Prototype (Figma)
[klik link disini](https://www.figma.com/proto/kIHgFN461hM7wabDvcWmut/Tugas-Kelompok-TBO-w11)
