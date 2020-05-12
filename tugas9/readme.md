## Tugas 8 Pemrograman Jaringan

## Soal
1. Pull update terakhir
2. Jalankan kedua model tersebut
    * Server_async_http.py di port 45000
    * Server_thread_http.py di port 46000
3. Ujicobalah dengan apache benchmark untuk 1000 request dan konkurensi yang bervariasi
4. Buatlah tabel untuk melaporkan hasilnya

## Jalankan kedua model

![](img/1.png)

## Ujicobalah dengan apache benchmark untuk 1000 request dan konkurensi yang bervariasi
1. server_async_http.py
    * ab -n 1000 -c 1 -r -k -s 99999 http://127.0.0.1:45000/
    ![](img/ac1.png)  
    * ab -n 1000 -c 10 -r -k -s 99999 http://127.0.0.1:45000/
    ![](img/ac10.png)  
    * ab -n 1000 -c 50 -r -k -s 99999 http://127.0.0.1:45000/
    ![](img/ac50.png)  
    * ab -n 1000 -c 100 -r -k -s 99999 http://127.0.0.1:45000/
    ![](img/ac100.png)  
2. server_thread_http.py
    * ab -n 1000 -c 1 -r -k -s 99999 http://127.0.0.1:46000/
    ![](img/ac1.png)  
    * ab -n 1000 -c 10 -r -k -s 99999 http://127.0.0.1:46000/
    ![](img/ac10.png)  
    * ab -n 1000 -c 50 -r -k -s 99999 http://127.0.0.1:46000/
    ![](img/ac50.png)  
    * ab -n 1000 -c 100 -r -k -s 99999 http://127.0.0.1:46000/
    ![](img/ac100.png)  
