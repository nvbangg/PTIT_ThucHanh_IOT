
## Note:

- cài thư viện:
```sh
python -m pip install paho-mqtt
cd Buoi1
```

## bài 1
- Mở Terminal 1 và chạy:
```sh
python subscriber_bai1.py
```
Kết quả:
```
Dang ket noi toi broker...
Ket noi broker thanh cong!
Dang lang nghe topic: iot/lab/message
```

- Sau đó Mở Terminal 2 và chạy:
```sh
python publisher_bai1.py
```
kết quả:
```
Dang ket noi toi broker...
Da gui message:
Topic: iot/lab/message
Payload: Xin chao tu client Python MQTT - B23DCCN067 - Nguyễn Văn Bằng
```

kết quả phía terminal 1:
```
Nhan duoc message:
Topic: iot/lab/message
Payload: Xin chao tu client Python MQTT - B23DCCN067 - Nguyễn Văn Bằng
Time: 11:36:09
```

## bài 2

- Mở Terminal 1 và chạy:

```sh
python monitor_subscriber_bai2.py
```
kết quả:
```
Dang ket noi toi broker...
Ket noi broker thanh cong!
Dang lang nghe topic: iot/lab/sensor01/data
```
- Sau đó mở Terminal 2 và chạy:
```sh
python sensor_publisher_bai2.py
```
kết quả:
```
Dang ket noi toi broker...
Da gui: {"device_id": "sensor01", "temperature": 36.4, "humidity": 37.8}
```
kết quả phía terminal 1:
```
Device: sensor01
Temperature: 36.4 C
Humidity: 37.8 %
CANH BAO: Nhiet do cao
CANH BAO: Do am thap
```
