import time
import serial


PORT = "COM2"
BAUD = 9600

print(f"{PORT} portu dinleniyor...")

try:
  ser = serial.Serial(PORT, BAUD, timeout=1)
  time.sleep(2)

  while True:
    if ser.in_waiting > 0:
      veri = ser.readline().decode("utf-8").strip()
      if veri:
        zaman = time.strftime("%H:%M:%S")
        print(f"[{zaman}] Alınan Veri: {veri} °C")

        

except KeyboardInterrupt:
  print("Durduruldu.")
  ser.close()