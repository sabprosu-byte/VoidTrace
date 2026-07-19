import os
import time
import socket

def banner():
    print("\033[92m")
    print("====================================")
    print("     V O I D T R A C E  v1.0        ")
    print("        Developed by User           ")
    print("====================================")
    print("\033[0m")

def main():
    while True:
        os.system('clear')
        banner()
        print("1. Port Analizi")
        print("2. Ağ Bilgisi")
        print("3. Çıkış")
        secim = input("\nVoidTrace > ")

        if secim == "1":
            print("\n[!] Port Analizi başlatılıyor...")
            hedef = "127.0.0.1"
            portlar = [80, 443, 8080, 22]
            for port in portlar:
                time.sleep(0.5)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                sonuc = s.connect_ex((hedef, port))
                if sonuc == 0:
                    print(f"[+] Port {port}: AÇIK")
                else:
                    print(f"[-] Port {port}: KAPALI")
                s.close()
            input("\nAnaliz tamamlandı. Ana menüye dönmek için Enter'a bas...")
        
        elif secim == "2":
            print("\n[!] Ağ bilgileri alınıyor...")
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()
            time.sleep(1)
            print("Yerel IP Adresi: " + local_ip)
            print("Durum: Bağlı")
            input("\nAna menüye dönmek için Enter'a bas...")
            
        elif secim == "3":
            print("[-] Kapatılıyor...")
            break
        else:
            print("[X] Geçersiz seçim!")
            time.sleep(1)

if __name__ == "__main__":
    main()

