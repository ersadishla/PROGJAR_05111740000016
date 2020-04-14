#ab -n jumlah_request -c jumlah_konkuren http://localhost:8887/testingab -n jumlah_request -c jumlah_konkuren http://localhost:8887/testing.txt


ab -n 10 -c 1 http://127.0.0.1:10001/

ab -n 10 -c 5 http://127.0.0.1:10001/

ab -n 10 -c 10 http://127.0.0.1:10001/


ab -n 50 -c 1 http://127.0.0.1:10001/

ab -n 50 -c 10 http://127.0.0.1:10001/

ab -n 50 -c 30 http://127.0.0.1:10001/

ab -n 50 -c 50 http://127.0.0.1:10001/


ab -n 100 -c 1 http://127.0.0.1:10001/

ab -n 100 -c 10 http://127.0.0.1:10001/

ab -n 100 -c 50 http://127.0.0.1:10001/

ab -n 100 -c 100 http://127.0.0.1:10001/

