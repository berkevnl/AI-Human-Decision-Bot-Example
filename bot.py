import sys
import time
import os

# HOTL modunda karşılaşıldığında öğrenciyi uzmana aktaracak ifadeler listesi
kritik_ifadeler = [
    "kararsızım",
    "çaresizim",
    "depresyon",
    "ailem",
    "baskı",
    "ekonomik zorluk",
    "ne yapacağımı bilemiyorum",
    "korkuyorum",
    "tüm hayatımı değiştirecek",
    "nefret ediyorum",
    "hiçbir fikrim yok",
    "sevgilimle okumak istiyorum",
    "ortamı gerçekte nasıl"
]

def uzmana_sor(line):
    # Botun vereceği yanıt
    bot_yaniti = line.split("|")[1]
    
    # Öğrencinin girdisi ile eşleşen soru ve yanıt satırını soru.txt'ye yaz
    with open("soru.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print("Bot: Bu soru için Uzman Tercih Danışmanı'ndan yanıt bekliyorum... [YANIT ALINIYOR]")
    
    # Dosya oluşana kadar bekle (30 saniye bekleme - sürekli kontrol)
    max_deneme = 30
    deneme = 0
    while not os.path.exists("cevap.txt"):
        time.sleep(1)
        deneme+=1
        if deneme > max_deneme:
            return "Uzman yanıtı zaman aşımına uğradı."

    try:
        # Dosya oluştuğunda içeriği cevap değişkenine al ve cevap.txt'yi sil
        with open("cevap.txt", "r", encoding="utf-8") as f:
            cevap = f.read().strip().lower()
        os.remove("cevap.txt")
    except:
        time.sleep(1)
        return uzmana_sor(line)
    
    # Mantıksal kontroller
    if cevap in ["e", "evet"]:
        return bot_yaniti
    elif cevap in ["h", "hayır"]:
        return "Bu soruya daha iyi bir yanıtım olduğunda cevap vereceğim."
    else:
        return "Güvenlik protokolü ihlali veya geçersiz yanıt."

mod = sys.argv[1].lower()

# bilgi.txt dosyasının içeriğini lines değişkenine al
with open("bilgi.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# HOOTL modu
if mod == "hootl":
    while True:
        mesaj = input("Öğrenci: ").lower()
        # bilgi.txt'yi dolaşıp anahtar-değer şeklinde olan satırları kontrol et
        for line in lines:
            line = line.strip()
            if "|" not in line:
                continue
            # anahtar-değer şeklinde olan satırı "|" sembolünden bölerek listeye çevir
            anahtar, deger = line.split("|")
            # anahtar kelime, öğrencinin girdiği mesajın içinde var ise değeri yazdır
            if anahtar in mesaj:
                print(f"Bot: {deger}")
            else:
                print("Bot: Söylediğin şey hakkında pek bir bilgim yok ama eğer istersen farklı bir konuda yardımcı olabilirim.")

# HOTL modu
elif mod == "hotl":
    while True:
        mesaj = input("Öğrenci: ").lower()
        # Kritik ifadelerden herhangi birinin, öğrencinin girdiği mesajda olup olmadığını kontrol et
        for ifade in kritik_ifadeler:
            if ifade in mesaj:
                # Uzmana aktarma mesajı
                print("Bot: Bu durumda yanıt verebilmem doğru olmaz, en uygun kararın verilebilmesi için seni uzman tercih danışmanına yönlendiriyorum... [BAĞLANILIYOR]")
                exit()
        # Kritik ifade yoksa bilgi.txt'yi dolaşıp anahtar-değer şeklinde olan satırları kontrol et
        for line in lines:
            line = line.strip()
            if "|" not in line:
                continue
            # anahtar-değer şeklinde olan satırı "|" sembolünden bölerek listeye çevir
            anahtar, deger = line.split("|")
            # anahtar kelime, öğrencinin girdiği mesajın içinde var ise değeri yazdır
            if anahtar in mesaj:
                print(f"Bot: {deger}")
            else:
                print("Bot: Söylediğin şey hakkında pek bir bilgim yok ama eğer istersen farklı bir konuda yardımcı olabilirim.")

# HITL modu
elif mod == "hitl":
    while True:
        mesaj = input("Öğrenci: ").lower()
        # bilgi.txt'yi dolaşıp anahtar-değer şeklinde olan satırları kontrol et
        for line in lines:
            line = line.strip()
            if "|" not in line:
                continue
            # anahtar-değer şeklinde olan satırı "|" sembolünden bölerek listeye çevir
            anahtar, deger = line.split("|")
            # anahtar kelime, öğrencinin girdiği mesajın içinde var ise yanıt için uzman onayına gönder
            if anahtar in mesaj:
                print(f"Bot: {uzmana_sor(line)}")
            else:
                print("Bot: Söylediğin şey hakkında pek bir bilgim yok ama eğer istersen farklı bir konuda yardımcı olabilirim.")

else:
    print("Geçersiz mod girdiniz.\nKullanım: python bot.py [hootl/hotl/hitl]")