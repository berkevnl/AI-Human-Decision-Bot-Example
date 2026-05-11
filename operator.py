import os

def operator_panel():
    print("--- UZMAN TERCİH DANIŞMANI YANITLAMA PANELİ ---")
    while True:
        # soru.txt dosyasının varlığını kontrol et ve içeriği soru değişkenine al
        try:
            if os.path.exists("soru.txt"):
                with open("soru.txt", "r", encoding="utf-8") as f:
                    soru = f.read()
                
                # Satırı "|" sembolünden bölerek listeye çevir (anahtar-değer şeklinde 2 elemanlı liste)
                # İlk eleman öğrencinin mesajıyla eşleşen soru, ikinci eleman ise botun vereceği yanıt
                metin = soru.split("|")

                # Öğrenciyi yanıtlayabilmek için uzmandan onay iste
                print(f"[Bot'tan Gelen Soru] Öğrencinin '{metin[0]}' mesajı için '{metin[1]}' şeklinde yanıt vereceğim, onaylıyor musunuz? ")
                cevap = input("Yanıtınız [E/H]: ").lower()

                # Mantıksal kontroller ve cevabın cevap.txt'ye yazılması
                if cevap in ["e", "evet", "h", "hayır"]:
                    with open("cevap.txt", "w", encoding="utf-8") as f:
                        f.write(cevap)
                    # İşlem bitince soru.txt'yi sil
                    os.remove("soru.txt")
                    print("Yanıtınız başarıyla iletildi!")
                else:
                    print("Geçersiz girdi, lütfen belirtilen şekilde yanıtlayın.")
        except Exception as e:
            print(f"Hata oluştu: {e}")
    
print(operator_panel())


