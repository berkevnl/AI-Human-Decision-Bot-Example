# Üniversite Tercih Danışmanı

Öğrenci sınav sonucunu, hedeflerini, ilgi alanlarını, bulunduğu şehri ve benzer bilgileri bota yazar; bot ise bilgileri önceden belirlenmiş verilerle eşleyerek en uygun cevabı verip öğrenciye yardımcı olmaya çalışır veya uzman tercih danışmanına yönlendirir.

## Hedef Kitle

Hedef kitle, üniversite adayı öğrencilerdir. Bu öğrenciler, üniversite sınavı sonuçlarının açıklanmasının ardından isteklerine en uygun ve doğru tercih listesini elde edebilmek için bu botu kullanır.

# Modlar

## HOOTL (Human-Out-Of-The-Loop)

Bu modda bot, öğrenci ile olan iletişimine göre sürdürülür ve gerekli dönütler bot tarafından otomatik olarak verilir.

Süreçte uzmandan herhangi bir onay istenmez, tamamen bot tarafından yürütülür.

Kesin, duygusallıktan uzak ve genel veriler karşısında doğru yanıt; duygusallık içeren, genelden uzak ve daha spesifik veriler karşısında hata yapmaya meyilli olacaktır.

## HOTL (Human-On-The-Loop)

Bu mod çoğunlukla botun;
- Emin olamadığı
- Riskli gördüğü
- Standart verilerle çözemediği
durumlarda devreye girer.

Öğrencinin;
- "Tıp istiyorum ama biyolojiden nefret ediyorum."
- "Yazılım mı hukuk mu psikoloji mi hiçbir fikrim yok."
- "Ailem tıp okumamı istiyor, ben işletme istiyorum."
- "Sevgilimle okumak istiyorum."
- "Bu tercih tüm hayatımı değiştirecek."
- "Bu üniversitenin ortamı gerçekten nasıl?"
tarzda ifadeleri veya sağlık problemi, ekonomik durum, şehir zorunluluğu gibi özel durumlar karşısında bot, riskli bir karar alıp hata yapmak istemeyeceği için öğrenciyi uzman bir danışmana yönlendirir.

## HITL (Human-In-The-Loop)

Bu modda operatör, *Uzman Tercih Danışmanı*'dır. Süreç HOOTL modundaki gibi öğrenci ve bot iletişimine göre sürdürülür. Operatör, aktif olarak sürecin içerisinde yer alır ve botun her yanıtını yönetme hakkına sahiptir.