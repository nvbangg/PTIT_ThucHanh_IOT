import json
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
DEVICE_ID = "light01"
CMD_TOPIC = "iot/lab/light01/cmd"
STATUS_TOPIC = "iot/lab/light01/status"

# Trang thai ban dau cua den
current_status = "OFF"


def send_status(client):
    payload = json.dumps({
        "device_id": DEVICE_ID,
        "status": current_status
    })
    client.publish(STATUS_TOPIC, payload)
    print("Trang thai hien tai:", payload)


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Ket noi broker thanh cong!")
        print("Dang lang nghe lenh dieu khien tren topic:", CMD_TOPIC)
        client.subscribe(CMD_TOPIC)
        # Gui trang thai ban dau khi ket noi thanh cong
        send_status(client)
    else:
        print("Ket noi that bai:", reason_code)


def on_message(client, userdata, msg):
    global current_status
    command = msg.payload.decode("utf-8").strip().upper()
    print(f"\nNhan lenh: {command}")

    if command in ["ON", "OFF"]:
        current_status = command
        print(f"Cap nhat trang thai den thanh: {current_status}")
        send_status(client)
    else:
        print(f"Lenh '{command}' khong hop le (chi chap nhan ON hoac OFF)")


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

print("Dang ket noi toi broker...")
client.connect(BROKER, PORT, 60)

try:
    client.loop_forever()

except KeyboardInterrupt:
    print("\nKet thuc Smart Light Device")

finally:
    client.disconnect()
