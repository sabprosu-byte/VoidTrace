#!/usr/bin/env python3
import socket
import sys
import os
import requests
import time
import subprocess
from datetime import datetime

try:
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone
except ImportError:
    print("[!] Eksik kütüphane! Yüklemek için: pip install phonenumbers")
    sys.exit(1)

class ipCAWAnalyzer:
    def __init__(self, target_ip):
        self.target_ip = target_ip
        self.common_ports = {
            554: "RTSP",
            80: "HTTP",
            8080: "HTTP-Proxy",
            37702: "ONVIF",
            8000: "Hikvision",
            1935: "RTMP"
        }

    def scan_ports(self):
        print(f"\n[*] Gerçek IP Kamera / Özel Port Taraması Başlatılıyor -> {self.target_ip}")
        open_ports = []
        for port, description in self.common_ports.items():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1.0)
                if sock.connect_ex((self.target_ip, port)) == 0:
                    print(f"[+] Port {port} -> AÇIK ({description})")
                    open_ports.append(port)
                sock.close()
            except socket.error:
                pass
        if not open_ports:
            print("[+] Kritik kamera portu bulunamadı.")

def port_analizi():
    target = input("Hedef IP / Domain girin: ").strip()
    print(f"\n[*] Gerçek Port Taraması Başlatılıyor -> {target}")
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

def ag_bilgisi():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"[+] Yerel Hostname: {hostname}")
    print(f"[+] Yerel IP Arayüzü: {local_ip}")

def target_intelligence():
    target = input("Target Intelligence için Hedef IP / Domain: ").strip()
    try:
        ip = socket.gethostbyname(target)
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=4).json()
        print(f"[+] Hedef Çözüldü IP: {ip}")
        print(f"    Ülke: {r.get('country')}, Şehir: {r.get('city')}, Servis Sağlayıcı: {r.get('isp')}")
    except:
        print("[!] İstihbarat alınamadı.")

def http_header_analizi():
    url = input("URL girin (https://example.com): ").strip()
    if not url.startswith("http"):
        url = "http://" + url
    try:
        r = requests.get(url, timeout=5)
        print(f"[+] Gerçek HTTP Status Kodu: {r.status_code}")
        for k, v in r.headers.items():
            print(f"    {k}: {v}")
    except Exception as e:
        print(f"[!] Hata: {e}")

def antivirus_dosya_analizi():
    path = input("Analiz edilecek dosya yolunu girin: ").strip()
    if os.path.exists(path):
        size = os.path.getsize(path)
        print(f"[+] Gerçek Dosya Boyutu: {size} bayt")
        print(f"[+] Dosya Erişilebilir ve Okunabilir.")
    else:
        print("[!] Dosya bulunamadı!")

def subnet_recon():
    base_ip = input("Ağ alt tabanı girin (örn: 192.168.1): ").strip()
    print("[*] Gerçek Subnet / Host Discovery Taraması Yapılıyor...")
    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)
            if s.connect_ex((ip, 80)) == 0:
                print(f"[+] Aktif Host Bulundu: {ip}")
            s.close()
        except:
            pass

def ip_domain_bilgi():
    target = input("IP / Domain Bilgi Toplanacak Hedef: ").strip()
    try:
        ip = socket.gethostbyname(target)
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=4).json()
        print(f"[+] IP: {ip}")
        print(f"    Ülke: {r.get('country')}")
        print(f"    Şehir: {r.get('city')}")
        print(f"    ISS: {r.get('isp')}")
    except:
        print("[!] Bilgi sorgulanamadı.")

def stress_injector():
    target = input("Hedef IP / Domain: ").strip()
    port = int(input("Hedef Port (örn: 80): ").strip())
    print(f"[*] Gerçek Stress & Latency Injector Başlatıldı -> {target}:{port}")
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
        print(f"[!] Bağlantı sonlandı: {e}")

def fsociety_protocols():
    print("[+] Fsociety Core Protocols & Recon Tools Çalıştırılıyor...")
    os.system("netstat -i" if os.name != 'nt' else "ifconfig")

def password_audit():
    print("\n=== Password Audit Suite (JtR, Hydra, Hashcat) ===")
    print("1. John the Ripper (john)")
    print("2. Hydra (hydra)")
    print("3. Hashcat (hashcat)")
    sec = input("Seçiminiz (1/2/3): ").strip()
    
    if sec == "1":
        path = input("Hash dosyasının tam yolu: ").strip()
        if os.path.exists(path):
            subprocess.run(["john", path])
        else:
            print("[!] Dosya bulunamadı!")
    elif sec == "2":
        target = input("Hedef (örn: ssh://192.168.1.1): ").strip()
        user = input("Kullanıcı adı: ").strip()
        wordlist = input("Wordlist yolu: ").strip()
        subprocess.run(["hydra", "-l", user, "-P", wordlist, target])
    elif sec == "3":
        hash_file = input("Hash dosyası: ").strip()
        mode = input("Hash modu (örn: 0 for MD5): ").strip()
        wordlist = input("Wordlist yolu: ").strip()
        subprocess.run(["hashcat", "-m", mode, hash_file, wordlist])
    else:
        print("[!] Geçersiz seçim.")

def ghost_track_number_recon():
    print("""
    ========================================
    |     GHOST - TRACKER - PHONE RECON    |
    |          @CODE BY HUNXBYTES          |
    ========================================
    """)
    print("[*] Bilgi: Azerbaycan (+994), Türkiye (+90) ve tüm dünya numaraları desteklenir.")
    raw_number = input("Hedef telefon numarasını girin (Örn: +994501234567 veya +905554443322) : ").strip()
    
    try:
        # Tüm dünya numaralarını ve yerel/uluslararası formatları esnek şekilde parse etme
        try:
            parsed_number = phonenumbers.parse(raw_number, None)
        except:
            parsed_number = phonenumbers.parse(raw_number, "AZ")

        country_code = parsed_number.country_code
        national_number = parsed_number.national_number
        
        location = geocoder.description_for_number(parsed_number, "en")
        time_zones = timezone.time_zones_for_number(parsed_number)
        operator_name = carrier.name_for_number(parsed_number, "en")
        
        is_valid = phonenumbers.is_valid_number(parsed_number)
        is_possible = phonenumbers.is_possible_number(parsed_number)
        
        intl_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        mobile_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        e164_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        
        number_type = phonenumbers.number_type(parsed_number)
        
        if number_type == phonenumbers.PhoneNumberType.MOBILE:
            type_str = "This is a mobile number"
        elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
            type_str = "This is a fixed line number"
        else:
            type_str = "Other line type (VoIP/Toll-free/etc)"

        print("\n========== SHOW INFORMATION PHONE NUMBERS ==========")
        print(f"Location             : {location if location else 'Unknown (Global/Local)'}")
        print(f"Region Code          : {phonenumbers.region_code_for_number(parsed_number)}")
        print(f"Timezone             : {', '.join(time_zones) if time_zones else 'Unknown'}")
        print(f"Operator             : {operator_name if operator_name else 'Unknown'}")
        print(f"Valid number         : {is_valid}")
        print(f"Possible number      : {is_possible}")
        print(f"International format : {intl_format}")
        print(f"Mobile format        : {mobile_format}")
        print(f"Original number      : {national_number}")
        print(f"E.164 format         : {e164_format}")
        print(f"Country code         : {country_code}")
        print(f"Local number         : {national_number}")
        print(f"Type                 : {type_str}")
        print("====================================================")

    except Exception as e:
        print(f"\n[!] Hata oluştu: Lütfen numaranın başında ülke kodu olduğundan emin olun (Örn: +994... veya +90...). Detay: {e}")

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    ██╗   ██╗ ██████╗ ██╗██████╗ ████████╗██████╗  █████╗  ██████╗███████╗
    ██║   ██║██╔═══██╗██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝
    ██║   ██║██║   ██║██║██║  ██║   ██║   ██████╔╝███████║██║     █████╗  
    ╚██╗ ██╔╝██║   ██║██║██║  ██║   ██║   ██╔══██╗██╔══██║██║     ██╔══╝  
     ╚████╔╝ ╚██████╔╝██║██████╔╝   ██║   ██║  ██║██║  ██║╚██████╗███████╗
      ╚═══╝   ╚═══╝  ╚═╝╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚══════╝
      [ VoidTrace v1.0 / Linux Edition ]
    """)

def menu():
    while True:
        banner()
        print("1. Port Analizi (Port Tarama)")
        print("2. Ağ Bilgisi Sorgulama")
        print("3. Terminal Tabanlı Arayüz")
        print("4. Target Intelligence (IP Konum ve Servis Sağlayıcı Analizi)")
        print("5. HTTP Header Analizi")
        print("6. Antivirus (Dosya Analiz)")
        print("7. Subnet Recon / Host Discovery")
        print("8. IP / Domain Bilgi Toplama")
        print("9. Stress & Latency Injector")
        print("10. Fsociety Core Protocols & Recon Tools")
        print("11. Password Audit Suite (JtR, Hydra, Hashcat)")
        print("12. Ghost Track (Location & Session Recon)")
        print("13. IP Kamera Güvenlik Modülü (Özel)")
        print("0. Çıkış")
        
        secim = input("VoidTrace > ").strip()
        
        if secim == "1":
            port_analizi()
        elif secim == "2":
            ag_bilgisi()
        elif secim == "3":
            print("[+] Zaten terminal tabanlı arayüzdesiniz.")
        elif secim == "4":
            target_intelligence()
        elif secim == "5":
            http_header_analizi()
        elif secim == "6":
            antivirus_dosya_analizi()
        elif secim == "7":
            subnet_recon()
        elif secim == "8":
            ip_domain_bilgi()
        elif secim == "9":
            stress_injector()
        elif secim == "10":
            fsociety_protocols()
        elif secim == "11":
            password_audit()
        elif secim == "12":
            ghost_track_number_recon()
        elif secim == "13":
            target_ip = input("Kamera IP adresi girin: ").strip()
            analyzer = ipCAWAnalyzer(target_ip)
            analyzer.scan_ports()
        elif secim == "0":
            print("Goodbye friend.")
            sys.exit(0)
        else:
            print("[!] Geçersiz seçim!")
            
        input("\n[ + ] Press enter to continue...")

if __name__ == "__main__":
    menu()
