---
title: Catatan Mingguan Eksperimen Vibe Coding Android Membangun SHL Quran Pro dan Qodho Reminder dari Google AI Studio sampai Lolos Ujian Closed Testing
draft: false
sticky: false
tocNumbering: true
excludeFromSummary: false
math: false
quiz: false
date: 2026-09-03 18:00:00
updated: 2026-09-03 18:00:00
categories:
  - [Weekly]
tags:
  - weekly log
  - android development
  - shl quran pro
  - qodho reminder
  - vibe coding
  - google ai studio
  - hermes agent
  - android studio
  - closed testing
  - changelog
  - bug hunting
  - kotlin compose
  - app widget
  - shl project
description: Catatan mingguan super lengkap dan santai seputar perjalanan eksperimen vibe coding Android modern. Mengupas tuntas kolaborasi Google AI Studio, Hermes, dan Android Studio dalam meracik SHL Quran Pro dan Qodho Reminder, validitas data mushaf, logika matematika runway ibadah, arsitektur widget obsidian gold, drama perburuan bug memori, riwayat changelog versi, hingga suka duka menembus ujian 20 tester 14 hari di Google Play Console.
cover: https://img.shlproject.com/2026/09/108d1afdd78d0ca5814d6f8591721686.webp
link: weekly/Catatan-Mingguan-Eksperimen-Vibe-Coding-Android-Membangun-SHL-Quran-Pro-dan-Qodho-Reminder
---
![](https://img.shlproject.com/2026/09/108d1afdd78d0ca5814d6f8591721686.webp)
Halo, selamat datang di pojok paling santai dari seluruh blog ini. Kalau kamu baru pertama kali mampir ke halaman Weekly, izinkan saya kenalkan dulu ya. Ini bukan artikel tutorial yang kaku dan penuh jargon teknis. Ini bukan paper akademis yang harus pakai bahasa formal dan kutipan jurnal. Ini ruang catatan pribadi saya, tempat saya nulis apa pun yang ada di kepala, dari curhat soal bug yang bikin frustasi sampai cerita kebahagiaan kecil waktu akhirnya sebuah fitur jalan sempurna di HP jadul. Anggap saja kita lagi ngobrol bareng di warung kopi tengah malam, laptopnya masih nyala, dan kopi sachet ketiga baru saja dituang. Kali ini, saya mau cerita panjang lebar tentang perjalanan saya bereksperimen dengan vibe coding untuk membangun dua aplikasi Android yang sangat personal buat saya, yaitu SHL Quran Pro dan Qodho Reminder. Ceritanya panjang, detailnya banyak, dan insya Allah bermanfaat buat siapa pun yang lagi penasaran soal bagaimana AI bisa jadi partner ngoding yang serius.

## Filosofi Ruang Santai Weekly Tempat Curhat Tanpa Batas

Kenapa saya bikin halaman Weekly ini? Jawabannya sederhana. Saya butuh tempat untuk menulis tanpa tekanan. Kalau di artikel utama blog, saya merasa harus menyusun semuanya rapi, terstruktur, penuh referensi, dan punya value yang jelas buat pembaca. Itu penting, dan saya tetap melakukannya. Tapi ada sisi lain dari proses kreatif yang sering hilang dalam artikel-artikel seperti itu, yaitu cerita di balik layar. Bagaimana rasanya begadang sampai subuh cuma buat debugging satu baris kode yang ternyata masalahnya sepele. Bagaimana rasanya menemukan solusi elegan yang bikin kamu senyum-senyum sendiri di depan monitor. Bagaimana rasanya merasa bodoh karena error yang sudah kamu cari dua hari ternyata hanya kurang satu titik koma, eh, ini Kotlin, titik koma nggak wajib, tapi kamu paham maksudnya.

Weekly ini adalah ruang santai tanpa batas. Di sini saya bisa curhat tentang betapa menyebalkannya Gradle Sync yang tiba-tiba gagal tanpa alasan jelas. Di sini saya bisa bercerita tentang betapa senangnya waktu pertama kali melihat widget Al-Quran dengan tema obsidian gold tampil cantik di home screen Samsung Galaxy A15. Di sini saya bisa berbagi tentang proses berpikir saya, keputusan desain yang saya ambil, kesalahan yang saya buat, dan pelajaran yang saya petik. Semua ditulis dengan gaya personal, tanpa filter formalitas, persis seperti kalau saya lagi cerita ke teman dekat.

Ada satu hal yang mungkin terdengar agak filosofis, tapi jujur ini yang saya rasakan. Buat saya, menulis kode itu mirip seni kaligrafi. Serius. Ketika kamu menulis sebuah fungsi Kotlin yang bersih, penamaan variabelnya jelas, logikanya mengalir natural dari atas ke bawah, dan setiap baris punya tujuan, ada keindahan di situ. Mungkin nggak semua orang bisa melihatnya, tapi buat yang sudah terbiasa, membaca kode yang ditulis dengan baik itu seperti membaca puisi. Dan kalau bicara konteks aplikasi Al-Quran, ada dimensi spiritual yang nggak bisa saya abaikan. Setiap kali saya menulis logika untuk merender ayat-ayat suci dengan benar, untuk memastikan setiap harakat tidak bergeser satu pixel pun dari posisinya, untuk menjaga integritas setiap huruf Arab dari Al-Fatihah sampai An-Nas, saya merasa sedang melakukan ibadah. Bukan cuma kerjaan teknis biasa. Ada rasa tanggung jawab yang berbeda.

Saya ingat satu malam di bulan Juli 2026. Saat itu sudah lewat tengah malam, mungkin sekitar jam dua dini hari. Rumah sepi. Yang terdengar cuma suara kipas laptop dan sesekali notifikasi Telegram masuk dari grup developer yang isinya sama-sama begadang. Saya sedang mengerjakan fitur tajweed color di SHL Quran Pro. Masalahnya waktu itu, metadata warna tajweed yang saya punya menggunakan character range indexing, artinya setiap aturan tajweed seperti ikhfa, idgham, iqlab, dan lainnya ditandai dengan posisi karakter awal dan akhir dalam string ayat. Tantangannya, posisi karakter ini harus presisi di level Unicode. Satu salah hitung, dan warna tajweed bisa menandai huruf yang salah. Bayangkan kalau huruf yang harusnya diwarnai merah sebagai tanda qalqalah malah geser ke huruf sebelahnya. Itu bukan cuma bug teknis biasa, itu menyangkut kebenaran ilmu tajweed.

Malam itu saya bolak-balik antara terminal, editor, dan emulator. Debug, test, salah lagi, perbaiki, test lagi. Rasanya seperti mengerjakan teka-teki yang potongannya terus berubah bentuk. Tapi ketika akhirnya berhasil, ketika semua warna tajweed muncul tepat di huruf yang benar dari awal sampai akhir ayat, ada perasaan yang sulit digambarkan. Bukan cuma puas. Ada rasa syukur. Ada rasa lega. Dan ada secangkir kopi yang sudah dingin di meja yang baru saya ingat belum diminum. Momen-momen seperti itulah yang ingin saya dokumentasikan di halaman Weekly ini. Bukan cuma hasilnya, tapi prosesnya. Bukan cuma fitur jadinya, tapi keringat di baliknya.

Dan kenapa formatnya catatan mingguan? Karena pengembangan aplikasi itu proses yang terus berjalan. Setiap minggu ada kemajuan baru, ada bug baru, ada ide baru, ada frustrasi baru, dan ada kemenangan kecil baru. Kalau saya tunggu sampai semuanya sempurna baru ditulis, maka artikel ini nggak akan pernah terbit. Jadi saya putuskan untuk mendokumentasikan semuanya secara bertahap, catatan demi catatan, minggu demi minggu. Apa yang kamu baca sekarang ini adalah kompilasi dari minggu-minggu yang telah berlalu, ditata ulang agar lebih enak dibaca, tapi tetap menjaga semangat asli catatan-catatan mentah saya.

## Gelombang Revolusi Vibe Coding yang Mengubah Segalanya

Sebelum kita masuk ke detail teknis aplikasi, saya perlu cerita dulu soal sesuatu yang fundamental. Sesuatu yang mengubah total cara saya membangun software. Namanya vibe coding. Istilah ini mungkin sudah sering kamu dengar, terutama kalau kamu mengikuti perkembangan dunia AI dan programming. Tapi izinkan saya menjelaskan dari perspektif pribadi, bukan dari definisi Wikipedia.

Vibe coding, dalam pengertian paling sederhana, adalah cara menulis software di mana kamu berkolaborasi dengan AI secara intensif. Bukan cuma pakai AI buat autocomplete satu baris kode, bukan cuma copy-paste dari ChatGPT. Ini lebih dalam dari itu. Kamu mendiskusikan arsitektur dengan AI. Kamu minta AI membuatkan prototype fungsi. Kamu review hasilnya, modifikasi, minta perbaikan, iterasi terus sampai hasilnya sesuai. AI jadi partner berpikir, bukan cuma alat bantu ketik. 

Untuk memahami betapa revolusionernya ini, izinkan saya flashback sebentar ke masa-masa gelap pengembangan Android tradisional. Kamu yang pernah bikin aplikasi Android dari nol pasti paham penderitaan ini. Pertama, kamu buka Android Studio. Tunggu loading. Lama. Lalu kamu buat project baru. Gradle sync mulai jalan. Tunggu lagi. Kadang lima menit, kadang lima belas menit, kadang gagal dan kamu harus clear cache lalu sync ulang. Kalau koneksi internet pas lemot, bisa setengah jam sendiri cuma buat syncing dependencies. Belum apa-apa sudah dua tab Stack Overflow terbuka.

Lalu kamu mulai menulis kode. Misalnya mau bikin RecyclerView untuk menampilkan daftar surah. Di era sebelum Jetpack Compose, kamu harus bikin XML layout untuk item-nya, bikin Adapter class, bikin ViewHolder, set up LayoutManager, handle click listener, dan kalau mau menambahkan fitur seperti swipe-to-delete atau drag-and-drop, kamu butuh ItemTouchHelper dan callback-nya juga. Untuk satu daftar sederhana, kamu menulis puluhan hingga ratusan baris kode boilerplate. Dan kalau ada bug, good luck tracing error di antara tumpukan abstraksi itu.

Emulatornya juga nggak kalah bikin sabar. Android Emulator itu berat. Bahkan di komputer dengan RAM 16GB, kalau kamu jalankan bersamaan dengan Android Studio yang sudah makan RAM 4GB sendiri, ditambah Chrome dengan 30 tab terbuka karena kamu lagi debugging, semuanya mulai terasa lamban. Build time untuk project yang mulai membesar bisa makan waktu menunggu yang bikin kamu sempat buka sosial media, scroll timeline, lupa lagi ngapain, baru ingat pas build-nya selesai. Atau gagal. Lalu build ulang.

Dan yang paling menyebalkan dari semua hal di atas adalah error message yang cryptic. Pernah nggak kamu dapat error Gradle yang bunyinya seperti ini, "Could not resolve all files for configuration... Caused by... Caused by... Caused by..." dengan stack trace sepanjang dua layar monitor? Dan solusinya ternyata cuma menambahkan satu baris di file settings.gradle? Atau error runtime yang menampilkan "java.lang.NullPointerException" tanpa menunjuk baris yang benar karena ProGuard sudah mengobfuscate nama class-nya? Masa-masa itu nyata, dan saya sudah melewati semuanya.

Lalu AI datang dan mengubah segalanya. Bukan dalam satu hari, bukan secara dramatis seperti di film sci-fi. Perubahannya gradual. Awalnya saya cuma pakai AI untuk hal-hal kecil. Tanya bagaimana syntax tertentu di Kotlin. Minta tolong jelaskan error message yang nggak saya pahami. Generate boilerplate code untuk ViewModel dasar. Hal-hal seperti itu. Tapi seiring waktu, interaksi saya dengan AI semakin mendalam. Saya mulai mendiskusikan arsitektur aplikasi secara keseluruhan. Saya minta AI menganalisis trade-off antara Room Database dan DataStore untuk kasus spesifik saya. Saya minta AI membuatkan skema JSON untuk data mushaf lengkap dengan validasi. Dan yang paling penting, saya mulai mempercayai AI sebagai partner berpikir, bukan cuma mesin penjawab.

Tapi di sini saya harus memberikan catatan penting yang benar-benar krusial. Vibe coding bukan berarti copy-paste buta dari AI. Saya tekankan ini karena ada banyak orang yang salah paham. Mereka pikir vibe coding itu artinya kamu tinggal bilang "buatkan saya aplikasi Quran" ke AI, lalu AI kasih seluruh source code, kamu paste, compile, selesai. Tidak. Bukan begitu cara kerjanya, dan kalau kamu melakukan itu, hasilnya akan jelek. Sangat jelek.

Vibe coding yang benar itu seperti pair programming. Kamu tetap harus mengerti apa yang sedang terjadi. Kamu tetap harus bisa membaca kode yang dihasilkan AI dan menilai apakah itu bagus atau buruk. Kamu tetap harus punya pengetahuan dasar tentang arsitektur software, design patterns, dan best practices. AI mempercepat eksekusi, tapi kamu yang menentukan arah. AI bisa menulis implementasi fungsi dalam hitungan detik, tapi kamu yang harus memutuskan apakah fungsi itu perlu ada, di mana posisinya dalam arsitektur, dan bagaimana interaksinya dengan komponen lain.

Analogi yang paling tepat menurut saya adalah seperti ini. Bayangkan kamu seorang arsitek bangunan. Dulu, kamu harus menggambar blueprint sendiri, menghitung struktur sendiri, memilih material sendiri, semuanya manual. Sekarang kamu punya asisten super cerdas yang bisa menggambar blueprint dalam hitungan menit berdasarkan deskripsi verbal kamu. Tapi kamu tetap arsiteknya. Kamu yang menentukan bahwa bangunan ini harus tahan gempa, harus punya ventilasi alami, harus efisien energi. Asisten menggambar, kamu yang mereview dan memutuskan. Kalau ada yang salah, kamu yang mendeteksi dan mengarahkan perbaikan. Begitulah vibe coding seharusnya dipraktikkan. Kolaborasi, bukan abdikasi.

Dan dalam perjalanan membangun SHL Quran Pro dan Qodho Reminder, filosofi ini yang selalu saya pegang. Setiap baris kode yang masuk ke repository, entah itu ditulis langsung oleh saya atau di-generate oleh AI, semuanya melewati proses review. Semuanya harus saya pahami. Semuanya harus sesuai dengan standar yang saya tetapkan. AI mempercepat proses secara dramatis, tapi tanggung jawab akhir tetap di pundak saya.

## Tiga Sahabat Tempur Saya dalam Perang Kreatif

Dalam perjalanan vibe coding ini, saya tidak menggunakan satu tools saja. Ada tiga "senjata" utama yang menjadi andalan saya, masing-masing punya kekuatan unik dan peran spesifik dalam workflow. Ketiganya saling melengkapi dengan cara yang begitu natural sehingga setelah beberapa minggu, saya nggak bisa membayangkan bekerja tanpa salah satunya. Izinkan saya perkenalkan mereka satu per satu.

### 1. Google AI Studio Laboratorium Ide Liar Tengah Malam

Google AI Studio adalah tempat saya bereksperimen tanpa rasa takut. Kalau ada ide gila yang muncul tengah malam, di sinilah saya mengujinya pertama kali. Nggak perlu setup project, nggak perlu bikin file baru, nggak perlu mikirin file structure. Tinggal buka browser, ketik prompt, dan mulai brainstorming.

Saya menggunakan Google AI Studio terutama untuk tiga hal besar. Yang pertama dan paling sering adalah prototyping logika kalkulasi. Contoh paling nyata, waktu saya mengerjakan fitur hisab untuk menentukan awal bulan Hijriah di SHL Quran Pro Hisab itu bukan kalkulasi sederhana. Ini melibatkan perhitungan astronomi yang cukup kompleks, dari posisi bulan relatif terhadap matahari, ijtimak atau konjungsi, sudut elongasi, sampai penentuan apakah hilal bisa dilihat dari wilayah Indonesia. Saya nggak mungkin menulis semua rumus itu dari nol tanpa referensi.

Jadi apa yang saya lakukan? Saya buka Google AI Studio dan mulai berdiskusi. Saya jelaskan kebutuhan saya secara detail. "Saya butuh fungsi Kotlin yang menghitung perkiraan tanggal awal bulan Hijriah berdasarkan metode hisab hakiki. Input-nya tahun Hijriah dan bulan. Output-nya tanggal Masehi yang sesuai. Gunakan algoritma Jean Meeus untuk posisi bulan." Lalu AI merespons dengan draft kode lengkap. Saya review, tanya bagian-bagian yang nggak saya pahami, minta penjelasan tentang konstanta astronomi yang dipakai, verifikasi hasilnya dengan data dari Kementerian Agama, dan iterasi sampai hasilnya akurat.

Yang kedua, saya menggunakan Google AI Studio untuk merancang skema data. Waktu mendesain struktur JSON untuk menyimpan data mushaf, saya berdiskusi panjang lebar di sini. Bagaimana seharusnya hierarki data surah, ayat, juz, hizb, dan ruku diorganisir? Apakah lebih baik pakai nested JSON atau flat structure dengan foreign key? Bagaimana format metadata tajweed, apakah pakai character range atau markup inline? Setiap keputusan desain ini saya diskusikan dengan AI, mempertimbangkan trade-off dari segi performa query, ukuran file, kemudahan parsing, dan maintainability.

Yang ketiga, prototyping Kotlin data classes. Sebelum menulis kode di Android Studio, saya sering meminta AI di Google AI Studio untuk membuatkan draft data class beserta relasi antar-entitasnya. Misalnya, "Buatkan data class untuk representasi satu ayat Al-Quran yang menyimpan nomor surah, nomor ayat, teks Arab dalam rasm Utsmani, teks transliterasi Latin, terjemahan Bahasa Indonesia, metadata posisi juz dan hizb, serta daftar aturan tajweed dengan character range." AI akan memberikan draft, saya review, kita diskusikan apakah perlu menambahkan field bookmark status, last read timestamp, atau audio reference, lalu saya polish draft-nya sebelum membawanya ke tahap implementasi sebenarnya. Semua ini terjadi cepat dalam hitungan menit, sedangkan kalau murni manual, bisa butuh waktu berjam-jam hanya untuk finalisasi skema data.

Google AI Studio juga punya satu keunggulan yang sering saya manfaatkan, yaitu kemampuannya menghandle konteks yang sangat panjang. Saya bisa paste seluruh file Kotlin yang panjangnya ratusan baris, lalu bertanya di mana letak potensi memory leak, atau minta saran refactoring untuk meningkatkan readability. Responsnya cepat, dan karena sifatnya yang stateless per sesi baru, saya merasa bebas untuk bereksperimen sebebas-bebasnya tanpa takut mengacaukan sesuatu. Kalau hasilnya jelek, tinggal mulai sesi baru. Nggak ada konsekuensi. Itulah kenapa saya menyebutnya "laboratorium". Tempat bereksperimen tanpa takut meledak.

### 2. Hermes Agent Partner Ngoding Senior yang Nggak Pernah Tidur

Kalau Google AI Studio adalah laboratorium ide, maka Hermes Agent adalah partner senior yang turun langsung ke medan tempur. Ini adalah perbedaan fundamental yang penting untuk dipahami. Google AI Studio bekerja di level abstrak, mendiskusikan ide, merancang konsep, prototyping di sandbox. Hermes Agent bekerja langsung di codebase kamu. Dia bisa membaca file, menulis file, menjalankan perintah terminal, menganalisis struktur project, bahkan men-debug build errors secara real-time.

Pertama kali saya menggunakan Hermes Agent untuk project SHL Quran Pro, saya langsung merasakan perbedaannya. Bayangkan kamu punya rekan kerja senior developer yang duduk di sebelah kamu, bisa melihat layar kamu, bisa langsung buka file yang sedang kamu kerjakan, bisa menjalankan command di terminal kamu, dan punya pengetahuan mendalam tentang arsitektur Android modern. Itulah Hermes Agent.

Dalam konteks pengembangan SHL Quran Pro, Hermes Agent berperan besar di beberapa area. Yang paling krusial adalah setup dan maintenance arsitektur MVVM. Model-View-ViewModel itu terdengar sederhana di teori, tapi implementasinya di project nyata itu penuh nuansa. Misalnya, bagaimana seharusnya ViewModel untuk layar baca Quran distrukturkan? Dia harus menghandle state ayat yang sedang ditampilkan, state bookmark, state audio player yang sedang memutar murottal, state tajweed highlight, dan state navigasi antar surah. Semua state ini harus dimanage menggunakan StateFlow agar Compose UI bisa meng-observe perubahan secara reaktif. Dan semua ini harus thread-safe karena beberapa operasi berjalan di coroutine yang berbeda.

Hermes Agent membantu saya merancang dan mengimplementasikan semua itu. Bukan cuma memberikan contoh kode generik, tapi langsung menulis di file ViewModel yang ada di project saya. Dia bisa membaca struktur folder project saya, memahami dependency yang sudah terinstall dari build.gradle.kts, dan menulis kode yang kompatibel dengan setup yang sudah ada. Waktu saya meminta dia untuk menambahkan StateFlow baru untuk fitur tajweed toggle, dia nggak cuma menulis deklarasi StateFlow-nya. Dia juga menambahkan fungsi toggle di ViewModel, memperbarui UI layer untuk meng-observe state tersebut, dan memastikan default value-nya konsisten dengan UserPreferences yang tersimpan di DataStore.

Kemampuan refactoring Hermes Agent juga luar biasa bermanfaat. Ada satu kejadian yang saya ingat dengan jelas. Di versi awal SHL Quran Pro, saya punya satu file Repository yang menghandle semuanya. Baca data mushaf, manage bookmark, handle audio caching, semuanya di satu file. Ukurannya sudah membengkak sampai lebih dari 500 baris dan mulai sulit di-maintain. Saya minta Hermes Agent untuk memecahnya menjadi beberapa repository yang lebih fokus. Dan dia melakukannya dengan presisi. QuranRepository untuk operasi terkait data mushaf. BookmarkRepository untuk manajemen bookmark. AudioRepository untuk caching dan playback murottal. Setiap repository mendapat interface-nya sendiri untuk memudahkan testing dan dependency injection. Dan yang paling mengesankan, semua referensi di ViewModel dan dependency injection graph diperbarui secara otomatis. Nggak ada yang missed, nggak ada yang broken.

Area lain yang sangat terbantu adalah dependency auditing dan debugging build.gradle.kts. Siapa pun yang pernah bekerja dengan Gradle di project Android pasti tahu betapa menyebalkannya dependency conflicts. Versi library A butuh Kotlin 1.9.0, tapi library B sudah di-build untuk Kotlin 2.0.0, dan Compose Compiler punya versi requirement-nya sendiri. Belum lagi BOM (Bill of Materials) yang harus di-align antar dependencies. Hermes Agent bisa membaca file build.gradle.kts saya, menganalisis dependency tree, mengidentifikasi potensi konflik, dan menyarankan versi yang kompatibel. Kadang dia bahkan mendeteksi masalah yang belum saya sadari, seperti library yang sudah deprecated atau versi yang punya known vulnerability.

Dan jangan lupa soal terminal access. Hermes Agent bisa menjalankan perintah langsung di terminal saya. Mau jalankan ./gradlew dependencies untuk melihat dependency tree? Langsung bisa. Mau jalankan ./gradlew lint untuk analisis kode statis? Tinggal perintah. Mau check size APK hasil build? Hermes bisa navigasi ke folder output dan kasih tahu ukurannya. Semua ini tanpa saya harus pindah-pindah window. Proses yang tadinya butuh context switching berkali-kali sekarang bisa dilakukan dalam satu alur percakapan yang kontinu.

### 3. Android Studio Bengkel Perakitan Fisik dan Pengujian Performa

Dengan semua kecanggihan Google AI Studio dan Hermes Agent, kenapa masih butuh Android Studio? Jawabannya sederhana. Ada hal-hal yang hanya bisa dilakukan oleh IDE visual yang terintegrasi langsung dengan Android SDK. Google AI Studio dan Hermes Agent itu brilliant untuk logika, arsitektur, dan kode. Tapi kalau kamu mau melihat bagaimana UI benar-benar tampil di layar, kalau kamu mau mengukur berapa byte memori yang dikonsumsi oleh setiap Composable, kalau kamu mau melacak di mana tepatnya ada frame drop yang menyebabkan scroll terasa janky, kamu butuh Android Studio.

Layout Inspector adalah tool pertama yang saya andalkan. Ini memungkinkan saya untuk "membedah" UI yang sedang berjalan di device atau emulator, layer demi layer. Saya bisa melihat hierarki Composable tree, memastikan nggak ada unnecessary recomposition yang terjadi, dan memverifikasi bahwa spacing, padding, dan alignment sesuai dengan desain. Waktu membangun halaman baca Quran misalnya, saya perlu memastikan bahwa font Arab ditampilkan dengan baseline alignment yang benar, baris-baris ayat punya spacing yang nyaman untuk dibaca, dan scrolling behavior buttery smooth. Layout Inspector membantu saya mendeteksi dan memperbaiki isu-isu visual yang nggak mungkin dideteksi hanya dari kode.

Compose Preview juga jadi andalan. Ini memungkinkan saya melihat output visual dari Composable function tanpa harus build dan deploy seluruh aplikasi. Mau lihat bagaimana tampilan card bookmark dengan teks panjang versus teks pendek? Tinggal bikin dua Preview dengan data dummy yang berbeda. Mau test bagaimana UI beradaptasi dari light mode ke dark mode? Bikin dua Preview dengan konfigurasi theme berbeda. Mau lihat bagaimana tampilan di layar kecil versus layar besar? Bikin Preview dengan deviceSpec yang berbeda. Iterate visual jadi jauh lebih cepat.

Tapi tool paling krusial di Android Studio untuk project saya adalah Android Profiler. Ini terdiri dari tiga profiler utama yaitu Memory Profiler, CPU Profiler, dan Energy Profiler. Dan untuk aplikasi seperti SHL Quran Pro yang punya banyak resource berat, daftar besar data mushaf, file audio murottal, gambar kaligrafi, dan rendering teks Arab yang kompleks, profiling bukan sekadar nice-to-have, ini wajib.

Memory Profiler membantu saya mendeteksi memory leak. Ada satu kasus yang cukup dramatis waktu awal-awal development. Setiap kali user navigasi dari satu surah ke surah lain, memori yang dikonsumsi naik sekitar 2-3 MB tapi nggak pernah turun kembali. Setelah navigasi bolak-balik sepuluh kali, memori sudah membengkak lebih dari 30 MB di atas baseline. Ini classic memory leak. Dengan Memory Profiler, saya bisa track allocation, menemukan bahwa ada coroutine scope yang nggak di-cancel saat Fragment atau ViewModel di-destroy, sehingga reference ke data mushaf yang besar tetap hidup di memori. Perbaikannya sederhana, pindah ke viewModelScope yang otomatis di-cancel, tapi menemukan masalahnya tanpa Memory Profiler akan jauh lebih sulit.

CPU Profiler saya gunakan untuk mengoptimasi performa scroll. Kalau user sedang membaca Al-Quran dan scroll cepat, rendering teks Arab yang kompleks bisa menyebabkan jank kalau nggak di-handle dengan benar. CPU Profiler menunjukkan di mana thread utama menghabiskan waktu terlalu lama. Dari situ saya bisa memutuskan operasi mana yang harus dipindahkan ke background thread dan mana yang bisa di-cache untuk menghindari recomputation yang nggak perlu.

Energy Profiler mungkin terdengar kurang seksi dibandingkan dua profiler lainnya, tapi untuk aplikasi Al-Quran ini justru sangat penting. Bayangkan user yang membuka aplikasi saat sholat tarawih untuk membaca Al-Quran selama satu jam atau lebih. Kalau aplikasi kita boros baterai, user akan notice dan nggak happy. Energy Profiler membantu saya memastikan bahwa SHL Quran Pro nggak melakukan background work yang nggak perlu, nggak membangunkan CPU terlalu sering, dan secara umum bersahabat dengan baterai.

Lalu ada Logcat, si veteran debugging yang nggak pernah gagal. Meski sering dianggap primitif dibandingkan profiling tools modern, Logcat tetap menjadi senjata utama saya untuk real-time debugging. Saya memasang logging yang cukup detail di bagian-bagian kritis, misalnya saat parsing data mushaf, saat memuat audio murottal, dan saat menghitung jadwal sholat. Dengan filter tag yang tepat, saya bisa memantau alur eksekusi secara real-time dan langsung mengetahui di mana ada masalah.

Dan terakhir, real device testing. Emulator itu bagus untuk development harian, tapi tidak ada yang bisa menggantikan testing di perangkat sungguhan. Saya menguji SHL Quran Pro di berbagai device dengan spesifikasi berbeda. Samsung Galaxy A15 untuk segmen mid-range, beberapa perangkat lama untuk memastikan kompatibilitas dengan minSdk 24 yaitu Android 7.0 Nougat, dan perangkat flagship untuk memastikan fitur-fitur yang memanfaatkan hardware terbaru berjalan optimal. Rendering font Arab, respons haptic feedback pada fitur tasbih, akurasi timing audio playback, semua ini harus diverifikasi di perangkat nyata.

Kalau saya gambarkan workflow ketiga tools ini dalam sebuah alur, kira-kira seperti ini. Google AI Studio adalah tempat lahirnya ide dan desain awal. Saya bereksperimen, brainstorming, prototyping di sana. Ketika ide sudah cukup matang, saya pindah ke Hermes Agent untuk implementasi serius. Hermes Agent menulis kode langsung di project, melakukan refactoring, menjalankan build, dan debugging awal. Setelah kode siap dan build berhasil, saya berpindah ke Android Studio untuk pengujian visual, profiling performa, dan fine-tuning di perangkat nyata. Ada kalanya alur ini berulang. Misalnya, saat profiling di Android Studio saya menemukan memory leak, saya kembali ke Hermes Agent untuk memperbaikinya, dan kalau perlu mendiskusikan pendekatan perbaikan dulu di Google AI Studio.

```plain
┌─────────────────────┐
│  Google AI Studio    │
│  (Ide & Prototype)   │
│                     │
│  • Brainstorm logic  │
│  • Design JSON schema│
│  • Draft data classes│
└────────┬────────────┘
         │ Ide matang
         ▼
┌─────────────────────┐
│  Hermes Agent        │
│  (Implementasi)      │
│                     │
│  • Write real code   │
│  • MVVM architecture │
│  • Refactor & debug  │
│  • Terminal commands  │
└────────┬────────────┘
         │ Build berhasil
         ▼
┌─────────────────────┐
│  Android Studio      │
│  (Testing & Polish)  │
│                     │
│  • Visual inspection │
│  • Memory profiling  │
│  • Device testing    │
│  • Performance tuning│
└─────────────────────┘
```

Tiga tools, satu tujuan. Membangun aplikasi yang bukan cuma jalan, tapi benar-benar bagus. Dan dengan kombinasi ini, kecepatan serta kualitas development meningkat secara drastis dibandingkan cara tradisional.

## Awal Mula Ide SHL Quran Pro Lahir dari Keresahan Pribadi

Sekarang kita masuk ke cerita asal-usul aplikasi itu sendiri. Kenapa saya membuat SHL Quran Pro? Jawabannya berakar dari keresahan yang sangat personal.

Sebagai seorang Muslim yang berusaha rutin membaca Al-Quran, saya tentu saja sudah mencoba banyak aplikasi Al-Quran yang tersedia di Play Store. Puluhan, mungkin ratusan aplikasi. Dan jujur, banyak yang bagus. Tapi selalu ada sesuatu yang mengganggu saya. Selalu ada "tapi" di setiap aplikasi yang saya coba.

Ada aplikasi yang fiturnya lengkap, tapi iklannya luar biasa mengganggu. Banner iklan di bagian bawah layar saat kamu sedang membaca ayat suci. Interstitial ad yang muncul tiba-tiba saat kamu berpindah surah. Video ad yang harus ditonton 30 detik untuk unlock fitur bookmark. Saya paham bahwa developer perlu menghasilkan uang, dan iklan adalah model bisnis yang sah. Tapi ada sesuatu yang terasa kurang pantas saat iklan game atau produk komersial disandingkan dengan ayat-ayat suci Al-Quran di layar yang sama. Itu perasaan pribadi saya, mungkin kamu setuju, mungkin tidak. Tapi perasaan itu nyata dan menjadi salah satu motivasi utama saya.

Ada aplikasi yang bebas iklan, tapi tipografinya buruk. Font Arab yang dipakai terlihat kaku, spacing antar huruf nggak proporsional, harakat menumpuk di atas huruf dengan posisi yang kurang presisi. Buat orang yang terbiasa membaca mushaf fisik dengan kaligrafi yang indah, membaca Al-Quran di aplikasi dengan font jelek itu mengurangi khusyuk secara signifikan. Mungkin terdengar berlebihan, tapi coba bandingkan pengalaman membaca Al-Quran dari mushaf cetak Madinah dengan membaca dari aplikasi yang font-nya terlihat seperti dikerjakan sambil buru-buru. Bedanya terasa.

Dan ada juga aplikasi yang font-nya bagus dan bebas iklan, tapi desain UI-nya terasa membosankan, generik, atau malah norak. Warna-warna yang terlalu mencolok, ornamen yang berlebihan, layout yang terasa cramped. Atau sebaliknya, terlalu minimalis sampai terasa steril dan nggak berkarakter. Menemukan aplikasi Al-Quran yang elegant, clean, berkarakter visual yang kuat, sekaligus fungsional itu ternyata sulit.

Keresahan-keresahan ini menumpuk dari waktu ke waktu. Setiap kali saya menginstall aplikasi Quran baru dari Play Store dan menemukan hal yang sama, ada suara kecil di kepala yang berkata, "Coba bikin sendiri aja." Awalnya saya abaikan. Bikin aplikasi Al-Quran dari nol itu bukan perkara gampang. Data mushafnya saja sudah jadi tantangan besar, belum bicara soal rendering font Arab, audio murottal, tajweed highlighting, dan segala fitur lainnya. Itu proyek yang scope-nya masif untuk solo developer.

Tapi suara itu makin lama makin keras. Dan satu malam di awal tahun 2026, setelah sekali lagi merasa frustrasi dengan aplikasi Quran yang baru saya download, yang ternyata punya fitur sharing berformat ugly dan tajweed-nya nggak akurat, saya membuat keputusan. Di meja kerja yang masih berantakan dengan sisa camilan dan notes adhesive, saya membuka Google AI Studio dan mengetik prompt pertama yang memulai semuanya.

"Saya ingin membangun aplikasi Al-Quran Android dari nol menggunakan Kotlin dan Jetpack Compose. Aplikasi ini harus zero ads, memiliki tipografi Arab terbaik yang mungkin, desain UI yang premium dan elegant, serta fitur lengkap termasuk tajweed highlighting, audio murottal, tasbih digital, dan widget home screen. Target audience adalah Muslim Indonesia yang menginginkan pengalaman membaca Al-Quran digital yang bermartabat. Bantu saya mulai dari arsitektur dasar."

Malam itu menjadi malam pertama dari banyak malam-malam panjang yang akan datang. Dan dari prompt sederhana itu, lahirlah apa yang sekarang dikenal sebagai SHL Quran Pro.

Saya bermimpi tentang aplikasi Quran yang akan saya gunakan sendiri dengan bangga. Yang ketika saya buka di masjid saat menunggu iqamah, orang yang melihat layar HP saya akan bertanya, "Itu aplikasi apa? Bagus banget tampilannya." Yang setiap detail visualnya dipikirkan dengan cermat, dari pemilihan warna yang kalem dan nyaman di mata sampai transisi antar halaman yang smooth. Yang font Arab-nya indah seperti mushaf cetak terbaik. Yang fiturnya lengkap tanpa terasa bloated. Yang gratis, tanpa iklan, tanpa pembelian in-app, murni dibangun sebagai amal jariyah dan kebanggaan karya.

Mimpi besar? Tentu saja. Naif? Mungkin. Tapi kadang proyek terbaik lahir dari mimpi yang terasa terlalu besar. Dan dengan bantuan tiga sahabat tempur yang sudah saya ceritakan di atas, mimpi itu mulai mengkristal menjadi kenyataan, satu commit demi satu commit.

## Bedah Super Detail Seluruh Fitur SHL Quran Pro

Oke, sekarang kita masuk ke bagian yang saya tahu banyak ditunggu. Detail fitur. Tapi saya nggak akan cuma bikin daftar fitur yang kering dan membosankan. Untuk setiap fitur, saya akan ceritakan apa yang ada di baliknya, tantangan teknisnya, keputusan desain yang saya buat, dan kadang-kadang cerita drama yang menyertai pengembangannya. Siap? Kita mulai dari yang paling fundamental dan paling kritis.

### 1. Standar Validitas Data Mushaf Suci yang Tidak Boleh Salah Satu Huruf Pun

Ini adalah fondasi dari segalanya. Kalau data mushaf-nya salah, seluruh bangunan di atasnya runtuh. Nggak pedal seberapa cantik UI-nya, seberapa smooth animasinya, seberapa kaya fiturnya. Kalau ada satu huruf Arab yang salah, satu harakat yang hilang, satu ayat yang tertukar posisinya, aplikasi ini kehilangan seluruh kredibilitasnya. Dan buat aplikasi yang berkaitan dengan kitab suci, kredibilitas bukan sekadar reputasi bisnis. Ini masalah tanggung jawab spiritual.

Jadi dari awal saya menetapkan standar yang sangat ketat untuk data mushaf. Data utama yang saya gunakan bersumber dari standar Mushaf Madinah yang diterbitkan oleh Mujamma' al-Malik Fahd, dan di-cross-reference dengan data resmi dari Kementerian Agama Republik Indonesia (Kemenag RI). Kenapa dua sumber? Karena saya ingin memastikan bahwa tidak ada perbedaan yang terlewat. Mushaf Madinah adalah standar internasional yang diakui oleh umat Islam seluruh dunia. Data Kemenag RI memberikan lapisan verifikasi tambahan khususnya untuk konteks Indonesia, termasuk terjemahan resmi dalam Bahasa Indonesia.

Proses verifikasi datanya cukup intensif. Pertama, saya memastikan jumlah total ayat tepat 6.236. Ini mungkin terdengar simpel, tapi kamu harus ingat bahwa ada perbedaan pendapat ulama mengenai apakah basmalah di awal setiap surah (kecuali At-Taubah) dihitung sebagai ayat pertama atau bukan. Dalam riwayat Hafs 'an 'Ashim yang menjadi standar mushaf yang paling banyak digunakan di Indonesia dan mayoritas dunia Muslim, basmalah di awal Al-Fatihah dihitung sebagai ayat pertama (sehingga Al-Fatihah memiliki 7 ayat), sementara basmalah di awal surah-surah lain bukan merupakan bagian dari ayat surah tersebut. Total 6.236 ayat ini harus dipastikan benar dalam data mapping saya.

Setiap ayat dalam database memiliki mapping ke posisi juz (1-30), hizb (1-60), dan ruku' (556 ruku' dalam Al-Quran). Mapping ini penting untuk fitur navigasi. User harus bisa langsung lompat ke Juz 30 misalnya, atau ke hizb tertentu, dan landing di ayat yang tepat. Satu kesalahan mapping berarti user bisa diarahkan ke ayat yang salah, dan untuk pengalaman membaca Al-Quran, itu sangat mengganggu.

Teks Arab yang digunakan adalah dalam rasm Utsmani, bukan rasm Imla'i. Apa bedanya? Rasm Utsmani adalah cara penulisan yang mengikuti tradisi penulisan mushaf-mushaf awal yang disalin atas perintah Khalifah Utsman bin Affan. Ada beberapa perbedaan spelling dengan rasm Imla'i (cara penulisan Arab modern standar). Misalnya, kata "sholat" dalam rasm Utsmani ditulis dengan alif setelah lam (الصلوة), sedangkan dalam rasm Imla'i ditulis الصلاة. Mungkin terlihat sepele, tapi buat penghafal Al-Quran yang terbiasa dengan mushaf cetak, konsistensi rasm ini sangat penting. Mereka membaca dengan mata yang terlatih mengenali pola visual spesifik dari rasm Utsmani, dan perbedaan kecil pun bisa mengganggu kelancarannya.

Sekarang kita bicara soal tajweed color metadata, dan ini bagian yang benar-benar teknis. Setiap aturan tajweed dalam Al-Quran harus ditandai sehingga bisa ditampilkan dengan warna yang berbeda ke user. Ikhfa ditandai hijau, idgham bighunnah ditandai biru, iqlab ditandai magenta, qalqalah ditandai merah gelap, ghunnah ditandai oranye, dan seterusnya. Setiap penandaan ini dilakukan menggunakan character range indexing. Artinya, untuk setiap aturan tajweed dalam setiap ayat, data-nya berisi posisi karakter awal dan posisi karakter akhir dalam string Unicode ayat tersebut.

Kenapa character range dan bukan markup inline seperti HTML? Karena markup inline akan mengubah string asli dan membuat rendering lebih kompleks. Dengan character range, teks Arab tetap bersih sebagai pure string, dan layer pewarnaan tajweed diterapkan sebagai overlay saat rendering. Ini memudahkan banyak hal, termasuk pencarian teks, copy-paste, dan penghitungan posisi untuk audio synchronization.

Tapi implementasi character range di Unicode Arab itu penuh jebakan. Karakter Arab bisa memiliki combining characters (harakat seperti fathah, kasrah, dhammah) yang menempati posisi tersendiri dalam string Unicode meskipun secara visual mereka menempel pada huruf dasarnya. Jadi ketika data tajweed berkata "warnai karakter posisi 5 sampai 8", posisi-posisi itu harus dihitung dengan benar termasuk combining characters. Salah hitung satu posisi saja, dan warna tajweed bisa menandai huruf yang salah. Inilah yang saya ceritakan di bagian awal tadi, debugging tajweed color hingga dini hari.

Proses testing untuk data integrity ini saya lakukan secara berlapis. Layer pertama adalah automated checksum verification. Setiap file data mushaf memiliki SHA-256 checksum yang sudah diverifikasi terhadap sumber resmi. Setiap kali aplikasi pertama kali dijalankan atau data di-update, checksum diverifikasi untuk memastikan file tidak corrupt atau ter-modify. Layer kedua adalah unit test yang memverifikasi jumlah surah (114), jumlah ayat per surah (sesuai standar), total ayat keseluruhan (6.236), dan mapping juz/hizb/ruku'. Layer ketiga, yang paling memakan waktu, adalah verifikasi manual. Saya membandingkan rendering teks di aplikasi dengan mushaf cetak fisik, ayat per ayat, untuk surah-surah tertentu yang saya pilih sebagai sample. Ini nggak mungkin dilakukan untuk seluruh 6.236 ayat secara manual, jadi saya memilih sample yang representatif termasuk ayat-ayat yang dikenal memiliki rasm Utsmani berbeda dari rasm Imla'i, ayat-ayat terpanjang, dan ayat-ayat dengan aturan tajweed yang kompleks.

Apakah prosesnya panjang dan melelahkan? Sangat. Tapi kompromi bukan opsi ketika menyangkut kebenaran teks suci. Ini satu titik di mana saya nggak akan pernah mengambil jalan pintas.

### 2. Keindahan Font Amiri Quran dan Rahasia Ligatur Lam Alif

Setelah data mushaf-nya solid, tantangan berikutnya adalah bagaimana menampilkan teks Arab itu dengan visual yang indah, autentik, dan nyaman dibaca. Dan di sinilah font menjadi sangat penting. Pemilihan font untuk aplikasi Al-Quran bukan keputusan trivial. Ini bukan seperti memilih antara Roboto dan Inter untuk aplikasi e-commerce. Font Arab untuk Al-Quran harus memenuhi beberapa kriteria yang sangat ketat.

Pertama, font harus mendukung rasm Utsmani secara lengkap. Banyak font Arab yang didesain untuk teks Arab modern (rasm Imla'i) dan nggak memiliki glyph khusus untuk variasi penulisan rasm Utsmani. Kedua, font harus memiliki dukungan harakat yang komprehensif termasuk kombinasi harakat yang jarang seperti fathah berdiri (alif khanjariyyah), sukun yang ditempatkan di posisi non-standar, dan tanda-tanda waqf. Ketiga, font harus memiliki estetika kaligrafi yang indah, karena kita bicara tentang teks suci yang layak ditampilkan dengan keindahan.

Setelah mengevaluasi banyak font termasuk Scheherazade New, KFGQPC Uthmanic Script HAFS, LPMQ ISEP Misbah, dan beberapa lainnya, pilihan saya jatuh pada Amiri Quran. Kenapa Amiri? Ada beberapa alasan yang sangat spesifik.

Amiri Quran adalah varian khusus dari typeface Amiri yang dirancang oleh Khaled Hosny. Font ini didesain mengikuti tradisi kaligrafi Naskh yang digunakan di mushaf-mushaf cetak Mesir yang terkenal akan keindahan tipografinya. Yang membuat Amiri Quran unggul dibandingkan banyak alternatif adalah dukungan OpenType features-nya yang sangat kaya.

Mari kita bicara teknisnya sebentar. OpenType features adalah instruksi yang tertanam dalam file font yang mengatur bagaimana glyph (bentuk visual huruf) ditampilkan dalam konteks tertentu. Dan untuk teks Arab, ini sangat krusial karena bahasa Arab adalah script yang highly contextual. Bentuk sebuah huruf berubah tergantung posisinya dalam kata, apakah di awal (initial form), tengah (medial form), akhir (final form), atau berdiri sendiri (isolated form). Dan di atas itu, ada ligatur, yaitu ketika dua atau lebih huruf bergabung menjadi satu bentuk visual khusus.

Ligatur paling ikonik dalam kaligrafi Arab adalah ligatur Lam-Alif (لا). Ketika huruf Lam (ل) diikuti oleh Alif (ا), keduanya nggak ditulis sebagai dua huruf yang bersebelahan. Mereka bergabung menjadi satu bentuk khas yang sangat mudah dikenali. Amiri Quran memiliki rendering ligatur Lam-Alif yang sangat indah, mengikuti tradisi kaligrafi Naskh klasik. Kedua huruf menyatu dengan proporsi yang seimbang, lengkungan yang halus, dan estetika yang mengingatkan pada kaligrafi tangan master khat.

Tapi ligatur Lam-Alif hanyalah salah satu dari banyak ligatur yang di-handle oleh Amiri Quran. Font ini juga memiliki ligatur kontekstual untuk berbagai kombinasi huruf lainnya, semuanya diatur melalui OpenType lookup tables. Ada GSUB (Glyph Substitution) tables yang mengatur kapan satu glyph diganti dengan glyph lain berdasarkan konteks, dan GPOS (Glyph Positioning) tables yang mengatur posisi tepat dari setiap glyph dan harakat relatif terhadap huruf dasarnya.

Dalam implementasi di Jetpack Compose, saya memastikan bahwa semua OpenType features ini diaktifkan. Compose pada dasarnya menggunakan text shaping engine (HarfBuzz di Android) yang mendukung fitur-fitur OpenType secara native. Tapi ada beberapa konfigurasi yang perlu dilakukan agar hasilnya optimal. Misalnya, saya perlu mengatur line height dan letter spacing dengan cermat. Untuk teks Arab, letter spacing default seringkali terlalu rapat atau terlalu renggang. Saya bereksperimen dengan berbagai nilai sampai menemukan sweet spot di mana huruf-huruf terlihat proporsional, harakat terbaca jelas tanpa menumpuk, dan jarak antar baris cukup lega untuk mencegah harakat baris atas bertabrakan dengan huruf tinggi (seperti Alif dan Lam) di baris bawah.

Ada satu detail kecil tapi sangat berpengaruh yang saya habiskan waktu cukup lama untuk menyempurnakan, yaitu line-height. Ini terlihat sepele, "kan tinggal set lineHeight di TextStyle?" Secara teknis iya, tapi menemukan nilai yang tepat ternyata butuh iterasi yang banyak. Kalau line-height terlalu kecil, harakat di baris atas bisa menimpa huruf-huruf tinggi di baris bawah. Ini terutama jadi masalah pada ayat-ayat yang memiliki banyak harakat tanwin (fathatain, kasratain, dhammatain) yang memiliki ekstensi vertikal cukup besar. Kalau line-height terlalu besar, tampilan jadi terasa longgar dan boros ruang layar, user harus scroll lebih banyak untuk membaca jumlah ayat yang sama. Menemukan keseimbangan yang tepat antara readability dan informasional density itu butuh banyak percobaan.

Proses saya untuk menemukan line-height yang optimal kira-kira seperti ini. Saya memilih beberapa sample ayat yang mewakili berbagai "kesulitan" rendering. Ayat pendek dengan sedikit harakat seperti dari Juz 'Amma. Ayat panjang dengan banyak harakat dan tanda waqf. Ayat yang mengandung huruf-huruf tinggi berturut-turut. Lalu saya render semua sample ini dengan berbagai nilai line-height, dari 1.2x sampai 2.0x ukuran font, dan menilai hasilnya secara visual di perangkat nyata. Bukan di emulator saja, tapi di HP sungguhan dengan ukuran layar 6.5 inci yang merupakan ukuran rata-rata pengguna target. Akhirnya saya menemukan sweet spot yang memberikan readability optimal tanpa terlalu boros ruang layar, dan hasilnya saya simpan sebagai default di ThemeConfig aplikasi.

Perbandingan sebelum dan sesudah proses optimasi tipografi ini cukup dramatis. Versi awal SHL Quran Pro menggunakan font default sistem untuk teks Arab, yang ternyata adalah Noto Naskh Arabic. Font yang bagus dan versatile, tapi nggak setara dengan Amiri Quran untuk konteks mushaf. Ketika saya mengganti ke Amiri Quran dengan konfigurasi yang sudah dioptimasi, tampilannya berubah dari "aplikasi yang menampilkan teks Arab" menjadi "pengalaman membaca mushaf digital yang cantik". Perbedaannya bukan sekadar lebih bagus. Rasanya seperti membandingkan mushaf cetak kualitas standar dari toko buku biasa dengan mushaf premium dari Madinah. Keduanya sama-sama readable, tapi ada level keindahan dan kekhusyukan yang berbeda.

### 3. Tiga Tingkat Ketebalan Kaligrafi Biar Mata Nggak Cepat Lelah

Setelah font terpilih dan konfigurasi dasar teroptimasi, saya menyadari bahwa satu ukuran dan ketebalan font nggak akan cocok untuk semua situasi dan semua user. Orang tua yang matanya sudah mulai kurang tajam butuh teks yang lebih tebal dan besar dibandingkan anak muda berusia duapuluhan dengan penglihatan tajam. Orang yang membaca Al-Quran di malam hari dengan lampu kamar redup butuh ketebalan font yang berbeda dari orang yang membaca di siang hari di bawah sinar matahari cerah.

Dari pemikiran ini lahirlah fitur tiga tingkat ketebalan kaligrafi di SHL Quran Pro. Pertama ada mode Normal, ini adalah ketebalan default yang cocok untuk kebanyakan situasi. Font weight standar, cocok untuk membaca di kondisi pencahayaan normal, untuk user dengan penglihatan yang baik, dan untuk sesi baca yang panjang karena nggak terlalu tebal sehingga nggak cepat melelahkan mata. Ini mode yang aktif pertama kali saat user membuka aplikasi dan yang saya rekomendasikan untuk penggunaan sehari-hari.

Kedua ada mode Semi Tebal. Ini satu tingkat di atas Normal, cocok untuk beberapa situasi spesifik. User yang sudah berusia di atas lima puluh tahun dan mulai mengalami presbiopia atau mata tua biasanya lebih nyaman dengan teks yang sedikit lebih tebal tanpa harus memperbesar ukuran font terlalu banyak. Semi Tebal juga bagus untuk membaca di kondisi pencahayaan yang kurang optimal, misalnya di masjid dengan penerangan yang tidak terlalu terang, atau di kamar tidur dengan lampu tidur saja. Ketebalan tambahan ini meningkatkan kontras visual sehingga huruf-huruf dan harakat lebih mudah dibedakan.

Ketiga ada mode Tebal, ini ketebalan maksimum. Didesain untuk situasi yang membutuhkan visibilitas tinggi. Penggunaan outdoor di bawah sinar matahari langsung, di mana silau layar bisa mengurangi kontras, jadi mode Tebal membantu menjaga readability. Juga berguna untuk user dengan gangguan penglihatan yang lebih serius, atau untuk kasus di mana HP diletakkan agak jauh dari mata, misalnya diletakkan di stand di atas meja saat sholat tarawih.

Implementasi teknis fitur ini di Jetpack Compose memanfaatkan reactive state management. Pilihan ketebalan user disimpan di DataStore sebagai preference yang persisten, sehingga kalau user memilih Semi Tebal, pilihan itu tetap tersimpan meskipun aplikasi ditutup dan dibuka kembali. Di level ViewModel, pilihan ini menjadi sebuah StateFlow yang di-observe oleh Compose UI.

```kotlin
// Di ViewModel
private val _fontWeightLevel = MutableStateFlow(FontWeightLevel.NORMAL)
val fontWeightLevel: StateFlow<FontWeightLevel> = _fontWeightLevel.asStateFlow()

fun setFontWeight(level: FontWeightLevel) {
    _fontWeightLevel.value = level
    viewModelScope.launch {
        userPreferencesRepository.saveFontWeight(level)
    }
}
```

```kotlin
// Di Composable
val fontWeight by viewModel.fontWeightLevel.collectAsStateWithLifecycle()

Text(
    text = ayahText,
    style = TextStyle(
        fontFamily = amiriQuranFamily,
        fontWeight = when (fontWeight) {
            FontWeightLevel.NORMAL -> FontWeight.Normal
            FontWeightLevel.SEMI_BOLD -> FontWeight.Medium
            FontWeightLevel.BOLD -> FontWeight.Bold
        },
        fontSize = quranFontSize
    )
)
```

Yang menarik secara teknis adalah bagaimana perubahan ketebalan ini langsung terlihat secara real-time tanpa perlu restart layar. Karena fontWeight adalah StateFlow yang di-observe oleh Compose, setiap kali nilainya berubah, Compose secara otomatis melakukan recomposition hanya pada Text composable yang terpengaruh. User tinggal buka pengaturan, geser slider atau tekan tombol pilihan ketebalan, dan langsung bisa melihat perubahannya di layar baca tanpa harus navigasi keluar dan masuk lagi. Feedback visual yang instan seperti ini penting untuk UX yang baik, karena user bisa langsung menilai apakah ketebalan yang dipilih sudah nyaman atau perlu penyesuaian lebih lanjut.

Saya juga menambahkan preview visual di halaman pengaturan. Ketika user memilih tingkat ketebalan, ada sample teks Arab yang langsung berubah ketebalannya di area preview di atas pilihan. Teks sample ini saya pilih dengan cermat, yaitu ayat Al-Fatihah pertama (Bismillahirrahmanirrahim), karena ini adalah teks yang sangat familiar bagi semua Muslim sehingga perubahan visual-nya mudah dinilai. User bisa membandingkan ketiga tingkat ketebalan dengan cepat sebelum memutuskan mana yang paling nyaman buat mata mereka.

Keputusan untuk menyediakan tiga tingkat, bukan dua dan bukan lima atau lebih, juga melewati pertimbangan desain. Dua pilihan terasa terlalu terbatas. Lima atau lebih akan membuat user bingung karena perbedaan antar level menjadi terlalu subtle untuk dibedakan secara visual. Tiga adalah sweet spot yang memberikan variasi cukup tanpa overwhelm. Ini mengikuti prinsip "The Paradox of Choice" yang mengatakan bahwa terlalu banyak pilihan justru membuat orang lebih sulit memutuskan dan kurang puas dengan pilihannya. Tiga opsi, cukup untuk mengakomodasi variasi kebutuhan, tapi nggak terlalu banyak sehingga terasa membebani.

Respons user terhadap fitur ini cukup positif di tahap closed testing. Beberapa tester yang berusia di atas lima puluh tahun secara khusus menghargai mode Tebal. Satu tester menulis di feedback bahwa ini pertama kalinya dia bisa membaca Al-Quran di HP tanpa kacamata baca. Feedback seperti itu membuat semua kerja keras optimasi tipografi terasa sangat berharga. Pada akhirnya, fitur teknis yang paling bermakna bukan yang paling canggih atau paling sulit diimplementasikan, tapi yang benar-benar menyelesaikan masalah nyata pengguna.

## Tasbih Digital Obsidian Gold Sensasi Getaran yang Bikin Kangen Berdzikir

Pernah nggak sih kamu merasa dzikir itu harusnya lebih... *imersif*? Maksud saya begini — kita hidup di zaman di mana smartphone bisa bikin kamu merasakan getaran halus saat mengetik, bisa memberi feedback sentuhan saat gaming, tapi kenapa teknologi haptic ini belum pernah dipakai secara serius untuk pengalaman ibadah? Pertanyaan sederhana inilah yang mengawali perjalanan panjang saya membangun fitur tasbih digital di SHL Quran Pro.

Dan bukan sembarang tasbih digital ya. Bukan yang cuma angka naik satu-satu dengan tampilan flat membosankan. Yang saya mau adalah sesuatu yang ketika kamu memegangnya, menutup mata, dan mulai berdzikir — kamu *merasakan* setiap hitungan. Seperti butiran tasbih fisik yang mengalir di antara jari-jarimu, tapi versi digital yang jauh lebih kaya pengalaman.

### Angka 68sp dan Cincin Progres yang Hidup Bernapas

Hal pertama yang kamu lihat saat membuka tasbih digital ini adalah angka besar. Besar *banget*. Saya pakai ukuran 68sp — untuk konteks, itu hampir dua kali lipat dari judul artikel biasa di layar smartphone. Kenapa sebesar itu? Karena saat kamu berdzikir, mata kamu mungkin setengah terpejam. Atau mungkin kamu berdzikir dalam gelap sebelum tidur. Angka sebesar ini memastikan kamu bisa melihat progres tanpa harus fokus berlebihan pada layar.

Di sekeliling angka itu ada cincin progres yang beranimasi halus. Setiap kali kamu mengetuk layar, cincin ini bergerak sedikit — smooth, gradual, penuh ketenangan. Warnanya? Tentu saja gold on obsidian. Emas yang bercahaya di atas kegelapan. Ada sesuatu yang sangat meditatif ketika melihat cincin emas itu perlahan-lahan melingkar sempurna, dan kamu tahu bahwa setiap milimeter progresnya mewakili satu kali dzikir yang kamu ucapkan.

Animasinya saya rancang menggunakan Canvas API dengan bezier curve yang sangat halus. Bukan gerakan linear yang kaku — tapi easing yang organik, seperti napas. Cincin itu seolah *bernapas* bersamamu saat berdzikir. Ketika mencapai target, cincin melingkar penuh dan ada animasi pulse gentle yang seolah merayakan pencapaianmu tanpa berlebihan. Subtle. Tenang. Penuh makna.

### Rekayasa Getaran Haptic yang Bikin Ketagihan

Nah, ini bagian yang paling saya banggakan dan paling banyak menghabiskan waktu eksperimen. Getaran haptic bukan sekadar "brrt brrt" seperti notifikasi WhatsApp. Ini adalah seni tersendiri.

Saya menggunakan VibrationEffect API dari Android yang memungkinkan kontrol sangat granular atas pola getaran. Bukan cuma on-off, tapi amplitudo — seberapa kuat getarannya — bisa diatur per-milidetik. Bayangkan kamu bisa mendesain "bentuk" sebuah getaran seperti mendesain gelombang suara.

Untuk setiap ketukan tasbih biasa, saya merancang pola yang saya sebut "pearl drop" — getaran sangat singkat (sekitar 15 milidetik) dengan amplitudo medium. Rasanya seperti jari menyentuh butiran tasbih dan melepaskannya. Crisp. Clean. Satisfying.

Tapi yang menarik adalah pola getaran berubah di milestone tertentu. Saat hitungan mencapai kelipatan 33, ada pola "wave" yang lebih panjang — sekitar 40 milidetik dengan amplitudo yang naik lalu turun, seperti gelombang lembut. Ini memberi sinyal tanpa harus melihat layar bahwa kamu sudah menyelesaikan satu siklus.

Dan saat mencapai target akhir — entah itu 33, 99, atau 999 — ada pola "completion bloom" yang lebih elaborate. Tiga pulse berurutan dengan jeda singkat di antaranya, amplitudo naik bertahap. Rasanya seperti... penyelesaian. Seperti meletakkan butiran tasbih terakhir dan merasakan kepuasan batin.

Proses eksperimennya gila sih. Saya literalnya duduk berjam-jam mengutak-atik nilai amplitudo dan durasi, mencoba di berbagai device, meminta teman-teman mencoba dengan mata tertutup dan memberi feedback. "Yang ini terlalu keras." "Yang itu nggak kerasa." "Oo yang ini enak, kayak nge-klik yang satisfying." Trial and error yang panjang, tapi hasilnya — *chef's kiss*.

Secara teknis, implementasinya menggunakan VibrationEffect.createWaveform() untuk pola kompleks dan VibrationEffect.createOneShot() untuk pulse sederhana. Saya membuat sebuah sealed class `TasbihHapticPattern` yang mendefinisikan semua pola sebagai konstanta, sehingga konsisten di seluruh aplikasi. Untuk device yang tidak mendukung amplitude control (API level di bawah 26), ada fallback ke pola on-off sederhana yang tetap memberikan feedback, walau tidak se-nuansa versi premium.

### Preset Target dan Mode Infinite yang Membebaskan

Soal target hitungan, saya menyediakan preset yang sudah familiar — 33, 66, 99, dan 999. Angka-angka ini bukan sembarangan dipilih. 33 adalah jumlah dzikir standar setelah shalat (Subhanallah 33x, Alhamdulillah 33x, Allahu Akbar 33x). 99 terkait dengan Asmaul Husna. 999 untuk mereka yang ingin sesi dzikir lebih panjang dan mendalam.

Tapi ada satu mode lagi yang ternyata justru paling banyak dipakai — mode infinite. Tanpa target. Tanpa batas. Kamu cukup mengetuk dan terus mengetuk selama hatimu masih ingin berdzikir. Angka terus naik tanpa ada titik akhir yang menghentikanmu.

Kenapa mode ini populer? Karena ternyata banyak orang yang merasa tertekan dengan target. "Saya baru 20, masih 13 lagi." Mindset seperti ini justru mengalihkan fokus dari dzikir itu sendiri ke angka. Mode infinite membebaskan. Kamu berdzikir sampai hatimu merasa cukup, lalu berhenti. Simple.

Dari sisi UX, saat mode infinite aktif, cincin progres berubah menjadi animasi loop yang terus berputar tanpa titik akhir — seperti infinity symbol yang bergerak. Visual reminder bahwa tidak ada finish line, yang ada hanyalah perjalanan.

### Cerita dari Pengguna yang Bikin Saya Terharu

Salah satu momen paling berkesan selama development adalah saat beta testing. Saya minta beberapa teman untuk mencoba fitur tasbih ini dengan instruksi sederhana — "Coba pakai sambil merem."

Ada seorang teman, sebut saja Mas Budi, yang biasanya pakai tasbih fisik tapi sering kehilangan hitungan karena pikirannya kemana-mana. Dia mencoba fitur ini sambil berbaring di tempat tidur sebelum tidur, mata terpejam, hanya mengandalkan getaran sebagai feedback.

WhatsApp-nya ke saya malam itu masih saya simpan sampai sekarang. "Bro, ini gila sih. Gue dzikir 99 tadi tuh kayak meditasi. Getarannya pas banget, kayak gue megang tasbih beneran. Pas nyampe 33 ada getaran beda, gue tau tanpa buka mata. Pas selesai 99, getaran akhirnya kayak ngasih tau 'udah, istirahat.' Gue hampir ketiduran dalam keadaan dzikir. Terbaik."

Pesan itu menguatkan keyakinan saya bahwa teknologi haptic memang punya tempat dalam pengalaman ibadah digital. Bukan menggantikan tasbih fisik — tapi menjadi alternatif yang powerful saat tasbih fisik tidak tersedia.

Ada juga seorang ibu yang cerita lewat review Play Store bahwa beliau menggunakan fitur ini saat menunggu anak di sekolah. Duduk di mobil, mata terpejam, berdzikir dengan bantuan getaran halus smartphone. "Waktu nunggu yang biasanya bosan, sekarang jadi waktu paling tenang dalam hari saya," tulisnya. Membaca itu, saya merasa semua waktu yang dihabiskan untuk fine-tuning pola getaran benar-benar worth it.

## Pemutar Murottal dengan Sorotan Ayat Berjalan yang Bikin Merinding

Kalau tasbih digital itu tentang sentuhan, maka pemutar murottal ini tentang pendengaran — dan visual yang berjalan seirama. Bayangkan kamu membaca mushaf digital, lalu audio murottal mulai mengalun, dan setiap ayat yang sedang dibacakan oleh qari itu otomatis ter-highlight. Mata mengikuti, telinga mendengarkan, hati meresapi. Multi-sensory experience yang bikin bulu kuduk merinding.

Kedengarannya simpel kan? Tapi di balik layar, ini adalah salah satu fitur paling kompleks secara teknis di seluruh SHL Quran Pro.

### Deep Dive ke Media3 ExoPlayer

Untuk audio playback, saya menggunakan Media3 ExoPlayer — library media player paling robust di ekosistem Android. Kenapa bukan MediaPlayer bawaan Android? Karena MediaPlayer itu seperti mobil standar — bisa jalan, tapi terbatas. ExoPlayer itu seperti mobil balap yang bisa kamu custom setiap komponennya.

ExoPlayer memberikan kontrol granular atas buffering, caching, dan yang paling penting — progress tracking yang akurat hingga level milidetik. Akurasi ini krusial untuk fitur highlighting ayat, karena perbedaan 200 milidetik saja bisa membuat highlight bergeser ke ayat yang salah.

Integrasi Media3 juga berarti kita mendapat MediaSession secara gratis. MediaSession ini yang memungkinkan kontrol dari lockscreen, notification, dan bahkan dari perangkat bluetooth. Jadi kamu bisa mulai memutar murottal, mengunci layar, dan tetap mengontrol playback dari notification shade atau dari earphone bluetooth-mu.

### Mekanisme Sinkronisasi Sorotan Per Ayat

Ini bagian yang paling tricky. Setiap surah yang dibacakan oleh setiap qari punya timing yang berbeda-beda. Al-Fatihah yang dibacakan Mishary Alafasy punya timing per-ayat yang berbeda dari versi As-Sudais. Tidak ada standar universal.

Solusinya? Timing metadata per ayat per qari. Setiap file audio murottal dilengkapi dengan data JSON yang berisi timestamp mulai dan selesai untuk setiap ayat. Data ini yang menghubungkan dunia audio dengan dunia visual.

Saat ExoPlayer memutar audio, ada sebuah coroutine yang terus-menerus memonitor posisi playback (menggunakan `player.currentPosition`) dan mencocokkannya dengan timing metadata. Saat posisi memasuki range sebuah ayat baru, event dikirim melalui StateFlow ke UI layer, yang kemudian menggeser highlight ke ayat yang tepat.

Highlight-nya sendiri bukan sekadar background color biasa. Ini adalah animasi gradient yang fade in secara halus — dari transparan ke gold semi-transparan — sehingga perpindahan antar ayat terasa smooth, bukan patah-patah. Ada juga auto-scroll yang memastikan ayat yang sedang di-highlight selalu visible di viewport, dengan smooth scrolling yang tidak mengagetkan mata.

### Background Playback dan Kontrol Lockscreen

Salah satu keluhan paling umum tentang aplikasi murottal yang ada di pasaran adalah playback yang berhenti saat layar mati atau saat pindah aplikasi. "Saya lagi dengerin Al-Mulk sebelum tidur, pas layar mati suaranya ikut mati." Frustrasi banget kan?

Di SHL Quran Pro, murottal berjalan di sebuah foreground service yang terpisah dari UI. Artinya, bahkan kalau kamu close aplikasinya, audio tetap mengalun. Di lockscreen, ada notification controls lengkap — play/pause, next ayat, previous ayat, dan nama surah plus ayat yang sedang dibaca.

Implementasi foreground service ini harus hati-hati. Android semakin ketat soal background execution, terutama dari Android 12 ke atas. Saya harus memastikan service dimulai dengan benar, notification channel terdaftar dengan tepat, dan ada handling yang proper saat system mencoba menghentikan service karena memory pressure.

### Mode Repeat Loop untuk Hafalan

Fitur ini lahir dari masukan teman-teman yang sedang program tahfidz. Metode menghafal Al-Quran yang umum adalah mengulang-ulang ayat atau kelompok ayat berkali-kali sampai hafal. Secara tradisional, ini berarti kamu harus terus-menerus menekan tombol replay.

Mode repeat di SHL Quran Pro lebih cerdas dari itu. Kamu bisa memilih range ayat — misalnya ayat 1 sampai 5 dari Surah Al-Baqarah — dan mengatur jumlah pengulangan. 5 kali, 10 kali, 20 kali, atau infinite loop sampai kamu sendiri yang menghentikan. Di antara setiap pengulangan, ada jeda singkat yang bisa diatur durasinya — waktu untukmu mencoba membaca sendiri sebelum audio terulang.

Ada juga opsi "half-speed" yang memperlambat audio tanpa mengubah pitch. Ini sangat membantu untuk ayat-ayat yang panjang atau yang tajwidnya kompleks. Kamu bisa mendengarkan dengan tempo lebih lambat, memahami setiap makhraj huruf, lalu secara bertahap menaikkan kecepatan ke normal.

### Pilihan Qari yang Kamu Sayangi

SHL Quran Pro menawarkan beberapa qari pilihan yang masing-masing punya karakter unik. Mishary Rashid Alafasy dengan bacaannya yang merdu dan penuh perasaan — favorit banyak orang untuk mendengarkan saat istirahat. Abdurrahman As-Sudais, imam Masjidil Haram, dengan bacaan yang berwibawa dan khusyuk. Abdullah Al-Ghamdi yang terkenal dengan tempo sedang yang pas untuk belajar tajwid. Dan Mahmoud Khalil Al-Hushary, sang maestro qira'at yang bacaannya menjadi standar pembelajaran di banyak pesantren.

Setiap qari tersedia untuk seluruh 114 surah. Kamu bisa memilih qari default untuk keseluruhan, atau bahkan mencampur — surah favorit dengan qari favorit. Preferensi ini tersimpan dan sinkron, jadi kamu tidak perlu memilih ulang setiap kali buka aplikasi.

### Sistem Manajemen Download Offline

Streaming itu enak kalau koneksi internet stabil. Tapi kita tahu sendiri, koneksi di Indonesia itu... *bervariasi*. Di masjid kadang WiFi-nya lemot. Di perjalanan mudik, sinyal hilang-muncul. Makanya, fitur download offline itu bukan nice-to-have — ini essential.

Sistem download di SHL Quran Pro dibangun di atas WorkManager, yang menjamin download akan selesai bahkan kalau terjadi interupsi. Kalau koneksi putus di tengah jalan, download otomatis dilanjutkan saat koneksi kembali. Setiap surah yang sudah didownload ditandai dengan ikon khusus, dan kamu bisa mengelola storage — melihat berapa space yang dipakai, menghapus surah yang jarang didengar, atau download batch per juz.

Untuk efisiensi storage, file audio dikompresi dalam format yang optimal tanpa mengorbankan kualitas yang signifikan. Satu juz lengkap memakan sekitar 80-120 MB tergantung qari, yang menurut saya masih sangat reasonable untuk kualitas audio yang ditawarkan.

### Cerita Testing Audio Sync Jam 3 Pagi

Ada satu cerita yang selalu bikin saya senyum sendiri kalau diingat. Selama development fitur highlighting sync ini, saya mengalami bug yang sangat annoying — di beberapa surah tertentu, highlight-nya meleset satu ayat. Sudah di-debug siang hari, tidak ketemu masalahnya.

Akhirnya jam 3 pagi, setelah shalat tahajjud dan nggak bisa tidur lagi, saya buka laptop dan mulai tracing ulang. Ruangan gelap, hanya cahaya layar laptop. Saya putar Surah Ar-Rahman dengan volume rendah sambil nge-log setiap timestamp.

*Ar-Rahman... Al-lamal Quran... Khalaqal insan...* — suara Alafasy mengalun pelan di keheningan malam, sementara mata saya scanning log timestamp di console. Dan tiba-tiba saya menemukan masalahnya — ada off-by-one error di parser timing metadata. Ayat pertama dihitung dari index 0 di data JSON tapi dari index 1 di database lokal. Classic programmer mistake.

Fix-nya cuma satu baris kode. Satu baris. Tapi butuh waktu tiga hari dan satu sesi debugging jam 3 pagi ditemani lantunan Ar-Rahman untuk menemukannya. Ironisnya, saat fix itu di-apply dan saya test ulang — melihat highlight berjalan sempurna seiring bacaan qari — saya merasa itu adalah momen paling indah dalam seluruh proses development SHL Quran Pro. Debugging ibadah ditemani ibadah. Subhanallah.

## Mesin Pencari Cepat dan Generator Kartu Kutipan Ayat Islami

Pernah nggak kamu lagi ngobrol sama teman, terus pengen ngutip ayat Al-Quran tapi lupa ada di surah apa? "Itu lho, yang tentang sabar... yang ada kata *shabr*-nya... surah apa ya?" Situasi ini terjadi lebih sering dari yang kita kira. Dan inilah kenapa mesin pencari yang cepat dan akurat itu penting banget di aplikasi Quran.

### Mesin Pencari Lokal untuk Terjemahan Indonesia

Search engine di SHL Quran Pro bekerja sepenuhnya offline — tidak perlu koneksi internet. Seluruh teks Al-Quran, terjemahan Bahasa Indonesia, dan metadata ayat sudah tersimpan di database lokal menggunakan Room Database dengan FTS (Full-Text Search) yang dioptimasi.

Kamu bisa mencari berdasarkan kata kunci dalam terjemahan Indonesia — ketik "sabar" dan dalam hitungan milidetik muncul semua ayat yang mengandung kata itu dalam terjemahannya. Bisa juga mencari dengan kata Arab yang diketik dalam huruf latin (transliterasi), atau langsung dengan teks Arab.

Hasil pencarian ditampilkan dengan snippet context — potongan terjemahan di sekitar kata yang dicari, dengan highlight pada kata yang match. Setiap hasil bisa langsung di-tap untuk membuka ayat lengkap beserta konteksnya dalam surah. Smooth, cepat, tanpa loading yang bikin frustrasi.

Performa pencarian ini saya optimalkan habis-habisan. Query sederhana selesai dalam waktu di bawah 50 milidetik di device modern. Bahkan di device entry-level, hasilnya muncul dalam waktu kurang dari 200 milidetik. Ini berkat indexing strategy yang tepat dan query optimization di level SQLite.

### Integrasi Tafsir Ringkas dan Asbabun Nuzul

Menemukan ayat itu satu hal. Memahami konteksnya itu hal lain yang sama pentingnya. Makanya, di SHL Quran Pro, setiap ayat dilengkapi dengan tafsir ringkas yang menjelaskan makna ayat dalam bahasa yang mudah dipahami, plus asbabun nuzul (sebab-sebab turunnya ayat) untuk ayat-ayat yang memilikinya.

Tafsir ringkas ini bukan copy-paste dari kitab tafsir yang tebal dan berat bahasa arabnya. Ini adalah ringkasan yang ditulis ulang agar accessible untuk pembaca umum — tetap akurat secara ilmiah, tapi disampaikan dengan bahasa yang jernih dan mudah dicerna. Untuk kamu yang ingin mendalami lebih jauh, ada referensi ke kitab tafsir lengkap yang bisa dijadikan rujukan.

### Generator Kartu Kutipan Ayat

Ini fitur yang ternyata *sangat* disukai pengguna — dan jujur, saya agak surprised betapa populernya. Fitur quote card generator memungkinkan kamu mengubah ayat Al-Quran menjadi gambar yang cantik dan siap dibagikan.

Cara kerjanya simpel. Pilih ayat yang ingin dijadikan quote, pilih template desain (ada beberapa pilihan — minimalist, floral, geometric pattern Islami, gradient modern), dan aplikasi otomatis menghasilkan gambar resolusi tinggi dengan teks Arab, terjemahan, dan referensi surah-ayat yang tertata rapi.

Di balik layar, fitur ini menggunakan Canvas API Android untuk merender text dan ornamen ke Bitmap. Setiap template adalah sebuah konfigurasi yang mendefinisikan font, ukuran, posisi, warna, dan dekorasi background. Rendering terjadi di background thread menggunakan Coroutines, jadi UI tetap responsive bahkan saat menghasilkan gambar resolusi tinggi.

### Sharing Langsung ke Media Sosial

Setelah kartu kutipan dihasilkan, satu tap lagi untuk membagikannya. Tombol share menggunakan Android ShareSheet yang menampilkan semua aplikasi yang bisa menerima gambar — WhatsApp, Instagram Stories, Facebook, Telegram, atau aplikasi lainnya.

Untuk WhatsApp dan Telegram, gambar dikirim dengan caption otomatis yang berisi teks ayat dan referensi. Untuk Instagram Stories, gambar sudah di-size dengan rasio yang tepat untuk story format. Detail kecil yang bikin pengalaman sharing terasa seamless dan thoughtful.

Banyak pengguna yang menggunakan fitur ini untuk berbagi ayat harian di status WhatsApp mereka, atau untuk membuat konten dakwah di Instagram. Dari data analytics, fitur quote card ini di-generate rata-rata ribuan kali per hari. Sebuah ayat Al-Quran, dibalut desain yang cantik, dibagikan dari hati ke hati melalui jalur digital. Kalau itu bukan dakwah era modern, saya nggak tau lagi apa namanya.

## Mahakarya Widget Carousel Jam Shalat di Layar Utama Smartphone

Kalau semua fitur yang sudah saya ceritakan di atas berada *di dalam* aplikasi, maka widget ini adalah fitur yang hidup *di luar* — langsung di homescreen smartphone-mu. Dan biar saya jujur, widget ini mungkin adalah bagian paling menantang secara teknis dari keseluruhan project SHL Quran Pro.

### Arsitektur RemoteViews dan ViewFlipper Multi Halaman Tanpa Kedip

Widget di Android itu... gimana ya menjelaskannya. Kalau membangun UI di dalam aplikasi itu seperti melukis di kanvas besar dengan semua alat yang tersedia, maka membangun widget itu seperti melukis di atas perangko dengan kuas yang cuma tiga jenis. Terbatas *banget*.

Android widget menggunakan RemoteViews — sebuah subset sangat terbatas dari view system Android. Kamu nggak bisa pakai RecyclerView, nggak bisa pakai custom view, nggak bisa pakai sebagian besar animasi yang biasa tersedia di aplikasi normal. Yang ada cuma basic views seperti TextView, ImageView, dan beberapa layout sederhana.

Dalam keterbatasan inilah saya harus membangun widget carousel tiga halaman yang bisa auto-rotate setiap 10 detik. Solusinya? ViewFlipper — salah satu dari sedikit view yang mendukung animasi transisi di RemoteViews.

ViewFlipper ini saya konfigurasi dengan tiga child layout, masing-masing menampilkan informasi berbeda. Transisi antar halaman menggunakan animasi fade yang halus — bukan slide, karena slide transition di RemoteViews sering menyebabkan glitch visual yang jelek.

Masalah terbesar? Flickering. Setiap kali widget di-update (misalnya untuk memperbarui countdown waktu shalat), seluruh RemoteViews harus di-rebuild dan di-apply ulang. Proses ini, kalau tidak ditangani dengan hati-hati, menyebabkan flicker — layar kedip sekilas saat view lama diganti view baru. Sangat mengganggu dan terlihat amatir.

Solusi saya adalah partial update strategy. Alih-alih me-rebuild seluruh widget setiap detik, saya hanya meng-update elemen yang berubah. TextClock (yang akan saya ceritakan sebentar lagi) menangani jam sendiri tanpa perlu update dari app. Countdown waktu shalat di-update setiap menit, bukan setiap detik. Dan transisi halaman carousel ditangani oleh ViewFlipper sendiri — saya cukup mengatur interval dan membiarkannya bekerja.

Hasilnya? Widget yang terasa *hidup* tanpa pernah kedip. Smooth. Seamless. Seperti bagian native dari homescreen.

### Bahasa Desain Obsidian Gold yang Bikin Homescreen Jadi Premium

Sekarang soal tampilan. Widget ini harus cantik. Bukan cantik yang norak atau mencolok, tapi cantik yang *premium*. Yang bikin orang melihat homescreen-mu dan bertanya, "Wah itu widget apa? Keren banget."

Bahasa desain yang saya pilih adalah Obsidian Gold — background gelap dengan aksen emas. Tapi detail implementasinya yang bikin beda.

Corner radius 14dp memberikan kelengkungan yang soft tapi tidak terlalu bulat. Ini angka yang saya dapat setelah mencoba berbagai nilai — 8dp terlalu kotak, 20dp terlalu pil, 14dp *pas*. Ada glassmorphism effect di background — semi-transparan dengan blur, yang membuat widget terasa menyatu dengan wallpaper apapun yang kamu pakai.

Dan border gold 1.5dp dengan warna #80E5A93C. Kenapa #80? Itu alpha 50% — semi-transparan. Border emas full opacity itu terlalu "teriak." Dengan alpha 50%, border ini memberikan kesan emas yang subtle, sophisticated, seperti pinggiran halaman mushaf mewah. Ketebalan 1.5dp cukup untuk terlihat jelas tapi tidak mendominasi.

Konsep desain ini terinspirasi dari pengalaman saya melihat mushaf-mushaf antik di museum. Ada sesuatu yang timeless dari kombinasi hitam yang dalam dan emas yang hangat. Warna-warna ini tidak pernah terasa ketinggalan zaman, tidak pernah terasa norak, dan punya asosiasi natural dengan kesakralan dan kemuliaan.

### Hero Clock 34sp Detik yang Berdetak Tanpa Makan Baterai

Di tengah widget, ada jam digital besar dengan ukuran 34sp, lengkap dengan detik yang berdetak — HH:mm:ss. Setiap detik berubah, smooth, tanpa jeda.

"Tapi bukankah update setiap detik itu boros baterai?" Pertanyaan valid. Dan jawabannya adalah — tidak, kalau kamu melakukannya dengan cara yang benar.

Rahasia saya adalah TextClock. Ini adalah widget bawaan Android yang secara native menangani update waktu. TextClock tidak menggunakan timer atau alarm dari app — dia terhubung langsung ke system clock Android. Artinya, update setiap detik ditangani di level system, bukan di level aplikasi. Dampak baterainya? Praktis nol. Literally nol tambahan dibanding kalau kamu tidak punya widget sama sekali.

Ini berbeda dari pendekatan naif di mana developer menggunakan AlarmManager atau Handler untuk meng-update TextView setiap detik. Pendekatan itu memang boros baterai karena harus membangunkan aplikasi setiap detik. TextClock menghindari semua itu dengan cara yang elegan.

Format yang saya gunakan adalah HH:mm:ss dengan font monospace agar digit tidak "loncat-loncat" saat berubah. Warna emas yang sama dengan border, tapi dengan full opacity untuk visibility. Detik yang berdetak memberikan kesan bahwa widget ini *hidup* — bukan gambar statis, tapi sesuatu yang bernapas di homescreen-mu.

### Auto Rotator Sepuluh Detik Weton Hijriah dan Mutiara Hadits

Widget tiga halaman ini berisi informasi yang berrotasi setiap 10 detik. Siklus pertama menampilkan informasi waktu — tanggal Masehi, tanggal Hijriah, dan weton Jawa. Siklus kedua menampilkan jadwal shalat. Siklus ketiga menampilkan mutiara hadits atau quote Islami yang berubah setiap hari.

Soal weton Jawa, ini adalah sentuhan kultural yang saya sangat hargai. Weton — kombinasi hari dalam kalender Jawa (Pon, Wage, Kliwon, Legi, Pahing) dengan hari Masehi — adalah bagian dari identitas budaya Jawa yang semakin jarang diketahui generasi muda. Dengan menampilkannya di widget, saya berharap bisa membantu melestarikan pengetahuan ini secara natural.

Tanggal Hijriah dihitung menggunakan library Umm al-Qura Calendar yang akurat. Penting untuk diingat bahwa kalender Hijriah itu tidak seuniform kalender Masehi — ada variasi regional dan perbedaan metode penentuan awal bulan. Library yang saya gunakan mengikuti standar yang paling banyak diterima, dan untuk keperluan informasi umum di widget, akurasinya sudah sangat memadai.

Mutiara hadits di halaman ketiga diambil dari database lokal yang berisi ratusan hadits pilihan dari Sahih Bukhari dan Muslim, lengkap dengan terjemahan Indonesia. Setiap hari, satu hadits baru ditampilkan — seperti kalender harian, tapi di homescreen-mu. Banyak pengguna yang bilang ini adalah hal pertama yang mereka baca saat mengambil HP di pagi hari.

### Lima Kolom Waktu Shalat dengan Countdown Aktif yang Cantik

Halaman jadwal shalat menampilkan lima kolom — Subuh, Dzuhur, Ashar, Maghrib, Isya — masing-masing dengan ikon yang merepresentasikan posisi matahari. Subuh mendapat ikon bulan sabit, Dzuhur ikon matahari penuh di atas, Ashar ikon matahari condong, Maghrib ikon matahari terbenam, dan Isya ikon bintang.

Ikonografi ini bukan sembarang dekorasi. Ini adalah visual mnemonics yang membantu otak langsung mengenali waktu shalat yang dimaksud tanpa harus membaca teks. Dalam ukuran widget yang kecil, efisiensi visual seperti ini sangat penting.

Waktu shalat yang sedang aktif — yaitu yang countdown-nya sedang berjalan — mendapat highlight khusus. Background-nya sedikit lebih terang, dan ada label countdown yang menunjukkan berapa jam dan menit lagi menuju waktu shalat berikutnya. "2j 14m lagi menuju Ashar." Informasi ini ter-update otomatis dan memberikan awareness yang gentle tentang waktu ibadah tanpa harus membuka aplikasi.

Deteksi waktu shalat aktif dilakukan dengan membandingkan waktu saat ini dengan jadwal shalat hari ini. Saat waktu melewati satu shalat dan belum memasuki shalat berikutnya, shalat berikutnya menjadi "aktif" dan di-highlight. Logic sederhana, tapi dampaknya besar — kamu selalu tahu waktu shalat terdekat tanpa effort apapun.

## Kisah Lengkap Membangun Qodho Reminder dari Kegelisahan Batin

Kalau SHL Quran Pro adalah tentang menghadirkan Al-Quran ke genggaman tangan dengan cara yang indah dan powerful, maka Qodho Reminder lahir dari tempat yang berbeda — dari kegelisahan. Kegelisahan yang sangat personal dan sangat real.

### Akar Masalah Hutang Ibadah yang Sering Bikin Waswas

Mari kita bicara tentang sesuatu yang jarang dibahas secara terbuka tapi dirasakan oleh banyak Muslim — hutang ibadah. Shalat yang pernah ditinggalkan, puasa yang pernah bolong. Ini bukan tentang menghakimi. Ini tentang realita kehidupan beragama yang kompleks.

Dalam fikih Islam, keempat madzhab besar — Hanafi, Maliki, Syafi'i, dan Hanbali — sepakat bahwa shalat wajib yang ditinggalkan harus di-qodho (diganti). Ini bukan pilihan, ini kewajiban. Seorang Muslim yang baligh dan berakal, jika meninggalkan shalat — entah karena malas, lupa, sakit berkepanjangan, atau baru mulai menjalankan shalat di usia dewasa — memiliki hutang ibadah yang perlu dilunasi.

Masalahnya ada tiga. Pertama, banyak orang yang bahkan tidak tahu bahwa mereka punya hutang ibadah, atau tidak menyadari betapa besarnya hutang itu. Seseorang yang baru mulai shalat konsisten di umur 25 tahun, misalnya, mungkin memiliki hutang lebih dari 10 tahun shalat — itu hampir 20.000 shalat yang harus di-qodho. Angka yang overwhelming.

Kedua, tracking. Bagaimana cara mencatat progres qodho yang sudah dilakukan? Ingatan manusia tidak reliable untuk angka sebesar itu. Banyak yang mulai mengqodho dengan semangat, tapi kehilangan jejak setelah beberapa minggu karena tidak ada sistem pencatatan yang rapi.

Ketiga, motivasi. Saat kamu tahu hutangmu puluhan ribu shalat, rasanya seperti melihat gunung yang mustahil didaki. Banyak yang akhirnya menyerah sebelum benar-benar mulai, bukan karena malas, tapi karena merasa hopeless.

Saya sendiri merasakan ketiga masalah ini. Dan teman-teman saya juga. Saat saya mulai membicarakan ide Qodho Reminder, responsnya unanimous — "Ini saya banget. Saya butuh ini." Seorang sahabat saya bahkan mencoba tracking qodho-nya di spreadsheet Excel, tapi berhenti setelah sebulan karena terlalu ribet.

Dari sanalah Qodho Reminder lahir. Bukan dari keinginan membuat app yang keren, tapi dari kebutuhan yang sangat nyata dan personal.

### Kalkulator Masa Baligh dan Algoritma Runway Estimasi Tanggal Lunas

Fitur pertama yang saya bangun adalah kalkulator hutang. Konsepnya sederhana — masukkan estimasi umur saat kamu mulai shalat konsisten, dan aplikasi menghitung jumlah hutang shalatmu.

Tapi "sederhana" di level konsep ternyata cukup kompleks di level implementasi. Pertama, kalkulator perlu mengetahui usia baligh pengguna sebagai starting point kewajiban shalat. Standar fikih umumnya 15 tahun untuk laki-laki dan 9 tahun untuk perempuan, tapi ini bisa disesuaikan karena setiap orang berbeda.

Dari tanggal mulai wajib shalat hingga tanggal mulai konsisten shalat, aplikasi menghitung jumlah hari. Setiap hari dikalikan 5 (lima waktu shalat), dikurangi dengan pengecualian — misalnya hari-hari haid bagi perempuan, yang memang dibebaskan dari kewajiban shalat.

Kelima waktu shalat — Subuh, Dzuhur, Ashar, Maghrib, Isya — di-track secara terpisah. Kenapa? Karena pattern orang berbeda-beda. Ada yang dulu sering meninggalkan Subuh tapi rajin shalat yang lain. Ada yang bolong total selama beberapa tahun. Pemisahan ini memberikan fleksibilitas dan akurasi yang lebih tinggi.

Untuk puasa, ada tab terpisah yang menghitung hutang puasa Ramadhan dan fidyah. Logicnya serupa tapi lebih sederhana — jumlah hari puasa yang ditinggalkan dikalikan dengan kewajiban qodho atau fidyah yang berlaku.

Dan inilah fitur yang mungkin paling powerful secara psikologis — runway calculator. Setelah kamu memasukkan data hutang dan mulai mengqodho, aplikasi menghitung estimasi tanggal lunas berdasarkan pace qodho kamu saat ini.

Misalnya, kamu punya hutang 5.000 shalat dan selama sebulan terakhir kamu rata-rata mengqodho 10 shalat per hari. Runway calculator menunjukkan bahwa dengan pace ini, hutangmu akan lunas dalam sekitar 500 hari — kira-kira 1 tahun 4 bulan dari sekarang, tepatnya tanggal sekian bulan sekian.

Melihat tanggal konkret itu mengubah sesuatu secara psikologis. "Puluhan ribu shalat" terasa abstrak dan overwhelming. Tapi "lunas tanggal 15 Desember 2027" terasa *achievable*. Ada titik akhir yang bisa dilihat. Ada cahaya di ujung terowongan. Dan seiring kamu terus mengqodho dan tanggal itu semakin dekat, motivasi meningkat secara natural.

Algoritma runway ini menggunakan moving average dari 30 hari terakhir untuk menghitung pace, sehingga estimasinya realistis dan menyesuaikan dengan ritme hidupmu. Kalau minggu ini kamu lebih rajin, tanggal lunas maju. Kalau minggu depan agak kendor, tanggal mundur sedikit. Dynamic, honest, tapi selalu encouraging.

### Notifikasi Lembut ala Sahabat Hangat Bukan Alarm Menakutkan

Filosofi notifikasi di Qodho Reminder sangat saya pikirkan matang-matang. Ini bukan alarm. Ini bukan teguran. Ini adalah *sapaan hangat dari sahabat*.

Banyak aplikasi ibadah yang menggunakan pendekatan "alarm" — notifikasi yang agresif, insistent, kadang dengan nada menghakimi. "Kamu belum shalat!" "Jangan lupa qodho!" Pendekatan ini mungkin works untuk sebagian orang, tapi bagi banyak orang lain justru kontraproduktif. Orang merasa ditekan, guilty, dan akhirnya malah mengabaikan notifikasi atau bahkan uninstall aplikasinya.

Qodho Reminder mengambil pendekatan sebaliknya. Notifikasinya lembut, hangat, dan supportive. "Hai, udah sempet qodho hari ini? Semangat ya, kamu udah banyak banget progress-nya!" Atau "Shalat qodho yuk, satu aja hari ini juga nggak apa-apa. Setiap langkah berarti."

Tone-nya seperti sahabat yang peduli, bukan guru yang galak. Dan yang penting — notifikasi ini tidak spam. Cukup satu atau dua kali sehari, di waktu yang kamu tentukan sendiri. Kalau kamu sudah log qodho hari itu, notifikasi otomatis berhenti. Respectful terhadap perhatian dan waktu pengguna.

Fitur 1-Tap Fast Log juga lahir dari filosofi yang sama — menghargai waktu pengguna. Saat notifikasi muncul, ada tombol langsung di notification untuk mencatat qodho tanpa perlu membuka aplikasi. Satu tap. Selesai. Shalat Subuh qodho tercatat. Tidak ada form yang harus diisi, tidak ada layar yang harus dinavigasi.

Kalau kamu membuka aplikasi, pencatatan juga dirancang semudah mungkin. Pilih waktu shalat, tap tombol "+1", done. Untuk yang mengqodho lebih dari satu dalam satu waktu, ada opsi "+5" dan "+10" juga. Minim friction, maksimum convenience.

Dan saat kamu mencapai milestone tertentu — 100 shalat qodho, 500, 1000 — ada ucapan selamat yang hangat. "Masya Allah, kamu sudah mengqodho 500 shalat! Itu luar biasa. Istiqomah ya, sedikit demi sedikit." Perayaan kecil yang memberikan dopamine hit positif dan memperkuat habit loop.

### Antarmuka Sage Green dan Emas Tembaga yang Meneduhkan Jiwa

Kalau SHL Quran Pro menggunakan Obsidian Gold yang premium dan commanding, maka Qodho Reminder sengaja mengambil arah desain yang berbeda — Sage Green dan Copper Gold. Dan pemilihan ini sangat deliberate.

Sage green (#B2BFA8 dan variasi terdekatnya) adalah warna yang dalam psikologi warna diasosiasikan dengan ketenangan, penyembuhan, dan alam. Ini bukan hijau yang terang dan energetik seperti lime green. Ini hijau yang lembut, dusty, muted — seperti warna daun sage yang sudah dewasa. Warna ini menenangkan mata dan menurunkan anxiety.

Kenapa ini penting? Karena pengguna Qodho Reminder datang dengan beban emosional. Mereka sadar mereka punya hutang ibadah. Ada rasa bersalah di sana, ada kegelisahan. Warna yang salah bisa memperkuat perasaan negatif ini. Warna sage green dipilih untuk menjadi antidote — "Tenang, ini bukan tempat penghakiman. Ini tempat penyembuhan."

Aksen copper gold (#B87333) melengkapi sage green dengan sentuhan kehangatan. Bukan emas murni yang mewah dan distant, tapi tembaga — lebih earthy, lebih approachable, lebih humble. Kombinasi sage green dan copper gold menciptakan palette yang terasa seperti... memeluk. Hangat tanpa panas. Tenang tanpa dingin.

Filosofi desain keseluruhan Qodho Reminder saya sebut sebagai "Thuma'ninah Design" — diambil dari konsep thuma'ninah dalam ibadah, yang berarti ketenangan dan kekhusyukan. Setiap elemen UI dirancang untuk membawa ketenangan. Corner radius generous yang menghindari sudut tajam. Spacing yang lapang dan tidak sesak. Font yang clean dan readable. Transisi animasi yang halus dan tidak tergesa-gesa.

Bahkan feedback saat mencatat qodho pun dirancang dengan prinsip thuma'ninah. Tidak ada suara "bling!" yang noisy. Yang ada adalah animasi subtle — angka counter naik dengan smooth animation, progress bar bergerak sedikit, dan ada ripple effect halus yang menenangkan. Setiap interaksi dengan aplikasi ini seharusnya menurunkan stress level, bukan menaikkannya.

Room Database menjadi fondasi penyimpanan data di Qodho Reminder. Setiap entry qodho disimpan dengan timestamp, tipe shalat, dan metadata lainnya. StateFlow dari Kotlin Coroutines memastikan UI selalu reaktif terhadap perubahan data — saat kamu mencatat qodho baru, semua angka di dashboard otomatis terupdate tanpa perlu refresh manual.

Aplikasi ini menargetkan minSdk 24 (Android 7.0) untuk menjangkau device sebanyak mungkin, sambil menggunakan compileSdk 36 untuk memanfaatkan API terbaru yang tersedia. Keputusan ini memastikan bahwa Muslim di Indonesia — yang banyak menggunakan device entry-level — tetap bisa mengakses fitur ini tanpa harus punya smartphone terbaru.

Pada akhirnya, baik SHL Quran Pro maupun Qodho Reminder adalah cerminan dari satu keyakinan yang saya pegang teguh — bahwa teknologi, ketika didesain dengan niat yang benar dan perhatian terhadap detail, bisa menjadi jembatan antara kita dan ibadah kita. Bukan menggantikan. Bukan menghalangi. Tapi menjembatani, mempermudah, dan mempercantik perjalanan spiritual kita di era digital ini.

Setiap baris kode yang ditulis, setiap pixel yang ditempatkan, setiap pola getaran yang di-fine-tune — semuanya adalah bentuk ikhtiar kecil untuk memberikan tools terbaik bagi sesama Muslim dalam menjalankan ibadah. Dan kalau dari semua effort ini, ada satu orang saja yang jadi lebih rajin berdzikir karena fitur tasbih, atau ada satu orang yang akhirnya mulai mengqodho hutang shalatnya karena Qodho Reminder membuat prosesnya less overwhelming — maka wallahi, semua begadang dan debugging jam 3 pagi itu terbayar lunas.

Kita lanjut di bagian berikutnya ya, di mana saya akan ceritakan tentang arsitektur teknis yang lebih dalam, performance optimization, dan visi ke depan untuk kedua aplikasi ini. Stay tuned!

## Bedah Arsitektur Database Room dan Manajemen Status Reaktif

Kalau di bagian sebelumnya kita sudah ngobrol panjang lebar soal UI dan desain, sekarang waktunya kita nyelam ke dapur paling dalam dari SHL Quran Pro — yaitu **database**. Ini bagian yang nggak kelihatan sama pengguna, tapi justru jadi fondasi paling kritis. Ibarat rumah, database itu pondasinya. Kalau fondasi rapuh, secantik apapun cat tembok dan hiasan dindingnya, rumah tetap bakal ambruk.

Dan percaya deh, merancang skema database buat aplikasi Quran itu jauh lebih tricky dibanding aplikasi biasa. Kita nggak cuma nyimpen teks biasa — kita nyimpen teks Arab dengan harakat lengkap, metadata tajweed warna-warni, terjemahan multi-bahasa, tafsir panjang, sampai data qodho sholat dan puasa yang butuh presisi tinggi. Semua harus bisa diakses dalam hitungan milidetik. Nggak boleh lemot. Titik.

### Skema Database Mushaf SHL Quran Pro yang Tahan Banting

Oke, mari kita bongkar satu per satu. Database utama Mushaf SHL Quran Pro dibangun di atas **Room Persistence Library** — abstraksi SQLite resmi dari Android Jetpack. Kenapa Room dan bukan SQLite mentah? Karena Room kasih compile-time verification buat query SQL kita, jadi kalau ada typo di nama kolom, langsung ketahuan pas build — bukan pas aplikasi udah di tangan pengguna.

Entity utama kita namanya `QuranAyahEntity`. Ini jantungnya seluruh sistem. Strukturnya kira-kira begini:

```kotlin
@Entity(
    tableName = "quran_ayah",
    primaryKeys = ["surahNumber", "ayahNumber"],
    indices = [
        Index(value = ["surahNumber"]),
        Index(value = ["juzNumber"]),
        Index(value = ["pageNumber"])
    ]
)
data class QuranAyahEntity(
    val surahNumber: Int,
    val ayahNumber: Int,
    val arabicText: String,        // UTF-8 encoded Arabic with full harakat
    val tajweedMetadata: String,   // JSON column for tajweed color mapping
    val translationId: String,     // Indonesian translation
    val translationEn: String?,    // English translation (nullable)
    val tafsirShort: String?,      // Tafsir ringkas
    val tafsirFull: String?,       // Tafsir lengkap
    val juzNumber: Int,
    val pageNumber: Int,
    val hizbQuarter: Int,
    val sajdah: Boolean = false
)
```

Perhatikan beberapa keputusan desain penting di sini.

**Pertama, composite primary key.** Kita pakai kombinasi `surahNumber` dan `ayahNumber` sebagai primary key, bukan auto-generated ID. Kenapa? Karena data Al-Quran itu statis dan universal — Surah Al-Fatihah ayat 1 itu selalu Surah 1 Ayat 1 di manapun di dunia ini. Nggak perlu ID sintetis yang malah bikin query jadi lebih kompleks. Dengan composite key, kita bisa langsung query `WHERE surahNumber = 2 AND ayahNumber = 255` buat dapetin Ayat Kursi tanpa join tambahan.

**Kedua, kolom arabicText pakai UTF-8 encoding penuh.** Ini kelihatannya sepele, tapi pernah bikin pusing tujuh keliling. Teks Arab Al-Quran itu bukan teks biasa — setiap huruf bisa punya harakat (fathah, kasrah, dhammah, tanwin, sukun, tasydid, dan kombinasinya). Satu ayat yang kelihatannya pendek di mata manusia, bisa punya ratusan Unicode code point. SQLite secara default memang support UTF-8, tapi kita harus ekstra hati-hati waktu melakukan operasi string — misalnya `LENGTH()` di SQLite menghitung jumlah byte, bukan jumlah karakter Unicode. Salah pakai fungsi ini bisa bikin pagination teks Arab jadi kacau balau.

**Ketiga, kolom tajweedMetadata menyimpan data JSON.** Ini salah satu keputusan arsitektur yang paling seru. Setiap ayat punya aturan tajweed yang berbeda-beda — di mana harus idgham, di mana ikhfa, di mana iqlab, dan seterusnya. Daripada bikin tabel relasi terpisah yang bakal bikin JOIN bertumpuk-tumpuk, kita simpan metadata tajweed sebagai JSON string langsung di kolom. Formatnya kira-kira begini:

```json
{
  "rules": [
    {"start": 15, "end": 18, "type": "idgham_bighunnah", "color": "#4CAF50"},
    {"start": 22, "end": 25, "type": "ikhfa", "color": "#FF9800"},
    {"start": 31, "end": 33, "type": "qalqalah", "color": "#2196F3"}
  ]
}
```

Setiap rule punya posisi karakter awal dan akhir, tipe tajweed, dan warna yang harus ditampilkan. Pas rendering di Compose, JSON ini di-parse dan dikonversi jadi `AnnotatedString` dengan `SpanStyle` yang sesuai. Hasilnya? Teks Arab yang warna-warni sesuai hukum tajweed, tanpa harus bikin query database tambahan per-kata.

**Keempat, index optimization untuk sub-2ms query.** Lihat anotasi `@Index` di atas. Kita bikin index terpisah untuk `surahNumber`, `juzNumber`, dan `pageNumber`. Ini bukan keputusan sembarangan — ini hasil profiling dengan Android Studio Database Inspector. Tanpa index, query untuk mengambil semua ayat di satu surah butuh sekitar 15-20ms. Dengan index, turun drastis ke 1.2-1.8ms. Kedengarannya nggak signifikan? Coba scroll cepat dari Surah Al-Baqarah ke Surah Ali Imran — setiap kali ganti halaman, query dipanggil. Kalau setiap query butuh 20ms, akan terasa stuttering yang mengganggu. Di 1.5ms? Butter smooth.

Kolom terjemahan dan tafsir juga sengaja dipisah jadi beberapa kolom (`translationId`, `translationEn`, `tafsirShort`, `tafsirFull`). Beberapa di antaranya nullable karena nggak semua ayat langsung punya tafsir lengkap di versi awal. Dengan memisahkan ke kolom berbeda (bukan JSON), kita bisa melakukan `SELECT` hanya kolom yang dibutuhkan — kalau pengguna cuma mau baca teks Arab tanpa terjemahan, kita nggak perlu load string terjemahan yang bisa panjang ke memori.

### Skema Entitas Qodho Reminder yang Fleksibel dan Kokoh

Selain database Mushaf, SHL Quran Pro juga punya fitur pencatat qodho sholat dan puasa. Dan ini ternyata tantangan arsitektur yang sama serunya. Beda dengan data Quran yang statis, data qodho itu dinamis — pengguna bisa menambah, mengedit, menandai selesai, dan melihat riwayat kapan saja.

Ada dua entity utama di sini:

```kotlin
@Entity(tableName = "prayer_qodho")
data class PrayerQodhoEntity(
    @PrimaryKey(autoGenerate = true)
    val id: Long = 0,
    val prayerType: String,        // "subuh", "dzuhur", "ashar", "maghrib", "isya"
    val estimatedDate: Long,       // epoch millis
    val completedDate: Long? = null,
    val isCompleted: Boolean = false,
    val notes: String? = null,
    val createdAt: Long = System.currentTimeMillis(),
    val updatedAt: Long = System.currentTimeMillis()
)

@Entity(tableName = "fasting_qodho")
data class FastingQodhoEntity(
    @PrimaryKey(autoGenerate = true)
    val id: Long = 0,
    val fastingType: String,       // "ramadhan", "sunnah", "nadzar"
    val estimatedDate: Long,
    val completedDate: Long? = null,
    val isCompleted: Boolean = false,
    val reason: String? = null,    // alasan qodho (sakit, haid, dll)
    val notes: String? = null,
    val createdAt: Long = System.currentTimeMillis(),
    val updatedAt: Long = System.currentTimeMillis()
)
```

Perhatikan kalau di sini kita pakai `autoGenerate = true` untuk primary key, berbeda dengan entity Quran tadi. Ini karena data qodho memang butuh ID unik yang auto-increment — satu pengguna bisa punya puluhan bahkan ratusan catatan qodho.

Yang menarik adalah kita juga bikin **transaction log** terpisah untuk melacak setiap perubahan:

```kotlin
@Entity(tableName = "qodho_transaction_log")
data class QodhoTransactionLog(
    @PrimaryKey(autoGenerate = true)
    val logId: Long = 0,
    val entityType: String,     // "prayer" atau "fasting"
    val entityId: Long,
    val action: String,         // "created", "completed", "edited", "deleted"
    val timestamp: Long = System.currentTimeMillis(),
    val previousState: String?  // JSON snapshot sebelum perubahan
)
```

Transaction log ini ternyata sangat berguna pas debugging. Waktu ada laporan dari tester bahwa data qodho-nya "hilang", kita bisa cek log dan ternyata pengguna tanpa sadar menekan tombol hapus (masalah UX yang kemudian kita perbaiki dengan menambahkan konfirmasi dialog). Tanpa log ini, kita bakal bingung sendiri cari penyebabnya.

Semua operasi tulis ke database qodho dilakukan lewat **Coroutines dengan Dispatchers.IO**. Ini prinsip yang harus dipegang teguh — jangan pernah, JANGAN PERNAH, melakukan operasi database di Main Thread. Kalau kita nulis database di Main Thread, UI bakal freeze selama operasi berlangsung. Mungkin cuma 5-10ms, tapi di perangkat low-end bisa sampai 50-100ms. Dan 100ms itu cukup bikin animasi 60 FPS jadi stuttering yang kelihatan.

```kotlin
class QodhoRepository(private val dao: QodhoDao) {

    suspend fun markPrayerCompleted(prayerId: Long) {
        withContext(Dispatchers.IO) {
            val prayer = dao.getPrayerById(prayerId)
            prayer?.let {
                dao.updatePrayer(it.copy(
                    isCompleted = true,
                    completedDate = System.currentTimeMillis(),
                    updatedAt = System.currentTimeMillis()
                ))
                dao.insertLog(QodhoTransactionLog(
                    entityType = "prayer",
                    entityId = prayerId,
                    action = "completed",
                    previousState = Gson().toJson(it)
                ))
            }
        }
    }
}
```

Dengan pola ini, UI thread tetap bebas 100%. Bahkan di perangkat entry-level dengan RAM 2GB, kita bisa target 120 FPS tanpa dropped frame saat operasi database berjalan di background. Pengguna menekan tombol "Selesai" dan langsung melihat animasi centang hijau yang smooth — sementara di belakang layar, coroutine sedang sibuk menulis ke SQLite dan mencatat log transaksi.

### Pola ViewModel dan StateFlow Kebal Rotasi Layar

Nah, ini bagian favorit saya. Salah satu masalah klasik di Android development adalah **data hilang saat layar dirotasi**. Di jaman Activity dan Fragment dulu, setiap kali pengguna memutar HP dari portrait ke landscape, activity dihancurkan dan dibuat ulang. Semua data yang disimpan di variabel biasa langsung hilang. Developer harus repot mengelola `onSaveInstanceState`, dan hasilnya sering buggy.

Di SHL Quran Pro, kita pakai arsitektur **ViewModel + StateFlow** yang elegant dan tahan banting. Kuncinya ada di sealed interface pattern untuk merepresentasikan state UI:

```kotlin
sealed interface QuranUiState {
    data object Loading : QuranUiState
    data class Success(
        val ayahList: List<QuranAyahEntity>,
        val currentPage: Int,
        val totalPages: Int,
        val bookmarks: Set<Int>
    ) : QuranUiState
    data class Error(val message: String) : QuranUiState
}
```

Kenapa sealed interface, bukan sealed class? Di Kotlin modern, sealed interface lebih fleksibel — sebuah class bisa implement multiple sealed interfaces, sedangkan sealed class cuma bisa punya satu parent. Untuk UI state yang kompleks, ini kasih ruang refactoring yang lebih leluasa ke depannya.

Lalu di ViewModel, kita expose state lewat `StateFlow`:

```kotlin
class QuranViewModel(
    private val repository: QuranRepository,
    private val savedStateHandle: SavedStateHandle
) : ViewModel() {

    private val _uiState = MutableStateFlow<QuranUiState>(QuranUiState.Loading)
    val uiState: StateFlow<QuranUiState> = _uiState.asStateFlow()

    private val currentSurah = savedStateHandle.getStateFlow("currentSurah", 1)

    init {
        viewModelScope.launch {
            currentSurah.collectLatest { surahNumber ->
                loadSurah(surahNumber)
            }
        }
    }

    private suspend fun loadSurah(surahNumber: Int) {
        _uiState.value = QuranUiState.Loading
        try {
            val ayahs = withContext(Dispatchers.IO) {
                repository.getAyahsBySurah(surahNumber)
            }
            _uiState.value = QuranUiState.Success(
                ayahList = ayahs,
                currentPage = repository.getPageForSurah(surahNumber),
                totalPages = 604,
                bookmarks = repository.getBookmarkedAyahs(surahNumber).toSet()
            )
        } catch (e: Exception) {
            _uiState.value = QuranUiState.Error(
                message = e.localizedMessage ?: "Terjadi kesalahan"
            )
        }
    }
}
```

Kenapa data selamat dari rotasi layar? Karena **ViewModel memiliki lifecycle yang lebih panjang dari Activity/Fragment**. Saat layar dirotasi dan Activity di-recreate, ViewModel yang sama tetap hidup di memori. StateFlow di dalamnya tetap menyimpan state terakhir. Waktu Activity baru subscribe ke `uiState`, dia langsung dapat nilai terkini tanpa harus fetch ulang dari database.

`SavedStateHandle` memberikan lapisan perlindungan ekstra — bahkan kalau ViewModel dihancurkan karena system kill (misalnya OS kehabisan memori dan membunuh proses aplikasi), state kunci seperti nomor surah terakhir yang dibaca tetap tersimpan dan bisa di-restore.

Di sisi Composable, kita pakai `derivedStateOf` untuk menghindari recomposition yang nggak perlu:

```kotlin
@Composable
fun QuranScreen(viewModel: QuranViewModel = hiltViewModel()) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    val showBookmarkBadge by remember {
        derivedStateOf {
            (uiState as? QuranUiState.Success)?.bookmarks?.isNotEmpty() == true
        }
    }

    when (val state = uiState) {
        is QuranUiState.Loading -> LoadingAnimation()
        is QuranUiState.Success -> AyahList(
            ayahs = state.ayahList,
            showBadge = showBookmarkBadge
        )
        is QuranUiState.Error -> ErrorMessage(state.message)
    }
}
```

`derivedStateOf` ini penting banget. Tanpa dia, setiap kali `uiState` berubah — misalnya ada ayat baru yang di-load — Compose akan meng-evaluate ulang `showBookmarkBadge` DAN me-recompose semua composable yang bergantung padanya. Dengan `derivedStateOf`, Compose cuma me-recompose kalau **hasil kalkulasi** berubah. Jadi kalau bookmark-nya tetap sama meskipun ayat list berubah, composable badge nggak akan di-recompose. Ini bisa menghemat ratusan recomposition per detik saat pengguna scrolling cepat.

## Catatan Perang Lima Drama Perburuan Bug Paling Seru

Sekarang masuk ke bagian yang paling seru untuk diceritakan — dan paling menyakitkan untuk dialami. Lima bug spektakuler yang bikin saya begadang, stress, tapi akhirnya kasih pelajaran yang nggak ternilai.

### Bug Pertama Kebocoran Memori Bitmap Widget yang Bikin Launcher Ngehang

**Gejala awal.** Beberapa tester melaporkan bahwa setelah menambahkan widget SHL Quran Pro ke home screen, launcher mereka jadi lemot. Beberapa bahkan mengalami launcher yang freeze total dan harus restart. Yang bikin bingung, nggak semua tester mengalaminya — hanya yang pakai perangkat dengan RAM 3GB ke bawah.

**Proses investigasi.** Langkah pertama, saya buka Android Studio Profiler dan mulai monitor memory usage. Dan di situ saya lihat angka yang bikin mata melotot — widget kita mengonsumsi **85MB RAM** hanya untuk satu instance. Delapan puluh lima megabyte! Untuk widget Quran yang cuma menampilkan satu ayat!

Saya trace lebih dalam pakai Memory Profiler, dan ketemu biang keladinya — sebuah `Bitmap` beresolusi tinggi yang di-load untuk background widget. Widget kita pakai desain Obsidian Gold yang cantik, dengan background gradient dan pattern islami. Masalahnya, bitmap background ini di-load di resolusi penuh (2048x2048 pixel) setiap kali widget di-update, tanpa scaling ke ukuran widget yang sebenarnya jauh lebih kecil.

Dan lebih parah lagi, bitmap ini nggak pernah di-recycle. Setiap kali `onUpdate()` dipanggil (yang bisa terjadi setiap 30 menit), bitmap baru di-load tanpa membebaskan yang lama. Setelah beberapa jam, memory usage menumpuk menjadi puluhan megabyte.

**Root cause** ternyata ada di kode `RemoteViews` yang terlalu naive:

```kotlin
// KODE BERMASALAH — Jangan ditiru!
fun updateWidget(context: Context, appWidgetId: Int) {
    val bitmap = BitmapFactory.decodeResource(
        context.resources,
        R.drawable.widget_bg_obsidian_gold  // 2048x2048 original
    )
    val views = RemoteViews(context.packageName, R.layout.widget_ayah)
    views.setImageViewBitmap(R.id.widgetBackground, bitmap)
    // bitmap never recycled, loaded at full resolution every time
}
```

**Solusi yang diterapkan.** Tiga langkah perbaikan sekaligus:

```kotlin
fun updateWidget(context: Context, appWidgetId: Int) {
    val options = context.getSystemService(AppWidgetManager::class.java)
        .getAppWidgetOptions(appWidgetId)
    val width = options.getInt(AppWidgetManager.OPTION_APPWIDGET_MAX_WIDTH)
    val height = options.getInt(AppWidgetManager.OPTION_APPWIDGET_MAX_HEIGHT)

    // 1. Calculate inSampleSize for downsampling
    val opts = BitmapFactory.Options().apply {
        inJustDecodeBounds = true
    }
    BitmapFactory.decodeResource(context.resources, R.drawable.widget_bg_obsidian_gold, opts)

    opts.inSampleSize = calculateInSampleSize(opts, width.dpToPx(), height.dpToPx())
    opts.inJustDecodeBounds = false

    // 2. Load scaled bitmap
    val scaledBitmap = BitmapFactory.decodeResource(
        context.resources,
        R.drawable.widget_bg_obsidian_gold,
        opts
    )

    val views = RemoteViews(context.packageName, R.layout.widget_ayah)
    views.setImageViewBitmap(R.id.widgetBackground, scaledBitmap)

    AppWidgetManager.getInstance(context).updateAppWidget(appWidgetId, views)

    // 3. Recycle bitmap after use
    scaledBitmap.recycle()
}
```

**Hasil.** Memory usage widget turun dari **85MB ke 4.2MB** — penurunan 95.1%. Launcher nggak pernah hang lagi, bahkan di perangkat dengan RAM 2GB. Ini juga memperbaiki issue battery drain yang beberapa tester laporkan tapi awalnya nggak saya korelasikan dengan bug ini.

### Bug Kedua Kumandang Adzan Subuh yang Diam Seribu Bahasa

**Gejala.** Fitur pengingat adzan di SHL Quran Pro bekerja sempurna untuk Dzuhur, Ashar, Maghrib, dan Isya. Tapi untuk Subuh? Diam membisu. Nggak ada suara, nggak ada notifikasi, nggak ada apa-apa. Subuh jam 4 pagi, HP diam aja kayak batu.

**Proses investigasi.** Awalnya saya curiga ada bug di kalkulasi waktu sholat. Saya cek — hasilnya benar, waktu Subuh terhitung dengan akurat. Lalu saya curiga `AlarmManager` nggak di-set. Saya cek — alarm terdaftar dengan benar. Jadi kenapa alarm nggak trigger?

Setelah berjam-jam googling dan membaca dokumentasi Android yang super panjang, akhirnya ketemu jawabannya — **Doze Mode**.

Android punya fitur hemat baterai bernama Doze Mode yang aktif ketika HP dalam keadaan diam, layar mati, dan nggak di-charge dalam waktu tertentu. Dan kapan HP paling sering di keadaan ini? Yup, **di malam hari saat kita tidur** — tepat saat alarm Subuh seharusnya berbunyi.

Di Doze Mode, Android menunda hampir semua alarm (`AlarmManager.set()` dan `AlarmManager.setExact()`) ke "maintenance window" yang jadwalnya ditentukan sistem. Artinya alarm Subuh jam 04:30 bisa baru trigger jam 06:00 atau bahkan lebih telat — saat HP keluar dari Doze Mode.

**Solusi bertingkat.** Ini butuh tiga lapis perbaikan.

Pertama, menggunakan `setExactAndAllowWhileIdle()` — API yang memang dirancang untuk alarm yang harus berbunyi bahkan di Doze Mode:

```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
    if (alarmManager.canScheduleExactAlarms()) {
        alarmManager.setExactAndAllowWhileIdle(
            AlarmManager.RTC_WAKEUP,
            triggerTimeMillis,
            pendingIntent
        )
    }
}
```

Kedua, karena mulai Android 12 (API 31) kita butuh permission `SCHEDULE_EXACT_ALARM`, kita tambahkan di Manifest dan handle kasus di mana user belum memberikan permission:

```xml
<uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM" />
```

Ketiga, sebagai failsafe tambahan, kita jalankan **Foreground Service** beberapa menit sebelum waktu Subuh. Foreground Service punya privilege khusus di Android — dia bisa tetap berjalan bahkan di Doze Mode, asalkan menampilkan persistent notification.

```kotlin
class SubuhAlarmService : Service() {
    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        val notification = buildNotification("Mempersiapkan pengingat Subuh...")
        startForeground(NOTIFICATION_ID, notification)

        // Schedule the actual adzan notification
        scheduleAdzanNotification()

        return START_STICKY
    }
}
```

Setelah tiga lapis perbaikan ini, adzan Subuh akhirnya konsisten berbunyi di semua perangkat test. Nggak ada lagi laporan alarm Subuh yang diam.

### Bug Ketiga Harakat Arab Bertumpukan di Layar Rasio Panjang

**Gejala.** Teks Arab di beberapa perangkat tampil dengan harakat yang bertumpukan — fathah, kasrah, dan tanwin saling menimpa sehingga nggak bisa dibaca. Anehnya, di mayoritas perangkat tampil normal.

**Investigasi.** Setelah mengumpulkan data dari tester, saya sadari ada pola — semua perangkat bermasalah punya layar dengan rasio **21:9** atau lebih panjang. Perangkat seperti Sony Xperia dan beberapa HP Samsung seri tertentu. Layar super panjang ini menghasilkan lebar layout yang lebih sempit dari biasanya, sehingga teks Arab yang punya harakat tinggi-tinggi ke atas jadi saling bertabrakan antar baris.

Masalahnya ada di line-height yang statis. Kita awalnya pakai `lineHeight` fixed di Compose:

```kotlin
Text(
    text = arabicText,
    style = TextStyle(
        fontSize = 28.sp,
        lineHeight = 48.sp  // static — tidak cukup untuk layar 21:9
    )
)
```

**Solusi.** Kita bikin **Dynamic Line-Height Calculator** yang menyesuaikan line-height berdasarkan rasio layar dan ukuran font:

```kotlin
@Composable
fun rememberDynamicLineHeight(fontSize: TextUnit): TextUnit {
    val configuration = LocalConfiguration.current
    val screenRatio = configuration.screenHeightDp.toFloat() / configuration.screenWidthDp.toFloat()

    return remember(fontSize, screenRatio) {
        when {
            screenRatio > 2.2f -> fontSize * 2.1f   // ultra-wide 21:9+
            screenRatio > 2.0f -> fontSize * 1.9f   // tall 20:9
            screenRatio > 1.8f -> fontSize * 1.8f   // standard 19.5:9
            else -> fontSize * 1.7f                   // classic 16:9
        }
    }
}
```

Sekarang teks Arab tampil cantik di semua rasio layar — dari tablet 4:3 sampai HP ultra-panjang 21:9. Harakat nggak pernah bertabrakan lagi.

### Bug Keempat Auto Rotator Widget yang Mogok Kerja Setelah Tiga Jam

**Gejala.** Widget "Ayat Harian" yang harusnya ganti ayat setiap 30 menit, berhenti berganti setelah sekitar 3 jam. Widget tetap menampilkan ayat terakhir yang dirotasi — nggak crash, nggak error, tapi diam aja nggak mau update.

**Investigasi.** Bug ini tricky karena nggak konsisten — kadang terjadi setelah 2 jam, kadang 4 jam, kadang malah jalan seharian tanpa masalah. Setelah saya pasang logging extensif, ditemukan bahwa widget berhenti update ketika **Android Low Memory Killer** membunuh proses aplikasi di background.

Awalnya kita pakai `AlarmManager` untuk menjadwalkan update widget setiap 30 menit. Tapi alarm yang dijadwalkan oleh sebuah proses akan musnah begitu proses itu dibunuh OS. Dan di perangkat dengan RAM kecil, proses background sering dibunuh dalam hitungan jam.

**Solusi dua lapis.** Pertama, migrasi dari `AlarmManager` ke **WorkManager** — sistem scheduling dari Android Jetpack yang persist bahkan setelah proses dihancurkan:

```kotlin
class WidgetRotatorWorker(
    context: Context,
    params: WorkerParameters
) : CoroutineWorker(context, params) {

    override suspend fun doWork(): Result {
        val nextAyah = getRandomAyah()
        updateAllWidgets(applicationContext, nextAyah)
        return Result.success()
    }
}

// Scheduling
val workRequest = PeriodicWorkRequestBuilder<WidgetRotatorWorker>(
    30, TimeUnit.MINUTES,
    5, TimeUnit.MINUTES  // flex interval
).setConstraints(
    Constraints.Builder()
        .setRequiresBatteryNotLow(true)
        .build()
).build()

WorkManager.getInstance(context).enqueueUniquePeriodicWork(
    "widget_rotator",
    ExistingPeriodicWorkPolicy.KEEP,
    workRequest
)
```

Kedua, sebagai backup, kita juga register `BroadcastReceiver` untuk `ACTION_TIME_TICK` — broadcast yang dikirim sistem setiap menit. Kalau kita deteksi sudah lebih dari 35 menit sejak update terakhir, kita trigger update manual:

```kotlin
class TimeTickReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        if (intent.action == Intent.ACTION_TIME_TICK) {
            val lastUpdate = PrefsHelper.getLastWidgetUpdate(context)
            if (System.currentTimeMillis() - lastUpdate > 35 * 60 * 1000) {
                // WorkManager missed? Force manual update
                WidgetUpdater.forceUpdate(context)
            }
        }
    }
}
```

Dengan dua mekanisme ini, widget sekarang konsisten berganti ayat setiap 30 menit — bahkan setelah seharian, bahkan di perangkat dengan RAM 2GB yang agresif membunuh proses background.

### Bug Kelima Recomposition Loop Tasbih yang Bikin CPU Kebakaran

**Gejala.** Seorang tester mengirim screenshot yang menunjukkan baterai HP-nya turun 15% dalam 10 menit pakai fitur tasbih counter. Saya buka Android Studio Profiler dan lihat **CPU usage di 90%** — untuk halaman yang cuma menampilkan satu angka dan satu tombol!

**Investigasi.** CPU Profiler menunjukkan bahwa Compose melakukan **ribuan recomposition per detik** di halaman tasbih. Setiap kali counter bertambah 1, hampir semua composable di layar di-recompose ulang — termasuk background gradient, header teks, dan animasi lingkaran yang seharusnya nggak berubah.

Root cause-nya ternyata di cara kita menyimpan state tasbih:

```kotlin
// KODE BERMASALAH
@Composable
fun TasbihScreen() {
    var count by remember { mutableStateOf(0) }
    var target by remember { mutableStateOf(33) }

    // Problem: creating new object every recomposition
    val progress = TasbihProgress(count, target, count.toFloat() / target)

    TasbihCircle(progress = progress)      // recompose setiap kali!
    TasbihCounter(count = count)            // recompose setiap kali!
    TasbihButton(onClick = { count++ })     // recompose setiap kali!
}

// This class is NOT @Stable — Compose can't prove it's stable
data class TasbihProgress(
    val current: Int,
    val target: Int,
    val percentage: Float
)
```

Masalahnya ada dua. Pertama, `TasbihProgress` dibuat ulang setiap recomposition — dan karena itu object baru (referensi berbeda), Compose menganggap parameter `progress` berubah dan harus me-recompose `TasbihCircle`. Kedua, class `TasbihProgress` nggak di-anotasi `@Stable`, jadi Compose nggak bisa membuktikan bahwa dua instance dengan nilai yang sama itu "equal" untuk keperluan skip recomposition.

**Solusi.** Kombinasi `@Stable` annotation dan `derivedStateOf`:

```kotlin
@Stable
data class TasbihProgress(
    val current: Int,
    val target: Int,
    val percentage: Float
)

@Composable
fun TasbihScreen() {
    var count by remember { mutableStateOf(0) }
    var target by remember { mutableStateOf(33) }

    val progress by remember {
        derivedStateOf {
            TasbihProgress(count, target, count.toFloat() / target)
        }
    }

    TasbihCircle(progress = progress)
    TasbihCounter(count = count)
    TasbihButton(onClick = { count++ })
}
```

Dengan `@Stable`, Compose tahu bahwa `TasbihProgress` bisa di-compare by value. Dengan `derivedStateOf`, object `progress` cuma dihitung ulang kalau `count` atau `target` berubah — dan referensinya tetap stabil di antara recomposition. Hasil akhir? CPU usage turun dari **90% ke 5%**. Battery drain hilang. Tester yang tadinya komplain sekarang malah pakai fitur tasbih berjam-jam tanpa masalah.

### Pelajaran Emas dari Setiap Bug yang Berhasil Ditaklukkan

Kelima bug di atas mengajarkan satu hal yang sama — **bug terbaik adalah guru terbaik**. Setiap malam begadang melacak memory leak, setiap jam frustasi karena alarm nggak berbunyi, setiap sesi profiling yang membingungkan — semua itu meninggalkan pelajaran yang jauh lebih dalam dari tutorial mana pun.

Dari bug bitmap, saya belajar bahwa **resource management bukan opsional** — itu wajib, terutama di platform yang memory-constrained seperti Android. Dari bug Doze Mode, saya belajar bahwa Android **selalu berubah** dan asumsi yang valid di API 21 bisa salah total di API 33. Dari bug harakat, saya belajar pentingnya **testing di berbagai form factor** — bukan cuma di emulator default. Dari bug widget, saya belajar bahwa proses background itu **fana** — OS bisa membunuhnya kapan saja, dan kode kita harus tahan terhadap kematian itu. Dan dari bug recomposition, saya belajar bahwa **Compose yang terlihat sederhana bisa sangat berbahaya** kalau kita nggak paham bagaimana recomposition bekerja di level internal.

Debugging itu bukan tanda kode kita jelek. Debugging itu tanda kita sedang membangun sesuatu yang cukup kompleks untuk memiliki bug yang menarik. Dan setiap bug yang berhasil ditaklukkan membuat kita developer yang lebih tajam, lebih waspada, dan lebih humble.

## Riwayat Perjalanan Versi dari Alfa Sampai Rilis Kandidat

Setiap versi yang di-release punya ceritanya sendiri. Ini bukan cuma changelog kering berisi daftar fitur — ini catatan perjalanan hati seorang developer yang berjuang membangun sesuatu dari nol.

### Versi 1.0.0 Alpha Fondasi Pertama dan Debaran Awal

Versi alfa pertama ini ibarat bayi yang baru lahir — belum cantik, belum rapi, tapi sudah bisa bernapas dan berteriak.

**Fitur yang masuk di v1.0.0 Alpha:**

- ✅ Mushaf digital lengkap 30 juz, 114 surah, 6.236 ayat
- ✅ Teks Arab UTF-8 dengan harakat lengkap
- ✅ Navigasi per-surah dasar
- ✅ Tampilan mode gelap default
- ✅ Arsitektur MVVM dasar dengan Room database
- ✅ minSdk 24 untuk menjangkau 98.5% perangkat aktif

Yang belum ada di versi ini jauh lebih banyak dari yang sudah ada. Belum ada terjemahan, belum ada tajweed warna, belum ada widget, belum ada notifikasi. Tapi versi inilah yang memberikan **debaran pertama** — perasaan melihat Surah Al-Fatihah tampil di layar HP untuk pertama kalinya dari kode yang kita tulis sendiri. Momen itu rasanya magis, dan saya ingat duduk terdiam memandangi layar selama beberapa menit, membaca Basmalah yang ditrender sempurna oleh code buatan sendiri.

### Versi 1.1.0 Beta Murottal Haptic dan Suara yang Menghidupkan

Kalau v1.0.0 adalah fondasi, v1.1.0 adalah nafas pertama yang menghidupkan.

**Fitur baru di v1.1.0 Beta:**

- ✅ Terjemahan Bahasa Indonesia untuk seluruh ayat
- ✅ Tajweed metadata dengan color coding 7 hukum bacaan
- ✅ Haptic feedback untuk setiap tap navigasi
- ✅ Audio murottal streaming untuk setiap ayat
- ✅ Pencarian ayat dengan query Bahasa Indonesia
- ✅ Bookmark ayat favorit dengan sync lokal
- ✅ Catatan pribadi per-ayat
- ✅ Perbaikan 23 bug dari fase alfa

Penambahan haptic feedback ternyata mengubah feel aplikasi secara dramatis. Setiap kali berpindah halaman mushaf, ada getaran halus yang terasa seperti **membalik halaman mushaf fisik**. Kecil tapi impactful. Beberapa tester yang awalnya biasa-biasa saja jadi mulai berkomentar "Wah, ini beda ya rasanya dari app Quran lain."

Audio murottal juga punya cerita tersendiri. Streaming audio per-ayat ternyata bukan perkara sederhana — kita harus handle network timeout, buffering state, cache management, dan seamless transition antar ayat supaya pendengar nggak terganggu gap atau glitch di antara ayat.

### Versi 1.2.0 Beta Kelahiran Widget Obsidian Gold yang Ikonik

Inilah versi yang melahirkan bintang baru — widget Obsidian Gold yang jadi identitas visual SHL Quran Pro.

**Fitur baru di v1.2.0 Beta:**

- ✅ Widget Home Screen "Ayat Harian" dengan desain Obsidian Gold
- ✅ Auto-rotator widget setiap 30 menit
- ✅ Tema Obsidian Gold untuk keseluruhan aplikasi
- ✅ Fitur Qodho Sholat tracker
- ✅ Fitur Qodho Puasa tracker
- ✅ Tasbih digital counter dengan animasi lingkaran
- ✅ Statistik bacaan harian
- ✅ Perbaikan memory leak widget (85MB → 4.2MB)
- ✅ Perbaikan 15 bug dari beta pertama

Widget Obsidian Gold ini awalnya cuma eksperimen desain iseng. Saya lagi scrolling Pinterest lihat-lihat desain luxury brand, terus kefikiran "gimana kalau widget Quran tampilannya se-elegan itu?" Hasilnya ternyata melampaui ekspektasi — gradient gold-to-dark dengan typography Arab yang elegan menjadi elemen yang paling sering di-screenshot dan dibagikan tester ke media sosial.

Fitur qodho dan tasbih juga lahir dari masukan komunitas. Beberapa tester bilang "seandainya ada pencatat qodho di sini, jadi nggak perlu buka app terpisah." Dan kami dengarkan. Dua minggu coding intensif, dua fitur baru lahir.

### Versi 1.3.0 Release Candidate Polesan Akhir Sebelum Ujian

Release Candidate — dua kata yang bermakna "ini sudah siap, tapi sekali lagi kita periksa sebelum diujicobakan ke dunia luar."

**Fitur dan perbaikan di v1.3.0 RC:**

- ✅ Pengingat adzan 5 waktu dengan Doze Mode bypass
- ✅ Dynamic Line-Height Calculator untuk semua rasio layar
- ✅ Foreground Service adzan Subuh failsafe
- ✅ WorkManager widget rotator anti-mati
- ✅ Recomposition optimization — CPU usage turun 94%
- ✅ Tafsir ringkas untuk ayat-ayat pilihan
- ✅ Animasi transisi halaman mushaf yang lebih smooth
- ✅ Accessibility improvements — TalkBack support dasar
- ✅ compileSdk dinaikkan ke 36
- ✅ Perbaikan total 41 bug dari seluruh fase sebelumnya

Versi ini adalah buah dari semua pelajaran bug yang sudah diceritakan di atas. Setiap fix yang hard-earned sekarang tertanam kuat di kode. Ini bukan versi yang paling banyak fitur baru, tapi versi yang paling **matang dan stabil**. Dan itulah yang dibutuhkan untuk menghadapi ujian terbesarnya — Closed Testing di Google Play Console.

## Petualangan Seru Menembus Ujian Closed Testing di Google Play Console

Kalau membangun aplikasinya sudah bikin deg-degan, proses publishing ke Google Play justru membawa level kecemasan baru yang sama sekali berbeda.

### Aturan Ketat 20 Penguji 14 Hari yang Bikin Deg-degan

Google punya aturan yang cukup ketat untuk developer baru yang mau publish aplikasi pertama mereka. Salah satu yang paling bikin nerveous adalah **program Closed Testing** — sebelum aplikasi bisa dipublikasi ke publik, developer harus menjalankan program testing tertutup dengan minimal **20 penguji aktif** selama **14 hari berturut-turut**.

Angka 20 penguji ini bukan sekadar formalitas. Google benar-benar mengecek apakah 20 orang yang berbeda sudah menginstal dan menjalankan aplikasi selama periode tersebut. Kalau kurang dari 20, atau kalau periode belum 14 hari, tombol "Publish to Production" tetap abu-abu dan nggak bisa diklik.

Kenapa Google menerapkan ini? Untuk memastikan bahwa aplikasi sudah diuji oleh manusia sungguhan di perangkat sungguhan sebelum dijual ke jutaan pengguna. Ini filter quality yang, meskipun bikin repot, sebenarnya sangat masuk akal.

### Strategi Merekrut 25 Sahabat Penguji Setia

Dua puluh penguji. Kedengarannya gampang? Coba pikirin — kita butuh 20 orang yang bersedia menginstal APK kita, menjalankannya setiap hari selama dua minggu, dan yang terpenting, **benar-benar melakukannya** dan bukan cuma bilang "iya nanti ya."

Saya mulai dari lingkaran terdekat. Lima orang teman kuliah yang saya tahu pasti bisa diandalkan. Lalu tiga orang dari keluarga — adik, kakak, dan sepupu yang hobi ngulik HP. Empat orang teman dari organisasi kampus yang kebetulan tertarik sama tech. Lima orang dari komunitas masjid yang sudah familiar dengan konsep aplikasi Quran digital. Dan delapan orang lagi dari berbagai grup WhatsApp — teman SMA, kenalan freelance, dan beberapa follower media sosial yang antusias.

Total 25 orang, sengaja lebih dari 20 sebagai buffer. Pengalaman mengajarkan bahwa pasti ada yang drop di tengah jalan — HP rusak, lupa, atau kehilangan minat. Dengan buffer 5 orang, kita aman.

### Membagikan APK Lewat Jalur Resmi Closed Testing Track

Google mewajibkan distribusi lewat jalur resmi Play Console, bukan sideloading APK lewat WhatsApp atau Telegram. Prosesnya melibatkan beberapa langkah:

Pertama, membuat **Google Group khusus** untuk tester. Semua 25 email tester ditambahkan ke grup ini. Kedua, di Play Console, membuat **Closed Testing Track** baru dan menghubungkannya dengan Google Group tadi. Ketiga, upload AAB (Android App Bundle) ke track tersebut. Keempat, mengirimkan link opt-in khusus ke semua tester — mereka harus klik link ini untuk "mendaftar" sebagai tester sebelum bisa mendownload dari Play Store.

Yang sering bikin bingung tester adalah proses opt-in ini. Beberapa mengira mereka sudah bisa langsung download setelah ditambahkan ke Google Group, padahal masih harus klik link opt-in terlebih dahulu. Saya sampai bikin tutorial screenshot step-by-step di Google Docs dan bagikan ke grup WhatsApp koordinasi.

### Jurus Menjaga Keaktifan Tester Harian Selama Dua Minggu

Ini tantangan terbesar. Merekrut 25 orang itu satu hal. Menjaga mereka tetap aktif **setiap hari** selama 14 hari itu level kesulitan yang jauh lebih tinggi.

Strategi saya bisa dibilang mirip game master yang menjaga engagement pemain. Setiap hari di grup WhatsApp koordinasi, saya kirim **"Misi Harian"** — tugas-tugas kecil yang menarik untuk dilakukan:

- Hari 1 → "Buka Surah Al-Mulk dan baca sampai akhir, screenshot halaman terakhirnya"
- Hari 3 → "Coba fitur tasbih, buat rekor 100x dan screenshot animasinya"
- Hari 5 → "Tambah widget ke home screen, kirim foto home screen kalian"
- Hari 7 → "Cari ayat tentang sabar pakai fitur pencarian"
- Hari 10 → "Catat sholat qodho kalian (kalau ada), cek apakah flow-nya mudah"
- Hari 14 → "Tulis satu kalimat feedback jujur tentang pengalaman kalian"

Setiap tester yang menyelesaikan misi harian mendapat "poin" di spreadsheet yang saya kelola. Tiga penerima poin tertinggi dijanjikan hadiah kecil — nggak mahal, tapi cukup jadi motivasi ekstra. Hasilnya? Dari 25 tester, **22 berhasil tetap aktif sampai hari terakhir**. Tiga yang tidak juga bukan karena malas, tapi karena kendala teknis (HP rusak dan satu orang ganti nomor jadi kehilangan akses Google Group).

Saya juga proaktif mengirim reminder pagi hari — "Pagi semuanya! Jangan lupa buka SHL Quran Pro hari ini ya, baca satu ayat juga nggak apa-apa 🤲" — yang ternyata efektif menjaga momentum. Kuncinya adalah membuat testing terasa bukan sebagai kewajiban, tapi sebagai aktivitas yang seru dan komunal.

### Momen Menegangkan Menganalisis Pre-Launch Report Google Cloud

Setelah upload AAB ke Play Console, Google secara otomatis menjalankan **Pre-Launch Report** — sebuah rangkaian automated testing yang menjalankan aplikasi kita di **puluhan perangkat fisik di Google Cloud**. Robot Google menjalankan crawl otomatis — membuka setiap screen, menekan setiap tombol, memutar layar, mengubah bahasa, mengganti ukuran font, dan berbagai skenario lainnya.

Menunggu hasil Pre-Launch Report itu rasanya kayak menunggu hasil ujian. Satu bagian di otak berkata "Harusnya oke, kita sudah testing sendiri," tapi bagian lain berteriak "Bagaimana kalau ada crash di device yang belum pernah kita test?"

Pukul 3 pagi (beda timezone dengan server Google, jadi hasilnya sering muncul dini hari), saya refresh Play Console dan melihat hasilnya.

**0 crash. 0 ANR (Application Not Responding). 0 critical warnings.**

Robot Google menjalankan aplikasi di 24 perangkat berbeda — dari Samsung Galaxy A12 low-end sampai Pixel 7 Pro flagship, dari Android 7 (API 24) sampai Android 14 (API 34) — dan tidak menemukan satu crash pun. Zero. Nol.

Ada beberapa minor warnings seperti "Text too small on some screens" dan satu accessibility suggestion, tapi nggak ada yang critical. Saya langsung berteriak kecil di kamar jam 3 pagi itu — untung nggak membangunkan siapa-siapa.

### Hari Kelulusan dan Email Terindah dari Google Play

Hari ke-15 setelah Closed Testing dimulai. Semua metrik terpenuhi — lebih dari 20 tester aktif, 14 hari terlewati, Pre-Launch Report bersih. Saya klik tombol "Request Production Access" dan menunggu.

Dua hari kemudian, email masuk. Subjeknya — "Your app has been approved for production."

Waktu itu saya sedang duduk di angkutan umum dari kampus. Membaca email itu di layar HP yang retak di pojok kiri bawah. Dan mata saya berkaca-kaca. Ini bukan cuma approval dari Google — ini validasi dari berbulan-bulan kerja keras, begadang, debugging, revisi, dan doa-doa tengah malam.

SHL Quran Pro resmi bisa ditemukan di Google Play Store. Dari sebuah folder project kosong di Android Studio, sampai menjadi aplikasi yang bisa didownload siapa saja di seluruh dunia. Subhanallah.

Terima kasih yang tak terhingga untuk ke-25 sahabat penguji yang meluangkan waktu mereka setiap hari selama dua minggu. Tanpa kalian, SHL Quran Pro nggak akan pernah sampai ke titik ini. Kalian bukan cuma tester — kalian adalah bagian dari cerita ini.

## Refleksi Hati Menemukan Makna di Balik Setiap Baris Kode

Di malam-malam coding yang sepi, ketika cursor berkedip-kedip sendirian di layar dan rumah sudah sunyi, kadang pikiran melayang ke pertanyaan yang lebih besar dari sekadar arsitektur kode. **Untuk apa semua ini?**

Ratusan jam belajar Kotlin. Puluhan malam debugging. Ribuan baris kode yang ditulis, dihapus, ditulis ulang. Untuk apa?

Dan jawabannya, yang selalu datang di keheningan malam itu, sederhana tapi dalam — **ini adalah usaha menjadikan teknologi sebagai amal jariyah.**

Ada hadits yang mengajarkan bahwa amal jariyah — amal yang pahalanya mengalir terus meskipun pemiliknya sudah tiada — salah satunya adalah ilmu yang bermanfaat. Ketika seseorang membaca Al-Quran lewat aplikasi ini, memahami tajweed-nya, mengamalkan isinya, membagikannya ke keluarganya — insya Allah ada aliran kebaikan yang sampai ke kita sebagai developer-nya.

Setiap fungsi `getAyahsBySurah()` yang berhasil mengembalikan data dalam 1.5ms itu bukan cuma pencapaian teknis. Itu juga membuka jalan bagi seseorang untuk membaca Kalam Allah dengan mudah dan nyaman. Setiap fix untuk bug Doze Mode adzan Subuh itu bukan cuma victory debugging — itu membantu seseorang bangun untuk sholat Subuh berjamaah.

Teknologi itu sendiri adalah anugerah akal dari Allah SWT. Kemampuan kita memahami logika pemrograman, merancang arsitektur software, me-debug masalah yang kompleks — semua itu bukan karena kita pintar semata. Itu karena Allah memberikan akal dan kesempatan untuk belajar. Dan sudah sepatutnya anugerah itu kita gunakan untuk sesuatu yang bernilai di sisi-Nya.

Saya teringat malam-malam tertentu saat kode nggak mau jalan, build terus error, emulator crash berulang kali. Di momen-momen itu, yang menguatkan bukan stack overflow skor tertinggi — tapi kesadaran bahwa ini proyek yang bermakna. Bahwa InsyaAllah setiap kesulitan dalam mengerjakan ini, ada pahala di baliknya.

Dan di malam-malam itu juga, saya berdoa — semoga setiap baris kode yang ditulis dengan niat baik diterima sebagai ibadah. Semoga SHL Quran Pro menjadi wasilah kebaikan bagi siapa saja yang menggunakannya. Aamiin.

## Rencana Seru Pengembangan di Masa Depan

Perjalanan SHL Quran Pro bukan berakhir di rilis pertama — justru di sinilah petualangan sesungguhnya dimulai. Ada banyak mimpi dan rencana yang sudah mengantri untuk diwujudkan.

**Modul Interaktif Tajweed Audio** — Ini yang paling saya excited-kan. Bayangkan bisa menekan satu kata di mushaf, lalu mendengar penjelasan audio "Ini hukum bacaan idgham bighunnah, cara membacanya seperti ini..." lengkap dengan contoh pelafalan yang benar. Bukan sekadar warna-warni di teks, tapi pengalaman belajar tajweed yang imersif dan interaktif. Modul ini membutuhkan kolaborasi dengan ustadz tajweed dan proses recording yang berkualitas, jadi timeline-nya mungkin lebih panjang — tapi insya Allah akan sangat worth it.

**Backup Terenkripsi ke Google Drive Pribadi** — Data qodho, bookmark, catatan pribadi — semua itu berharga bagi pengguna. Kehilangan progres qodho karena ganti HP itu menyakitkan. Rencana kita adalah mengimplementasikan backup terenkripsi (AES-256-GCM) ke Google Drive pengguna. Data dienkripsi di device sebelum diupload, jadi bahkan Google sekalipun nggak bisa baca isinya. Restore otomatis saat install di perangkat baru.

**Palet Tema Estetik Baru** — Obsidian Gold sudah jadi identitas, tapi kita ingin kasih lebih banyak pilihan. Tiga tema baru yang sedang didesain:

- **Sage Botanical** — nuansa hijau sage dengan aksen daun-daunan, terasa adem dan natural. Cocok buat yang suka suasana taman.
- **Midnight Starlight** — deep navy blue dengan taburan bintang-bintang kecil di background. Untuk yang suka baca Quran di malam hari, ini bakal terasa sangat immersive.
- **Morning Dawn** — gradient hangat dari peach ke soft gold, mengingatkan suasana fajar. Sempurna untuk yang rutin tilawah setelah Subuh.

Setiap tema bukan cuma ganti warna — typography, spacing, animasi transisi, semua disesuaikan dengan mood tema tersebut.

**Fitur Komunitas** — Ini masih di tahap eksplorasi konsep, tapi visinya adalah menghubungkan pengguna SHL Quran Pro dengan sesama — grup khataman bersama, tantangan hafalan mingguan, berbagi catatan tadabbur (dengan izin), dan mungkin forum diskusi sederhana. Semua kembali ke misi utama — menjadikan teknologi sebagai jembatan menuju kebaikan kolektif.

Semua rencana ini bertahap dan insya Allah akan direalisasikan sesuai kemampuan. Yang penting bukan cepat, tapi kualitas dan keikhlasan di setiap prosesnya.

---

Untuk kamu yang sudah membaca sampai sini — dari pembahasan arsitektur database, drama debugging malam hari, changelog versi, perjuangan menembus Google Play, sampai refleksi spiritual — terima kasih sudah menemani perjalanan ini. Menulis artikel ini sendiri adalah bentuk refleksi yang indah, karena memaksa saya mengingat kembali setiap momen yang sudah dilalui.

SHL Quran Pro bukan cuma proyek kode. Ini proyek hati. Dan perjalanannya masih panjang.

Sampai jumpa di Weekly berikutnya insya Allah. Semoga tulisan ini menginspirasi, atau minimal menghibur di sela-sela kesibukan kamu. Stay curious, stay grateful, dan jangan pernah berhenti belajar! 🤲

### 💡 Rekomendasi Bacaan Santai Lainnya

Kalau kamu menikmati tulisan ini, mungkin kamu juga bakal suka beberapa artikel santai lainnya di blog ini. Sengaja saya pilihkan topik-topik yang nyambung sama semangat produktivitas dan keberkahan yang kita obrolin di atas.

🕒 <a href="/post/manajemen/Seni-Mengatur-Waktu-dan-Prioritas-Kerja-agar-Hidup-Tidak-Dikejar-Deadline" target="_blank">Seni Mengatur Waktu dan Prioritas Kerja agar Hidup Tidak Dikejar Deadline</a> — Tips manajemen waktu yang actionable buat kamu yang sering merasa dikejar-kejar deadline. Cocok banget buat developer yang harus juggling antara coding, testing, dan kehidupan pribadi.

🤝 <a href="/post/manajemen/Seni-Mendelegasikan-Tugas-Tanpa-Takut-Hasil-Kerja-Berantakan" target="_blank">Seni Mendelegasikan Tugas Tanpa Takut Hasil Kerja Berantakan</a> — Buat yang mulai membangun tim atau bekerja bareng orang lain, artikel ini ngomongin cara mendelegasikan tugas dengan percaya diri tanpa micro-managing.

📜 <a href="/post/fiqh/Panduan-Lengkap-Fiqh-Ijarah-untuk-Bisnis-Sewa-dan-Jasa-Tenaga-Kerja-Modern" target="_blank">Panduan Lengkap Fiqh Ijarah untuk Bisnis Sewa dan Jasa Tenaga Kerja Modern</a> — Kalau kamu tertarik sisi syariah dari dunia bisnis dan kerja, ini bacaan yang enlightening sekaligus praktis.

🛠️ <a href="/tools" target="_blank">Tools dan Sumber Daya Gratis dari SHL Project</a> — Koleksi tools yang saya kumpulkan dan buat sendiri untuk membantu produktivitas sehari-hari. Ada yang berguna buat developer, ada juga yang buat kebutuhan umum.

Selamat membaca dan semoga bermanfaat! 📖✨
