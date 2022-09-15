


Link app Heroku: https://tugas-2-pbp-majid.herokuapp.com/katalog/




![image](https://user-images.githubusercontent.com/112489540/190291065-78d3adc0-230d-4cf0-a569-017eaa5682a4.png)
image didapat dari https://www.theturninggear.com/2018/10/22/djangos-architectural-pattern/

Apakah kaitan antara urls.py, models.py, views.py, dan katalog.html? Saat seorang user ingin masuk ke salah satu website django anda, sebuah web server
menerima request itu dan akan kirimkan request itu ke django untuk dihandalkan mereka. Django lalu akan menggunakan urls.py yang ada untuk memutuskan view
mana yang akan digunakan. views.py akan lalu tarik models yang dari models.py dan membawanya ke template html yang ada, dalam skenario ini katalog.html.
katalog.html ini lalu akan didisplay di browser user itu.

Pertama kita buat sebuah fungsi di views.py untuk mengantarkan item katalog. Di urls.py, kita import path dari urls django dan fungsi tadi dan mengkonek fungsi
itu dengan path di urls django, dan juga berikan nama app. Lalu kita import models dari models.py dan assign sebuah variabel ke semua objects yang ada di models.
Berikan nama dan id dan masukkan kedua itu bersama variabel models ke dalam context. Kita lalu membuat fungsi views return context itu. Lalu pada template
HTML-nya, kita fill dengan isi context yang ada di views tadi. Akhirnya kita cek di localhost, dan jika semua sudah dalam order, add, commit, dan push.

Mengapa kita menggunakan virtual environment? Virtual environment ini membuat semacam simulasi dimana segala hal yang kita utak-atik pada file kita akan
terisolasi dan tidak tercampur-campur dengan file atau project lain. Sebenarnya kita bisa lakukan project kita tanpa virtual environment, tetapi akan
ada risiko mix-up dan mengacaukan project lain.

