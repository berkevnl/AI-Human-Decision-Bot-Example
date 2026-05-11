# Üniversite Tercih Danışmanı Botu

> ⚠️ Bu proje gerçek bir ürün değildir. İnsan-Makine Döngüsü (Human-in-the-Loop) kavramını ve otomasyon seviyelerini pratik olarak incelemek amacıyla hazırlanmış **akademik bir araştırma çalışmasıdır.**

---

## Amaç

Bu çalışma, bir chatbot sisteminde **insanın karar sürecine ne ölçüde dahil edilmesi gerektiği** sorusunu araştırmaktadır. Bunun için farklı otomasyon seviyelerine sahip üç çalışma modu tanımlanmış ve bu modlar üniversite tercih danışmanlığı senaryosu üzerinden somutlaştırılmıştır.

---

## Nasıl Çalışır?

Sistem iki bileşenden oluşur:

- **`bot.py`** — Öğrenciyle diyalog kuran bileşen. `bilgi.txt` dosyasındaki anahtar–yanıt eşleşmelerini kullanarak girilen mesajlara cevap üretir.
- **`operator.py`** — HITL modunda çalışan uzman paneli. Botun önereceği yanıtları, uzmanın onayına sunar.

Botun bilgi tabanı (`bilgi.txt`) düz metin formatında, `anahtar|yanıt` eşleşmeleri içeren satırlardan oluşur. Anahtar kelime öğrencinin mesajında geçiyorsa bot karşılık gelen yanıtı kullanır.

---

## Çalışma Modları

| Mod | Açıklama |
|-----|----------|
| **HOOTL** *(Human-Out-Of-The-Loop)* | Tamamen otomatik. İnsan müdahalesi yoktur; bot tüm kararları kendi verir. |
| **HOTL** *(Human-On-The-Loop)* | Bot yine de otomatik çalışır; ancak duygusal veya riskli ifadeler tespit edildiğinde süreci durdurarak öğrenciyi uzmana yönlendirir. |
| **HITL** *(Human-In-The-Loop)* | Botun her yanıtı, gönderilmeden önce uzmanın onayından geçer. Uzman "E" derse yanıt iletilir, "H" derse bot farklı bir yanıt arar. |

---

## Çalıştırma

```bash
# HOOTL modu
python bot.py hootl

# HOTL modu
python bot.py hotl

# HITL modu (önce operator.py'yi ayrı bir terminalde başlatın)
python operator.py
python bot.py hitl
```

HITL modunda `bot.py` ve `operator.py` **eş zamanlı** çalıştırılmalıdır. İki süreç, `soru.txt` ve `cevap.txt` geçici dosyaları üzerinden haberleşir.

---

## Dosya Yapısı

```
AI-Human-Decision-Bot-Example/
├── bot.py                          # Ana bot mantığı (3 mod)
├── operator.py                     # Uzman onay paneli (HITL için)
├── bilgi.txt                       # Anahtar-yanıt bilgi tabanı
├── SPEC.md                         # Sistem spesifikasyonu
├── rapor.pdf                       # Araştırma raporu
├── README.md
└── arastirma/                      # Referans ekran görüntüleri
    ├── humworkai_mainpage.png          # Humwork AI ana sayfa
    ├── hireahuman_launch_linkedin.png  # HireAHuman – LinkedIn duyurusu
    └── hireahuman_maintenance.png      # HireAHuman – bakım modu ekranı
```

---

## Kısıtlamalar

Bu proje kavramsal düzeyde bir prototiptir; üretim ortamı için tasarlanmamıştır:

- Bilgi tabanı statik ve sınırlıdır; gerçek bir NLP/LLM motoru içermez.
- Süreçler arası iletişim dosya tabanlıdır (gerçek sistemde bir mesaj kuyruğu kullanılır).
- Hata yönetimi ve güvenlik katmanları minimumda tutulmuştur.
