import random
import time
import serial


PORT = "COM1"
BAUD = 9600

print(f"Simülatör başlatıldı. {PORT} üzerinden veri gönderiliyor...")

try:
  ser = serial.Serial(PORT, BAUD, timeout=1)
  while True:
   
    sicaklik = round(random.uniform(20.0, 35.0), 2)
    veri = f"{sicaklik}\n"

    
    ser.write(veri.encode("utf-8"))
    print(f"Gönderildi: {sicaklik} °C")

    time.sleep(1) 

except Exception as e:
  print(f"Hata oluştu: {e}")