========================================================================
BAO CAO THUC HANH BUOI 1: LAP TRINH PYTHON VOI GIAO THUC MQTT
========================================================================

DANH SACH SINH VIEN THUC HIEN:
+-----+----------------------+--------------+
| STT |       Ho va ten      | Ma sinh vien |
+-----+----------------------+--------------+
|  1  | Nguyen Van Bang      | B23DCCN067   |
|  2  | Phan Thanh Binh      | B23DCCN087   |
+-----+----------------------+--------------+

1. BROKER SU DUNG:
- Host: test.mosquitto.org
- Port: 1883
- Thu vien: paho-mqtt (pip install paho-mqtt)

2. CACH CHAY TUNG CHUONG TRINH:

* BAI 1:
- Terminal 1: python subscriber_bai1.py
- Terminal 2: python publisher_bai1.py

* BAI 2:
- Terminal 1: python monitor_subscriber_bai2.py
- Terminal 2: python sensor_publisher_bai2.py

* BAI 3:
- Terminal 1: python device_bai3.py
- Terminal 2: python controller_bai3.py
  (Nhap 'ON', 'OFF' de dieu khien den; nhap 'EXIT' de thoat)

3. KET QUA DAT DUOC:

* BAI 1:
- Publisher gui message len topic iot/lab/message:
  "Xin chao tu client Python MQTT - B23DCCN067 - Nguyen Van Bang"
- Subscriber nhan dung message va in kem thoi gian nhan thuc te.

* BAI 2:
- Sensor publisher gui dinh ky moi 3s payload JSON (nhiet do, do am).
- Monitor subscriber phan tich dung JSON, in canh bao neu Nhiet do > 35 do C
  hoac Do am < 40%.

* BAI 3:
- He thong giao tiep hai chieu giam sat va dieu khien thiet bi den thong minh.
- Controller gui lenh "ON"/"OFF" len topic iot/lab/light01/cmd.
- Device nhan lenh, cap nhat trang thai va gui status JSON len topic iot/lab/light01/status.
- Controller nhan va hien thi dung trang thai phan hoi tu thiet bi.
========================================================================
