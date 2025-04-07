import serial
import time

# 設定 Serial 連接
arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
time.sleep(2)  # 等待 Arduino 啟動

def send_command(command):
    """ 傳送 ON / OFF 指令給 Arduino """
    arduino.write(f"{command}\n".encode())  # 傳送指令
    print(f"發送: {command}")

def read_data():
    """ 讀取 Arduino 回傳的 LED 狀態與按鈕狀態 """
    while arduino.in_waiting:  # 檢查 Serial 是否有資料
        response = arduino.readline().decode().strip()  # 讀取並解碼
        if response:
            print(f"Arduino 回應: {response}")

# 主迴圈
try:
    while True:
        send_command("ON")  # 開啟 LED
        time.sleep(1)       # 等待 1 秒
        read_data()         # 讀取 Arduino 狀態

        send_command("OFF") # 關閉 LED
        time.sleep(1)       # 等待 1 秒
        read_data()         # 讀取 Arduino 狀態

except KeyboardInterrupt:
    print("\n程式結束")
finally:
    arduino.close()  # 關閉 Serial 連線

