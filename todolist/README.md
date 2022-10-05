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

  
  ==================================================================================================================================================================
  
  
Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Secara singkat, Inline style CSS menerapkan properti style CSS di dalam elemen tag secara langsung. Sehingga, tidak dibutuhkan pembuatan tag style pada bagian        kepala HTML. Internal style memuatkan properti styling pada kepala HTML dan assign properti itu ke sebuah selector. Lalu menggunakan tag div, user dapat customize bagian spesifik itu berdasarkan style yang berada di bagian kepala tadi. Pada external style, seluruh hal styling dilakukan di file yang berbeda. Di bagian kepala HTML, diberi tag link untuk mengasih reference styling ke HTML tersebut. Bagian body dicustomize menggunakan tag div
  
Jelaskan tag HTML5 yang kamu ketahui?
!DOCTYPE html: tipe dokumen adalah HTML
head: kepala dari HTML, berisi metadata dokumen
body: berisi hal-hal yang akan ditampilkan dalam dokumen HTML-nya
style: berisi styling css untuk mengcustomize dokumen
div: membagikan bagian body dokumen menjaid berbagai divisi. Membantu dalam customization
br: Single line break
h#: header text. text lebih besar
p: paragraf
dan lain-lain
  
Jelaskan tipe-tipe CSS selector yang kamu ketahui?
1. Element Selector: Menggunakan elemen HTML seperti h1, h2, p sebagai selector untuk mengcustomize body dokumen HTML
2. ID Selector: Menggunakan ID sebagai selector. ID bersiat unik sehingga elemen tanpa ID tidak akan terpengaruh.
3. Class Selector: Mix dari Element dan ID Selector. Dapat mengcustomize tampilan dengan menambahkan "class=" walaupun beda elemen.
  
