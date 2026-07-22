import os
import time
import socket

def banner():
    print("\033[92m")
    print("==================================================")
    print("           V O I D T R A C E   v1.0")
    print("              Developed by User")
    print("==================================================")
    print("\033[0m")

def main():
    while True:
        os.system('clear')
        banner()
        print("1. Port Analizi (Port Tarama)")
        print("2. Ağ Bilgisi Sorgulama")
        print("3. Terminal Tabanlı Arayüz")
        print("4. Target Intelligence (IP Konum ve Servis Sağlayıcı Analizi)")
        print("5. HTTP Header Analizi")
        print("6. Antivirüs (Dosya Analiz)")
        print("7. Subnet Recon / Host Discovery")
        print("8. IP / Domain Bilgi Toplama")
        print("9. Stress & Latency Injector")
        print("10. Fsociety Core Protocols & Recon Tools")
        print("11. Password Audit Suite (JtR, Hydra, Hashcat)")
        print("12. Ghost Track (Location & Session Recon)")
        print("13. Çıkış")
        
        secim = input("\nVoidTrace > ")

        if secim == "1":
            print("\n[!] Port Analizi başlatılıyor...")
            # Buraya port analizi kodlarını ekleyebilirsin
            input("\nDevam etmek için Enter'a basın...")
        elif secim == "2":
            print("\n[!] Ağ Bilgisi sorgulanıyor...")
            input("\nDevam etmek için Enter'a basın...")
        elif secim == "3":
            print("\n[!] Terminal Tabanlı Arayüz aktif...")
            input("\nDevam etmek için Enter'a basın...")
        elif secim == "4":
            print("\n[!] Target Intelligence analizi başlatılıyor...")
            input("\nDevam etmek için Enter'a basın...")
        elif secim == "5":
            print("\n[!] HTTP Header Analizi yapılıyor...")
            input("\nDevam etmek için Enter'a basın...")
        elif secim == "6":
            print("\n[!] Antivirüs Dosya Analizi başlatılıyor...")
            input("\nDevam etmek için Enter'a basın...")
        elif secim == "7":
            print("\n[!] Subnet Recon / Host Discovery taranıyor...")
            input("\nDevam etmek için Enter'a basın...")
        elif secim == "8":
            print("\n[!] IP / Domain Bilgi Toplama başlatılıyor...")
            input("\nDevam etmek için Enter'a basın...")
        elif secim == "9":
            print("\n[!] Stress & Latency Injector çalıştırılıyor...")
            input("\nDevam etmek için Enter'a basın...")
        elif secim == "10":
            print("\n[!] Fsociety Core Protocols & Recon Tools yükleniyor...")
            input("\nDevam etmek için Enter'a basın...")
        elif secim == "11":
            print("\n[!] Password Audit Suite (JtR, Hydra, Hashcat) başlatılıyor...")
            input("\nDevam etmek için Enter'a basın...")
        elif secim == "12":
            print("\n[!] Ghost Track (Location & Session Recon) aktif...")
            input("\nDevam etmek için Enter'a basın...")
        elif secim == "13" or secim == "14": # Menü sıralamasına göre çıkış
            print("\n[!] Çıkış yapılıyor...")
            sys.exit()
        else:
            print("\n[X] Geçersiz seçim! Tekrar deneyin.")
            time.sleep(1.5)

if __name__ == "__main__":
    import sys
    main()
    
