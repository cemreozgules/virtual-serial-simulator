import queue
import time
import threading


sanal_port_kuyrugu = queue.Queue()


# 1.VERİ GÖNDEREN THREAD 
def veri_gonderici():
  print(" Simülatör (Mikrodenetleyici) başladı, veri üretiliyor...")
  while True:
    sicaklik = 24.5  # Örnek veri
    veri = f"Sicaklik: {sicaklik} C\n"

    
    sanal_port_kuyrugu.put(veri)
    print(f"[GÖNDERİLDİ] -> {veri.strip()}")

    time.sleep(1)


# 2.VERİ OKUYAN KISIM 
def veri_okuyucu():
  print("📥 Okuyucu portu dinlemeye başladı...\n")
  try:
    while True:
      
      if not sanal_port_kuyrugu.empty():
        gelen_veri = sanal_port_kuyrugu.get().strip()
        zaman = time.strftime("%H:%M:%S")
        print(f"[{zaman}]  OKUNDU: {gelen_veri}")

      time.sleep(0.1)
  except KeyboardInterrupt:
    print("Durduruldu.")



if __name__ == "__main__":
  t1 = threading.Thread(target=veri_gonderici)
  t2 = threading.Thread(target=veri_okuyucu)

  t1.daemon = True
  t2.daemon = True

  t1.start()
  t2.start()

  
  try:
    while True:
      time.sleep(1)
  except KeyboardInterrupt:
    print("\nProgram kapatılıyor...")