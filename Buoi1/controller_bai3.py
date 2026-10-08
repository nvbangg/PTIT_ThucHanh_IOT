import time
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
DEVICE_ID = "light01"
CMD_TOPIC = "iot/lab/light01/cmd"
STATUS_TOPIC = "iot/lab/light01/status"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Ket noi broker thanh cong!")
        print("Dang lang nghe topic:", STATUS_TOPIC)
        client.subscribe(STATUS_TOPIC)
    else:
        print("Ket noi that bai:", reason_code)


def on_message(client, userdata, msg):
    print("Trang thai nhan duoc:")
    print(msg.payload.decode("utf-8"))


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

print("Dang ket noi toi broker...")
client.connect(BROKER, PORT, 60)
client.loop_start()

# Cho ket noi va subscribe on dinh
time.sleep(1)

try:
    print("\n--- DIEU KHIEN DEN THONG MINH ---")
    print("Nhap 'ON' de bat, 'OFF' de tat, 'EXIT' de thoat.\n")
    while True:
        cmd = input("Nhap lenh: ").strip()

        if not cmd:
            continue

        cmd_upper = cmd.upper()
        if cmd_upper == "EXIT":
            print("Thoat chuong trinh controller...")
            break
        elif cmd_upper in ["ON", "OFF"]:
            client.publish(CMD_TOPIC, cmd_upper)
            print(f"Da gui lenh {cmd_upper} toi {DEVICE_ID}")
            # Cho phan hoi tu thiet bi tra ve truoc khi yeu cau nhap lenh tiep theo
            time.sleep(0.8)
            print()
        else:
            print("Loi: Lenh khong hop le! Vui long chi nhap 'ON', 'OFF' hoac 'EXIT'.\n")

except KeyboardInterrupt:
    print("\nKet thuc Controller App")

finally:
    client.loop_stop()
    client.disconnect()
