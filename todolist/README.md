Link app Heroku: https://tugas-2-pbp-majid.herokuapp.com/todolist/


Apa kegunaan {% csrf_token %} pada elemen <form>?
  CSRF adalah sebuah serangan yang membuat user mengirimkan suatu request (permintaan) kepada suatu aplikasi, meskipun user itu tidak melakukan apapun.
  Django memiliki tag {% csrf_token %}. Ia akan generate sebuah token di sisi server saat rendering page tersebut. Lalu ia akan cross-check request-request
  yang masuk menggunakan token ini. Jika request tidak memiliki token ini, request itu tidak di-execute.
  
 
Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})?
  Bisa. Programmer dapat membuat forms.py secara manual dan export ke views.py. Di views, dapat dibuat sebuah fungsi akan meng-assign sebuah variabel 
  ke Class yang ada di form.s.py. Di dalam if form.is_valid():, masukkan form.cleaned_data[variabel di forms.py] ke dalam models yang akan dikirim ke
  berkas .html. 
  
Proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form?
  Saat user memasuki todolist, user kaan dibawa ke login page karena show_todolist bersifat @login_required. Jika user belum memiliki akun, link Buat Akun
  akan membawa user ke register.html. Saat user submit data di form, data itu akan disave dan user kembali ke login page. User akhirnya bisa login.
  Saat user ingin menambah task, user akan dibawa ke add_task.html, dimana user akan diminta data untuk disubmit ke form. Data itu lalu akan disave dan
  langsung didisplay di show_todolist.
  
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas?
  Pembuatan app django dan implementasi MVT secara garis besar sama seeprti tugas 2. Bedanya sekarang kita harus menambahkan elemen form ke html kita.
  Di views.py, dibuat 4 buat fungsi baru untuk melakukan register akun, login, logout, dan membuat task (beserta merestriksi show_todolist). Lalu, kita
  membuat berkas .html untuk register, login, dan add_task, sementara logout merupakan modifikasi yang dilakukan di todolist.html. Berkas .html ini
  bertugas untuk mengdisplay halaman register, login, logout masing-masing. Tentu juga perlu ditambahkan urls di urls.py. Dibuatlah juga buttons-buttons
  dalam berkas .html agar user dapat bisa balik lagi ke halaman yang sesuai setelah selesai. Lalu dalam models.py, model user menggunakan 
  models.ForeignKey agar halaman utama dapat mengdisplay.
