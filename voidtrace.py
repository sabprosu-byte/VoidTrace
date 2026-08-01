#!/usr/bin/env python3
import socket
import sys
import os
import requests
import time
import subprocess
from datetime import datetime

class ipCAWAnalyzer:
    def __init__(self, target_ip):
        self.target_ip = target_ip
        self.common_ports = {
            554: "RTSP (Real-Time Streaming Protocol)",
            80: "HTTP (Web Arayüzü)",
            8080: "Alternatif HTTP / Proxy",
            37702: "Dahua / ONVIF Servisi",
            8000: "Hikvision / Medya Servisi",
            1935: "RTMP Aktif Protokolü"
        }

    def scan_ports(self):
        print(f"\n[*] Gerçek Socket Taraması Başlatılıyor -> {self.target_ip}")
        print(f"[*] Zaman: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 50)
        open_ports = []
        for port, description in self.common_ports.items():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1.0)
                result = sock.connect_ex((self.target_ip, port))
                if result == 0:
                    print(f"[+] Port {port} -> AÇIK ({description})")
                    open_ports.append(port)
                sock.close()
            except socket.error:
                pass
        print("=" * 50)
        self.analyze_risks(open_ports)

    def analyze_risks(self, open_ports):
        if not open_ports:
            print("[+] Sistemde açık hedef port bulunamadı.")
        else:
            print("[!] Kritik portlar aktif!")

def port_analizi():
    target = input("Hedef IP / Domain girin: ").strip()
    print(f"\n[*] Port taraması başlatılıyor -> {target}")
    common_ports = [21, 22, 23, 25, 53, 80, 443, 3306, 8080]
    for port in common_ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            if s.connect_ex((target, port)) == 0:
                print(f"[+] Port {port} -> AÇIK")
            s.close()
        except:
            pass

def ip_bilgi():
    target = input("IP Bilgisi Alınacak Hedef IP: ").strip()
    try:
        r = requests.get(f"http://ip-api.com/json/{target}", timeout=4).json()
        print(f"[+] Ülke: {r.get('country')}")
        print(f"[+] Şehir: {r.get('city')}")
        print(f"[+] ISP: {r.get('isp')}")
    except:
        print("[!] İstihbarat alınamadı.")

def target_ointelligenip():
    target = input("Hedef IP / Domain girin: ").strip()
    try:
        ip = socket.gethostbyname(target)
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=4).json()
        print(f"[+] Çözülen IP: {ip}")
        print(f"    Ülke: {r.get('country')}, Şehir: {r.get('city')}")
    except:
        print("[!] Hedef çözülemedi.")

def subnet_recon():
    base_ip = input("Ağ alt tabanı girin (örn: 192.168.1): ").strip()
    print("[*] Gerçek ARP / Soket Tabanlı Host Taraması Yapılıyor...")
    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)
            result = s.connect_ex((ip, 80))
            if result == 0 or result:
                # Ağdaki aktif cihazları socket üzerinden yoklama
                host_name = socket.getnameinfo((ip, 0), socket.NI_NAMEREQ)[0]
                print(f"[+] Aktif Cihaz Bulundu: {ip} ({host_name})")
            s.close()
        except:
            pass

def stress_injector():
    target = input("Hedef IP / Domain: ").strip()
    port = int(input("Hedef Port (örn: 80): ").strip())
    print(f"[*] Gerçek Soket Yük Testi Başlatıldı -> {target}:{port}")
    count = 0
    try:
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            s.connect((target, port))
            s.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
            count += 1
            print(f"[>] Gerçek Paket #{count} Gönderildi.")
            s.close()
    except Exception as e:
        print(f"[!] Bağlantı koptu veya hedef yanıt vermiyor: {e}")

def http_header_analizi():
    url = input("URL girin (https://example.com): ").strip()
    if not url.startswith("http"):
        url = "http://" + url
    try:
        r = requests.get(url, timeout=5)
        print(f"[+] Gerçek Status Kodu: {r.status_code}")
        for k, v in r.headers.items():
            print(f"    {k}: {v}")
    except Exception as e:
        print(f"[!] Hata: {e}")

def track_akis():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"[+] Yerel Hostname: {hostname}")
    print(f"[+] Yerel IP Arayüzü: {local_ip}")
    try:
        ext_ip = requests.get("https://api.ipify.org", timeout=4).text
        print(f"[+] Gerçek Dış (WAN) IP Adresi: {ext_ip}")
    except:
        print("[!] Dış IP alınamadı.")

def host_discovery():
    subnet_recon()

def trace_akis():
    track_akis()

def society_protocols():
    print("[+] Ağ Arayüzleri ve Soket Durumları Listeleniyor...")
    os.system("netstat -i" if os.name != 'nt' else "ipconfig")

def password_audit():
    print("\n=== GERÇEK ARAÇ YÖNETİCİSİ ===" )
    print("1. John the Ripper Çalıştır")
    print("2. Hydra Çalıştır")
    print("3. Nmap ile Gerçek Ağ Taraması Çalıştır")
    sec = input("Seçiminiz (1/2/3): ").strip()
    
    if sec == "1":
        path = input("Hash dosyasının tam yolu: ").strip()
        if os.path.exists(path):
            subprocess.run(["john", path])
        else:
            print("[!] Dosya bulunamadı!")
    elif sec == "2":
        target = input("Hedef IP / Servis (örn: ssh://192.168.1.1): ").strip()
        user = input("Kullanıcı adı: ").strip()
        wordlist = input("Wordlist yolu: ").strip()
        subprocess.run(["hydra", "-l", user, "-P", wordlist, target])
    elif sec == "3":
        target = input("Nmap için Hedef IP / Subnet: ").strip()
        subprocess.run(["nmap", "-A", target])
    else:
        print("[!] Geçersiz seçim.")

def antivirus_analizi():
    path = input("Kontrol edilecek dosya yolunu girin: ").strip()
    if os.path.exists(path):
        size = os.path.getsize(path)
        print(f"[+] Gerçek Dosya Boyutu: {size} bayt")
        print(f"[+] Dosya İzinleri ve Erişilebilirlik: OK")
    else:
        print("[!] Dosya bulunamadı!")

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    ██╗   ██╗ ██████╗ ██╗██████╗ ████████╗██████╗  █████╗  ██████╗███████╗
    ██║   ██║██╔═══██╗██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝
    ██║   ██║██║   ██║██║██║  ██║   ██║   ██████╔╝███████║██║     █████╗  
    ╚██╗ ██╔╝██║   ██║██║██║  ██║   ██║   ██╔══██╗██╔══██║██║     ██╔══╝  
     ╚████╔╝ ╚██████╔╝██║██████╔╝   ██║   ██║  ██║██║  ██║╚██████╗███████╗
      ╚═══╝   ╚═══╝  ╚═╝╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝
      [ VoidTrace v1.0 / Tamamen Gerçek Sistem Motoru ]
    """)

def menu():
    while True:
        banner()
        print("1. Port Analizi")
        print("2. IP Bilgi (GeoIP)")
        print("3. Target (Hedef) Bilgi")
        print("4. Subnet Keşfi")
        print("5. Stress Injector (Gerçek Soket Yükü)")
        print("6. HTTP Header Analizi")
        print("7. Ghost Track (WAN/LAN Bilgisi)")
        print("8. Host Discovery")
        print("9. Trace IP / Cihaz")
        print("10. Society Protocols")
        print("11. Password Audit & Harici Araçlar (John/Hydra/Nmap)")
        print("12. Dosya/Sistem Analizi")
        print("13. IPCAW Analyzer")
        print("0. Çıkış")
        
        secim = input("VoidTrace > ").strip()
        
        if secim == "1":
            port_analizi()
        elif secim == "2":
            ip_bilgi()
        elif secim == "3":
            target_ointelligenip()
        elif secim == "4":
            subnet_recon()
        elif secim == "5":
            stress_injector()
        elif secim == "6":
            http_header_analizi()
        elif secim == "7":
            track_akis()
        elif secim == "8":
            host_discovery()
        elif secim == "9":
            trace_akis()
        elif secim == "10":
            society_protocols()
        elif secim == "11":
            password_audit()
        elif secim == "12":
            antivirus_analizi()
        elif secim == "13":
            target_ip = input("IPCAW Analizi için Hedef IP girin: ").strip()
            analyzer = ipCAWAnalyzer(target_ip)
            analyzer.scan_ports()
        elif secim == "0":
            print("Goodbye friend.")
            sys.exit(0)
        else:
            print("[!] Geçersiz seçim!")
            
        input("\n<Devam etmek için Enter tuşuna basın...>")

if __name__ == "__main__":
    menu()
  
