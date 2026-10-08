# BÁO CÁO THỰC HÀNH BUỔI 1: LẬP TRÌNH PYTHON VỚI GIAO THỨC MQTT

**Học phần**: Thực hành Internet of Things (IoT) - PTIT

### Danh sách sinh viên thực hiện

| STT | Họ và tên | Mã sinh viên |
| :---: | :--- | :---: |
| 1 | Nguyễn Văn Bằng | B23DCCN067 |
| 2 | Phan Thanh Bình | B23DCCN087 |

---

## 1. Cấu hình MQTT Broker & Môi trường

### 1.1. Cấu hình MQTT Broker
Dự án mặc định sử dụng Public MQTT Broker:
- **Broker Host**: `test.mosquitto.org`
- **Port**: `1883` (TCP không mã hóa)
- **Keepalive**: `60` giây

*(Tùy chọn Broker Local)*: Nếu muốn dùng Mosquitto chạy local:
- Cài đặt Eclipse Mosquitto trên máy hoặc chạy qua Docker:
  ```sh
  docker run -d -p 1883:1883 -p 9001:9001 eclipse-mosquitto
  ```
- Thay đổi biến `BROKER = "localhost"` trong các file mã nguồn.

### 1.2. Yêu cầu môi trường & Cài đặt thư viện
- **Python**: Phiên bản 3.x
- Cài đặt thư viện `paho-mqtt`:
  ```sh
  python -m pip install paho-mqtt
  ```
- Chuyển vào thư mục `Buoi1`:
  ```sh
  cd Buoi1
  ```

---

## 2. Cấu trúc thư mục buổi 1

```text
Buoi1/
├── publisher_bai1.py           # Bài 1: Gửi thông điệp sinh viên
├── subscriber_bai1.py          # Bài 1: Nhận và in thông điệp kèm thời gian
├── sensor_publisher_bai2.py    # Bài 2: Mô phỏng cảm biến gửi JSON mỗi 3s
├── monitor_subscriber_bai2.py  # Bài 2: Nhận dữ liệu cảm biến & cảnh báo ngưỡng
├── device_bai3.py              # Bài 3: Mô phỏng đèn thông minh (nhận lệnh & gửi status)
├── controller_bai3.py          # Bài 3: App điều khiển đèn (nhập ON/OFF và nhận status)
├── README.md                   # Hướng dẫn chi tiết và kết quả thực nghiệm
└── README.txt                  # Tóm tắt theo yêu cầu đề bài
```

---

## 3. Hướng dẫn chạy & Kết quả từng bài

### Bài 1: Gửi và nhận thông điệp MQTT cơ bản

#### Topic sử dụng
- `iot/lab/message`

#### Cách chạy
1. **Mở Terminal 1** chạy Subscriber:
   ```sh
   python subscriber_bai1.py
   ```
2. **Mở Terminal 2** chạy Publisher:
   ```sh
   python publisher_bai1.py
   ```

#### Kết quả đạt được
- **Terminal 2 (Publisher)**:
  ```text
  Dang ket noi toi broker...
  Ket noi broker thanh cong!
  Da gui message:
  Topic: iot/lab/message
  Payload: Xin chao tu client Python MQTT - B23DCCN067 - Nguyễn Văn Bằng
  ```
- **Terminal 1 (Subscriber)**:
  ```text
  Dang ket noi toi broker...
  Ket noi broker thanh cong!
  Dang lang nghe topic: iot/lab/message

  Nhan duoc message:
  Topic: iot/lab/message
  Payload: Xin chao tu client Python MQTT - B23DCCN067 - Nguyễn Văn Bằng
  Time: 11:36:09
  ```

---

### Bài 2: Mô phỏng cảm biến nhiệt độ và độ ẩm

#### Topic sử dụng
- `iot/lab/sensor01/data`

#### Định dạng Payload (JSON)
```json
{
  "device_id": "sensor01",
  "temperature": 36.4,
  "humidity": 37.8
}
```

#### Ngưỡng cảnh báo
- Nhiệt độ > 35°C: `CANH BAO: Nhiet do cao`
- Độ ẩm < 40%: `CANH BAO: Do am thap`

#### Cách chạy
1. **Mở Terminal 1** chạy Monitoring Subscriber:
   ```sh
   python monitor_subscriber_bai2.py
   ```
2. **Mở Terminal 2** chạy Sensor Publisher (gửi dữ liệu định kỳ mỗi 3 giây):
   ```sh
   python sensor_publisher_bai2.py
   ```

#### Kết quả đạt được
- **Terminal 2 (Sensor Publisher)**:
  ```text
  Dang ket noi toi broker...
  Ket noi broker thanh cong!
  Da gui: {"device_id": "sensor01", "temperature": 36.4, "humidity": 37.8}
  ```
- **Terminal 1 (Monitoring Subscriber)**:
  ```text
  Dang ket noi toi broker...
  Ket noi broker thanh cong!
  Dang lang nghe topic: iot/lab/sensor01/data

  Device: sensor01
  Temperature: 36.4 C
  Humidity: 37.8 %
  CANH BAO: Nhiet do cao
  CANH BAO: Do am thap
  ```

---

### Bài 3: Mô phỏng hệ thống điều khiển đèn thông minh

#### Topic sử dụng
- Topic điều khiển: `iot/lab/light01/cmd`
- Topic trạng thái: `iot/lab/light01/status`

#### Nguyên lý hoạt động
- **Smart Light Device (`device_bai3.py`)**:
  - Đăng ký lắng nghe lệnh từ `iot/lab/light01/cmd`.
  - Nhận lệnh `"ON"` -> bật đèn, chuyển trạng thái sang `"ON"`.
  - Nhận lệnh `"OFF"` -> tắt đèn, chuyển trạng thái sang `"OFF"`.
  - Sau mỗi lệnh hợp lệ (hoặc khi vừa kết nối), xuất bản trạng thái mới lên `iot/lab/light01/status` dưới dạng JSON:
    ```json
    {"device_id": "light01", "status": "ON"}
    ```
- **Controller App (`controller_bai3.py`)**:
  - Đăng ký lắng nghe trạng thái từ `iot/lab/light01/status`.
  - Cho người dùng nhập lệnh qua bàn phím:
    - Nhập `ON` / `OFF`: Gửi lệnh tới đèn qua `iot/lab/light01/cmd`.
    - Nhập `EXIT`: Thoát chương trình.
    - Nhập lệnh sai: Báo lỗi và yêu cầu nhập lại.
  - Hiển thị phản hồi trạng thái từ thiết bị ngay khi nhận được.

#### Cách chạy
1. **Mở Terminal 1** khởi động thiết bị đèn thông minh:
   ```sh
   python device_bai3.py
   ```
2. **Mở Terminal 2** chạy ứng dụng điều khiển:
   ```sh
   python controller_bai3.py
   ```
3. Nhập lệnh `ON`, `OFF` hoặc `EXIT` trên Terminal 2.

#### Kết quả đạt được
- **Terminal 1 (Device)**:
  ```text
  Dang ket noi toi broker...
  Ket noi broker thanh cong!
  Dang lang nghe lenh dieu khien tren topic: iot/lab/light01/cmd
  Trang thai hien tai: {"device_id": "light01", "status": "OFF"}

  Nhan lenh: ON
  Cap nhat trang thai den thanh: ON
  Trang thai hien tai: {"device_id": "light01", "status": "ON"}

  Nhan lenh: OFF
  Cap nhat trang thai den thanh: OFF
  Trang thai hien tai: {"device_id": "light01", "status": "OFF"}
  ```
- **Terminal 2 (Controller)**:
  ```text
  Dang ket noi toi broker...
  Ket noi broker thanh cong!
  Dang lang nghe topic: iot/lab/light01/status

  --- DIEU KHIEN DEN THONG MINH ---
  Nhap 'ON' de bat, 'OFF' de tat, 'EXIT' de thoat.

  Nhap lenh: ON
  Da gui lenh ON toi light01
  Trang thai nhan duoc:
  {"device_id": "light01", "status": "ON"}

  Nhap lenh: OFF
  Da gui lenh OFF toi light01
  Trang thai nhan duoc:
  {"device_id": "light01", "status": "OFF"}

  Nhap lenh: EXIT
  Thoat chuong trinh controller...
  ```
