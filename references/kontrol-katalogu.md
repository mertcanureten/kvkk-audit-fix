# Uygulanabilirlik ve kontrol kataloğu

Kaynak K kodları [mevzuat-kaynaklar.md](mevzuat-kaynaklar.md) içindedir. Aşağıdaki kontroller hukuki hükümlerin teknik değerlendirme yöntemleridir; belirtilen teknoloji veya mimari kanunun kelimesi kelimesine emri değildir. Risk ve uygulanabilirlik bağlamını değerlendir. Her satır için kod + runtime + belge kanıtının hangisinin mevcut olduğunu kaydet. Kontrol geçişi için sırf anahtar sözcük bulunması yeterli değildir.

| Kimlik | İnceleme ve beklenen kanıt | Düzeltme / kapanış ölçütü | Dayanak |
|---|---|---|---|
| KV-01 | Sorumlu, işleyen, alt işleyen; amaç ve karar yetkisi | İşlem bazlı roller ve sözleşme/fiilî davranış eşleşir | K01 m.3,12 |
| KV-02 | Form→API→DB→alıcı→imha zinciri; arka plan işler dahil | Bütün bilinen toplama/çıkış noktaları envanterde; bilinmeyenler görünür | K18 |
| KV-03 | İşleme amacı ve m.5/6 şartı; rızaya yanlış toplu dayanak | Her amaç için somut gerekçe; hukuk kararı eksikse açık bulgu | K01–K03 |
| KV-04 | İstisna iddiaları: m.28, kişisel kullanım, anonim veri | Şartları kanıtlı uygulanabilirlik; herkese muafiyet çıkarılmaz | K01 m.28 |
| KV-05 | Gereksiz TCKN, doğum tarihi, adres, rehber/konum alanları | UI ve API'de minimizasyon; toplu payload'da yasak alanın reddi/ayıklanması | K01 m.4 |
| KV-06 | Yanlış veri güncelleme, türetilmiş kayıtlara yayılım | Düzeltme ana depo, indeks ve alıcı süreçlerine ulaşır | K01 m.4,11 |
| KV-07 | Aydınlatma içeriği ve gerçek alıcı/amaç eşleşmesi | Faaliyete özel, erişilebilir ve doğru metin; bilinmeyen şirket bilgisi uydurulmaz | K10–K11 |
| KV-08 | Toplama anı, dolaylı toplama ve değişen amaç | Doğru zamanda bilgilendirme; metin sürümü ve sunum delili | K10 |
| KV-09 | Aydınlatma ile rızanın aynı kutuda/onayda birleşmesi | Bilgilendirme ve irade beyanı ayrıdır; aydınlatma bir rıza kapısı değildir | K10; 2026/347 |
| KV-10 | Önceden seçili, zorunlu, belirsiz veya paket rıza | Amaç bazlı aktif seçim; hizmete gerekmediğinde reddetme hizmeti bozmaz | K02; K21 |
| KV-11 | Rızanın kanıtı, kapsamı, sürümü, geri çekilmesi | Sunucu kaynaklı kayıt ve gelecekteki ilgili işlemeyi durdurma; geçmiş rıza uydurulmaz | K02; K21 |
| KV-12 | Çerez, piksel, localStorage, SDK, iframe, fingerprint | Amaç/sağlayıcı/süre/şart envanteri; adından gerekli sayılmaz | K21 |
| KV-13 | Rıza gereken takipte ilk yükleme, SSR, tag manager ve sunucu olayı | Geçerli seçimden önce hiçbir ilgili istek/olay yok; salt banner testi yetmez | K21 |
| KV-14 | Kabul/ret/tercih/geri çekme, erişilebilirlik ve dil | Ret ve geri çekme fiilen çalışır; eski oturum/kuyruk davranışı testlidir | K21 |
| KV-15 | Pazarlama ileti izni ile KVKK rızasının karışması | Amaç ve kanal ayrımı; 6563/IYS kapsam değerlendirmesi | S01; KVKK m.5,10 |
| KV-16 | Abonelikten çıkma sonrası gönderim, sağlayıcı ve retry kuyruğu | Ret gönderim anında da uygulanır; teslim/senkron kanıtı | S01–S02 |
| KV-17 | Yurt içi alıcı aktarımı ve erişim amacı | Alıcı, veri alanları ve m.8 şartı doğrulanır | K01 m.8 |
| KV-18 | Yabancı bulut, log, analitik, e-posta, destek, CDN ve alt işleyen | Fiilî alıcı/ülke/uzaktan erişim ve sonraki aktarım haritası | K05–K06 |
| KV-19 | Aktarım güvencesi, yeterlilik veya arızi istisna delili | Doğru mekanizma belgeyle kanıtlı; sadece DPA/GDPR/yerel region yeterli değil | K05–K08 |
| KV-20 | Standart sözleşme türü, imza, ek, bildirim | Rol doğru; süre ve bildirim kanıtı; imzasız taslakla kapanmaz | K07–K08 |
| KV-21 | Kategori bazlı süre, başlangıç olayı ve hukuki dayanak | Onaylı süre tablosu; bütün kayıtlara keyfî 30/90 gün atanmaz | K12; sektör mevzuatı |
| KV-22 | Süre dolumu, rıza geri çekme, hesap silme, legal hold | İşleme şartı ve saklama zorunluluğu ayrışır; job/dry-run testi | K12 |
| KV-23 | Soft delete, eski dosya URL'si, arama, cache, queue, replikalar | İlgili kullanıcı yeniden erişemez/kullanamaz; seçilen imha türünün şartı sağlanır | K12 |
| KV-24 | Yedekleme, geri yükleme ve silinen verinin geri gelmesi | Erişim sınırı, yaşam döngüsü, silme işaretinin restore sonrası uygulanması | K12; K22 |
| KV-25 | Hash/pseudonym/tokenization ile anonimlik iddiası | Eşleştirme ve yeniden tanımlama testi; salt hash anonim kabul edilmez | K12 m.10 |
| KV-26 | Başvuru kanalı, kimlik doğrulama, temsil ve güvenli cevap | Başkasının verisi verilmez; usul ve orantılı doğrulama karşılanır | K13–K15 |
| KV-27 | Başvuru takibi, zamanlayıcı, gerekçeli yanıt, alıcıya yayılım | En geç 30 gün takibi; teslim kanıtı; çözülmeyen işler eskale edilir | K12–K15 |
| KV-28 | Münhasır otomatik analizle aleyhe sonuç ve itiraz | İşlem izi, erişilebilir itiraz ve yetkili inceleme iş akışı | K01 m.11/1-g; K23 |
| KV-29 | Nesne sahipliği ve tenant izolasyonu: okuma/yazma/indirme | Her giriş yolunda sunucuda denetim; tenant A, B'yi okuyamaz | K22; m.12 |
| KV-30 | Yönetici, destek, servis hesabı ve işten ayrılanlar | En az yetki, görev ayrımı, iptal ve erişim kayıtları | K22; K04 |
| KV-31 | Oturum, reset, token, parola ve gizli anahtarlar | Güvenli saklama/taşıma, süre ve iptal; log/query string'e sır yazılmaz | K22; m.12 |
| KV-32 | Debug, APM, hata, telemetry, oturum kaydı | Alan izin listesi/redaksiyon; hata yollarında kişisel veri sızmaz | K22; m.4,12 |
| KV-33 | Public bucket, signed URL, export ve önbellek | Nesne yetkisi, süreli erişim, özel cache davranışı | K22; m.12 |
| KV-34 | TLS, disk/veritabanı/yedek şifreleme ve anahtar erişimi | Etkin ayar ve bağımsız anahtar yetkisi; sadece konfigürasyon adı kanıt değil | K22; K04 |
| KV-35 | Üretim verisi test/seed/fixture/CI/artifact içinde | Sentetik veriye geçiş; geçmiş sızıntı için ayrıca olay/temizleme planı | K22; m.4,12 |
| KV-36 | Bağımlılıklar, webhook, SSRF, injection, dosya yükleme | Kişisel veriye etkili yol doğrulanır; uygun negatif test ve düzeltme | K22; m.12 |
| KV-37 | Özel nitelikli veri alanları ve yetkisiz arama/indeksleme | M.6 şartı + ek tedbirler; ayrı erişim ve güvenli aktarım kanıtı | K03–K04 |
| KV-38 | Biyometrik veri, yüz şablonu ve mesai takibi | Faaliyetin güncel ilke kararına uygunluğu; daha az müdahaleci alternatif | S07 |
| KV-39 | Olay tespit, bildirim zinciri, öğrenme zamanı ve delil koruma | Olay prosedürü, süre takibi ve tatbikat; açığı ihlalle karıştırma | K16–K17 |
| KV-40 | VERBİS kapsamı, istisna kanıtı, kayıt ve envanter tutarlılığı | Şirket/dönem bilgileriyle değerlendirme; sadece headcount yetmez | K18–K20 |
| KV-41 | Eğitim, gizlilik, işleyen denetimi, politika sorumluları | Gerçek kayıt ve tarih; taslak belge tamamlanmış faaliyet değildir | K04; K22 |
| KV-42 | LLM prompt/cevap, trace, moderasyon ve embedding çıkışları | Alan minimizasyonu; sağlayıcı/ülke/süre/eğitim kullanımının doğrulanması | K23; K05 |
| KV-43 | RAG'de kaynak yetkisi ve vektör arama tenant ayrımı | Erişim retrieval öncesinde/sonrasında doğru; başka kullanıcı belgesi dönmez | K23; m.12 |
| KV-44 | Silinen kaynakların embedding, cache ve model eğitimindeki izi | Silme zinciri; modelden çıkarma imkânsızsa kalan risk/çözüm açık | K23; K12 |
| KV-45 | Model eğitimi, fine-tune, değerlendirme setleri ve amaç genişlemesi | Eğitim/çıkarım ayrı gerekçeli; sağlayıcı sözleşmesi teknik ayarla tutarlı | K23; m.4–6,9 |
| KV-46 | Çocuklar, çalışanlar ve kırılgan gruplar | Bağlam/temsil/özgür irade analizi; GDPR yaşını otomatik ithal etme | K01–K03; sektör kuralları |
| KV-47 | Mobil izinler, arka plan konum, push, crash SDK | İşletim sistemi izni ile KVKK şartı/aydınlatması ayrılır; amaçla sınırlı erişim | K01; K10; K21 |
| KV-48 | CCTV/ses, belge OCR, kimlik kopyası ve fiziksel kayıt | Gereklilik, alan, süre, erişim ve sektörel karar; sınırsız kayıt yok | K01; S05; K22 |
| KV-49 | Kamuya açık listeler, borç/başarı bilgileri ve arama motoru | Yetki/minimizasyon ve kaldırma; yalnız noindex erişim kontrolü sayılmaz | S08; m.4,12 |
| KV-50 | Sadakat hesabı doğrulama ve OTP'nin pazarlama iznine çevrilmesi | Doğrulama amacı ayrılır; karar kapsamı ve geçiş süresi güncel | S03; S06 |

Eksik altyapı erişimi olan kontrol `dogrulanamadi` kalır. Örneğin repoda şifreleme ayarı yok diye canlı DB'nin şifresiz olduğunu iddia etme. Kapsam dışındaki güvenlik kusurlarını gereksiz genişletme; kişisel veri etkisini göster.
