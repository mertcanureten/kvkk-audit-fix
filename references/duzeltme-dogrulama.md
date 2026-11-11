# Düzeltme ve doğrulama tarifleri

Bunlar önerilen mühendislik uygulamalarıdır. Mevcut mimariyi, kullanılan framework'ü ve kullanıcının işlev hedefini koruyarak uyarlayın. Hazır bir CMP/ORM/SDK seçimini bütün projelere dayatmayın. Uygulanacak her yama için: kök neden → minimal değişiklik → güvenlik/işlev testi → kalan kapsam → geri dönüş notu.

## A. Tarama pratiği

1. Manifest, route, ORM/schema/migration, auth middleware, SDK yapılandırmaları, deployment/IaC, cron/worker ve ilgili politika dosyalarını listele. `rg -l` ile aday dosyaları bul, gerekli satırları hedefli oku. Gizli `.env` değerleri yerine değişken adlarına bak; büyük dump/log veya kullanıcı dosyalarını içeri alma.
2. Alanlar: `email, phone, tckn, identity, birth, address, health, biometric, location`; alıcılar: `analytics, pixel, tracking, telemetry, sentry, webhook, smtp, openai, embedding`; yaşam döngüsü: `retention, expire, ttl, deletedAt, erase, consent`. Bunlar keşif ipucudur, hukuki bulgu değildir.
3. Aynı uç noktada middleware, servis, repository ve nesne depolama yetkisini birlikte incele. REST yanında GraphQL, websocket, batch export, mobil ve worker yollarını unutma.
4. Runtime inceleme gerekiyorsa yerel/test ortamı ve sentetik hesaplar kullan. Temiz tarayıcı profili, storage/network gözlemi ve test SDK stub'ları kullan. Üretime tarama veya exploit isteği gönderme yetkisini varsayma. HAR/cookie/token içeriğini rapordan çıkar.

## B. Takip ve rıza

Rızaya tabi izleyiciyi yalnızca HTML'den kaldırmak sunucu olaylarını durdurmaz. Yüklemeyi kategori bazlı rıza durumu üzerinden tek noktada yönet; SSR/preload, iframe, tag manager, mobil SDK, service worker ve server-side gönderimlerini kapsa. Ret halinde yeni gönderimi kes; yönetilebilir birinci taraf depoları temizle, üçüncü taraf silme sınırını yaz. Sağlayıcı özelliklerini doğrulamadan “consent mode anonimdir” deme.

Test: temiz profil ilk yükleme → ret → belirli kategori kabulü → sayfa/route değişimi → yenileme → geri çekme → yeni oturum. İlgili hedefe sıfır istek beklentisini hem istemci hem sunucuda test et. Zorunlu oturum/sepetin işlevi devam etsin. Rıza kaydını kullanıcının seçmediği kategorileri kapsayacak biçimde genişletme. Aydınlatma ve izin sürümlerini ayır; gereksiz IP/user-agent biriktirme.

## C. Erişim ve sızıntı

Her nesne erişiminde kimliği doğrulanmış sunucu bağlamından kullanıcı/tenant belirle. İstemciden gelen `tenantId` güven sınırı değildir. Sorguya sahiplik/rol koşulunu uygula; serializer alan izin listesi kullan; indirme/export yollarını aynı kurala bağla. Hata ve önbellek üzerinden nesne varlığının sızmasını da değerlendir.

Test: anonim, yetkili A, başka kullanıcı B, başka tenant C, süresi bitmiş oturum, dar yetkili destek rolü. Liste/arama, doğrudan ID, update/delete, export ve signed URL'de sınırı doğrula; yetkili kullanıcının işlemi çalışsın. Düzeltme üretime alınmadıysa yerel kapanıştan öte iddia etme.

Loglarda tüm request/response/body/header dökümü yerine gerekli alanların izin listesini kullan. Parola, token, sağlık, kimlik ve serbest metin redaksiyonu iç içe nesneler/array/hata yollarında çalışsın. Sentetik canary ile log/APM/CI çıktısında veri bulunmadığını test et. Eski loglar yama ile kaybolmaz: onların süre/imha ve olay değerlendirmesini ayrı açık iş yap. Anahtar sızıntısında rotasyon planı hazırla; yalnız `.gitignore` eklemek geçmişi temizlemez; repo geçmişini açık yetki olmadan yeniden yazma.

## D. Saklama, imha ve başvurular

Süreyi kaynaklı kategori/amaç/başlangıç olayından türet; süre bilinmiyorsa üretim verisini silebilen varsayılan uydurma. Onaylı politika yoksa yapılandırma şeması, dry-run ve eksik karar raporu hazırla. Hesap kapatma, veri silme ve kanunen saklanacak kayıtların kullanımını kısıtlamayı ayrı işlemler olarak tasarla.

İmha işi: sınırlı batch, idempotency, retry, legal hold, ilişki bütünlüğü, kuyruk/indeks/dosya yayılımı ve minimum kişisel veri içeren işlem kaydı. Soft delete ancak ilgili kullanıcıya erişilemez/tekrar kullanılamaz sonucu sağlıyorsa silme ölçütünü karşılayabilir; yok etme değildir. Pseudonymization ve şifreleme anonimleştirme değildir.

Test: tam süre sınırı, saat dilimi, geçerli legal hold, kaldırılmış hold, başka tenant, tekrar çağrı, yarıda kesilme ve retry; cache/arama/indirme yolundan erişim; yedekten dönüş sonrası silmenin tekrar uygulanması. Yedekleri sınırsız saklamayı gerekçelendirme; uygulanabilir yedek yaşam döngüsü, erişim sınırı ve yeniden kullanım engeli belgele. Canlı geri alınamaz imha yetkisi yoksa yalnızca test ve uygulanabilir migration/job hazırlığı yap.

Hak başvurusu: kayıt numarası, geliş zamanı, kimlik doğrulama, görev sahibi, son tarih, karar, teslim ve alıcıya yayılım kanıtı. Başvuruya yanıt paketinde üçüncü kişi verisini filtrele. API export özelliği yararlı olabilir; GDPR veri taşınabilirliğini KVKK'da bağımsız evrensel hak diye yazma. Otuz gün yerine keyfî iş günü hesabı kullanma; iş günü tanımlı sürelerde Türkiye tatil takvimini doğrula.

## E. Aktarım ve tedarikçi

Kodda API host'u bulmak ülke/aktarım durumunu tek başına kesinleştirmez. Endpoint, seçili region, sağlayıcı sözleşmesi, destek erişimi, alt işleyenler ve fiilî gönderilen alanları birlikte incele. Gerekirse alan minimizasyonu, PII redaksiyonu, mevcut feature flag veya test stub'ı uygula. Belirsiz hukuki sebebi “rıza kabul” bayrağıyla çözme.

Sözleşme/güvence eksiğinde doğru rol matrisi, doldurulacak ekler, teknik tedbirler, sonraki aktarım listesi ve bildirim takip taslağı üret. İmza/bildirim olmadan uyum tamamlandı deme. Türkiye region'a geçişin diğer yabancı erişimleri giderdiğini varsayma. Üretim sağlayıcı değişimi için maliyet, kayıp, kesinti ve geçiş testi gerekir.

## F. Yapay zekâ sistemleri

Prompt, dosya yükleme, tool çağrısı, embedding, cevap, tracing, değerlendirme ve eğitim akışlarını ayrı haritala. Kişisel veri içeren source ve retrieval sonuçlarına kaynak yetkisini uygula; sadece system prompt'a “veri sızdırma” yazmak erişim kontrolü değildir. Prompt injection ve diğer tenant belgesini isteme sentetik testlerini uygula.

Sağlayıcının “training off” ayarı sıfır saklama veya yurt dışı aktarım yokluğu demek değildir. Ürün/plan/region bazlı ayar ve sözleşmeyi doğrula. Eğitim setinden silme ile eğitilmiş modeldeki etkisini giderme farklıdır; ikinci işlemi yapamadığında açık sınır/riski yaz. İtiraz için gerçek insan incelemesi iş akışı gerekiyorsa görev sahibi ve karar kaydı oluştur; şeklen bir butonla tamamlanmış sayma.

## G. Hukuki metin ve kurumsal süreç

Gerçek envanterden metin üret; bilinmeyen unvan/adres/alıcı/süre/hukuki sebebi `karar gerekli` olarak taslakta tut, canlı metne tahmin koyma. “Her türlü amaçla, süresiz” gibi genel izin cümlesi ekleme. Sadece aydınlatma güncellemesi teknik veri sızıntısını çözmez. Personel eğitimi, Kurum bildirimi veya sözleşme imzası için belge taslağı hazırlamak faaliyetin gerçekleştiği anlamına gelmez.

## H. Kapanış kapısı

Test/build gereklilikleri tamam mı? Eski hata sentetik senaryoda artık oluşmuyor mu? Yetkili işlev devam ediyor mu? Tüm veri kopyaları ve geçmiş kayıtlar ele alındı mı? Hukuki/kurumsal bağımlılık kaldı mı? Kanıt hangi ortam/commit/tarihe ait? Yerel düzeltme ile üretim doğrulamasını ayrı durumla yaz. Test başarısızsa veya erişilemeyen ortam varsa raporda açık tut; sırf dosya değişti diye bulguyu kapatma.
