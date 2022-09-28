Link Heroku Apps:
HTML - https://tugas-2-pbp-majid.herokuapp.com/mywatchlist/html/
XML - https://tugas-2-pbp-majid.herokuapp.com/mywatchlist/xml/
JSON - https://tugas-2-pbp-majid.herokuapp.com/mywatchlist/json/

Postman screenshots:
HTML: ![image](https://user-images.githubusercontent.com/112489540/191636852-24341d19-26d4-44f2-aa94-61422088205e.png)

XML: ![image](https://user-images.githubusercontent.com/112489540/191636932-ed76a21d-69ef-4598-b3c5-1ff032baf886.png)

JSON: ![image](https://user-images.githubusercontent.com/112489540/191637003-79285df1-42e9-4550-b227-83a06a597c27.png)


Perbedaan antara JSON, XML, dan HTML:
    Dalam rendering sebuah dokumen, tiga masalah utama yang dihadapi adalah bagaimana bisa menformat dokumennya, bagaimana menstruktur dokumennya, dan 
bagaimana menyajikan konten. HTML berupaya mengatasi masalah tersebut dengan menggunakan serangkaian tags untuk membentuk sebuah format dan
ditampilkan di website secara rapih. Namun, aturan yang longgar dalam HTML belum menyelesaikan masalah struktur konten. Dari sini, XML dapat menyimpan
elemen-elemen data secara terstruktur. XML akan mengstrukturkan datanya yang nanti akan ditampilkan melalui formatting HTML. JSON tiba karena dengan 
berkembangnya web application, ada peningkatan permintaan untuk web apps mengdisplay informasi secara dinamis. JSON juga mempunyai advantage didevelop 
menggunakan bahasa javascript. JSON menampilkan datanya secara efisien, sedangkan XML menampilkan datanya secara terstruktur.

Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Pengiriman data dapat bermacam-macam rupanya. Bisa berupa sebuah catatan, susunan heading dan body pada suatu website, dan lainnya. Agar transisi
pengiriman data ini lebih mudah, diperlukan formatting data seperti HTML, XML, dan JSON.

Bagaimana cara kamu mengimplementasikan checklist di atas?
    Seperti di tugas 2, Pertama kita buat sebuah fungsi di views.py untuk mengantarkan item dan juga fungsi yang mengreturn sebuah HttpResponse. 
Di urls.py, routing yang dilakukan tidak hanya ke dalam bentuk html, tetapi juga tambahkan path untk xml dan json. Lalu kita import models dari models.py 
dan assign sebuah variabel ke semua objects yang ada di models.
    Berikan nama dan id dan masukkan kedua itu bersama variabel models ke dalam context. Kita lalu membuat fungsi views return context itu. Lalu pada template
HTML-nya, kita fill dengan isi context yang ada di views tadi. Pada link localhost, di akhir dapat ditambahkan html/, xml/, atau json/ tergantung dengan
format yang ingin user lihat.
