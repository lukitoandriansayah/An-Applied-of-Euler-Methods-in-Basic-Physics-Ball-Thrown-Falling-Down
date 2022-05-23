Numerical Integration
Misalkan diketahui posisi x_0 , kecepatan v_0  , dan percepatan a_0  partikel pada suatu waktu awal t_0 . Jika kita mengabaikan perubahan kecepatan selama selang 
waktu ∆t , posisi baru x_1 diberikan oleh 

        x_1 = x_0 + v_0x . ∆t	(1)

Demikian pula, jika kita asumsikan percepatan konstan selama ∆t , kecepatan pada waktu t_1= t_0+∆t  diberikan oleh 

        v_1x = v_0x + a_0x . ∆t	(2)

Kita dapat menggunakan nilai x_1 dan v_1x untuk menghitung percepatan baru a_1x menggunakan hukum kedua Newton, dan kemudian gunakan x_1 , v_1x , dan a_1x untuk 
menghitung x_2 dan v_2x . 

      x_2 = x_1 + v_1x . ∆t	(3)
      v_2x = v_1x + a_1x . ∆t	(4)

Hubungan antara posisi dan kecepatan pada waktu t_n dan waktu 

     t_(n+1) = t_n + ∆t   

diberikan 

    x_(n+1)   = x_n + v_nx . ∆t	(5)

    v_(n+1)x  = v_nx + a_nx . ∆t	(6)

Untuk mencari kecepatan dan posisi pada suatu waktu t , maka kita membagi selang waktu t- t_0 menjadi banyak interval yang lebih kecil dari t dan menerapkan 
Persamaan (5) dan (6), dimulai pada waktu awal t_0 . Hal ini akan melibatkan sejumlah besar perhitungan sederhana dan berulang yang paling mudah dilakukan di 
komputer. Teknik memecah interval waktu menjadi langkah-langkah kecil dan menghitung percepatan, kecepatan, dan posisi pada setiap langkah menggunakan nilai dari 
langkah sebelumnya disebut numerical integration (Tipler & Mosca, 2007).

Benda Jatuh
Tinjaulah sebuah benda yang sedang terjatuh dari suatu ketinggian. Benda tersebut berada dalam pengaruh gaya gravitasi  dan juga drag force selama tejatuh yang mana 
nilai drag force proporsional dengan laju kuadrat (Cutnell JD, 2018). Dari kasus tersebut, kita ingin menemukan kecepatan dan jarak tempuh sebagai fungsi waktu. 
Persamaan gerak benda yang terjatuh adalah sebagai berikut:

         mg - b.v^2 = m.a_x	

dimana arah kebawah adalah positif. Sehingga percepatan diberikan sebagai:

           a_x   = g-((b/m) . v^2)	(7)

Ambil nilai untuk a_x=0 , maka persamaan tersebut menjadi:
            
              0  = g- ((b/m) . v^2)	
            b/m  =  g/v^2 	

Variabel v^2 pada keadaan ini (percepatan nol) dituliskan sebagai laju terminal kuadrat (〖v_T〗^2). Jika nilai tersebut disulih ke dalam persamaan (7) akan 
memberikan:

             a_x = g (1-v^2/〖v_T〗^2 )	(8)
