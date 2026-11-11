# Çıktı sözleşmesi

## İnsan raporu

`assets/rapor-sablonu.md` alanlarını gerçek verilerle doldur. İncelenen proje/commit, ortam ve erişim sınırı; mevzuat doğrulama tarihi; kontrol kapsamı; öncelikli bulgular; değişiklik ve testler; açık kararlar; kaynaklar bulunmalı. Ham kişisel veri içermeyen dosya:satır, route, sentetik test veya maskelenmiş kanıt referansı kullan. Başka insanın önceden hazırladığı belgenin yokluğu, kendisinin yükümlülüğü yerine getirmediğini kanıtlamaz.

## bulgular.json sürüm 1

Üst alanlar:
- `schema_version`: `1`
- `project`: proje tanımlayıcısı
- `revision`: commit veya açıklamalı sürüm (`git-yok` olabilir)
- `audit_date`: ISO tarih
- `mode`: `denetle`, `denetle-duzelt`, `yeniden-dogrula`
- `scope`: incelenen yüzeylerin string listesi
- `limitations`: bilinmeyen/erişilemeyen kapsamların string listesi
- `findings`: bulgu nesnelerinin listesi

Her bulgu:
- `id`: kalıcı `KVKK-001` gibi kimlik; aynı kök neden tekrarında koru.
- `control_ids`: katalog kimlikleri, ör. `["KV-29"]`.
- `title`, `observation`, `impact`: somut tetikleyici, mevcut davranış ve ilgili kişi etkisi.
- `severity`: `P0|P1|P2|P3`; `confidence`: `yuksek|orta|dusuk`.
- `classification`: `dogrulanmis-uygunsuzluk|olasi-uygunsuzluk|belge-eksikligi|iyilestirme`.
- `status`: `acik|kismi|karar-bekliyor|duzeltildi-yerel|kapandi|yanlis-pozitif`.
- `legal_basis`: `[{"source_id":"K22", "url":"https://...", "provision":"KVKK m.12; ilgili rehber bölümü", "verified_on":"YYYY-MM-DD", "verification":"dogrulandi|dogrulanamadi", "applicability":"Bu faaliyete neden uygulanıyor"}]`.
- `evidence`: `[{"kind":"code|runtime|document|test", "location":"dosya:satır veya delil yolu", "summary":"Maskelenmiş kısa gözlem"}]`.
- `remediation`: `summary` (somut yapılacak/yapılan iş), `changed_files` listesi, `owner` (bilinmiyorsa atanması gereken rol), `due_date` (bilinmiyorsa null), `rollback`.
- `verification`: `tests` listesi (`name`, `result: passed|failed|not_run`, `evidence`), `environment`, `production_verified` boolean, `production_evidence` string/null.
- `residual_risks`: string listesi; `dependencies`: string listesi.
- `decision_needed`: string/null; `resolution_note`: string/null.

`duzeltildi-yerel` testi geçilmiş teknik kapsamı gösterir; canlıya uygulanmış demek değildir. `kapandi` için test, üretim/gerçek süreç kanıtı ve tamamlanmış bağımlılıklar gerekir. Salt belge düzeltmesinde “test”, gerçek belge/işlem karşılaştırması olabilir; otomatik test zorunluluğu uydurma. `yanlis-pozitif` için karşı kanıt ve gerekçe gerekir; bulguyu silme. Çözümlenmemiş anlamlı risk/bağımlılık varsa `kismi` kullan. Hukuki kaynak doğrulanmamışsa kesin uygunsuzluk veya tam kapanış kullanma.

## Diğer dosyalar

`envanter.csv`: `islem_id,amac,rol,ilgili_kisi,veri_kategorisi,ozel_nitelik,kaynak,toplama_noktasi,depolar,alici,ulke,isleme_sarti,aktarim_mekanizmasi,aydinlatma_riza,sure,sure_dayanagi,imha,yetki,kanit,bilinmeyen`.

`kontroller.csv`: `kontrol_id,uygulanabilirlik,durum,kanit,bulgu_id,gerekce`. Katalogdaki 50 kontrolün hepsi bir satırla temsil edilmeli; uygulanamayanlar açıklanmalı. Kapsam dışı sektörü geçer sayma. Kaynak doğrulama erişimi ayrı durumdur.

`kaynaklar.json`: mevzuat sicilindeki alanları taşıyan kaynak listesi. Sadece kullanılan veya doğrulanamayan ilgili kaynakları ekle; erişmediğin kaynağa erişim tarihi atama. Paket hazırlık tarihi ile bu denetimin tarihini karıştırma.

Rapor ve JSON aynı sayıları/durumları taşımalı. Bir sorunun teknik ve kurumsal parçalarını gerekirse ayrı bağlantılı bulgulara ayır. Önerilen öncelik veya hedef tarih yasal son tarihle karıştırılmamalı. Risk kabulü uygunsuzluğu kendiliğinden kaldırmaz; açık kalır ve kabul kararı not edilir.

## Doğrulama aracı

`python3 <skill>/scripts/validate_report.py <rapor>/bulgular.json`

Araç yapısal gereklilikleri, URL biçimini ve kapanış delillerinin varlığını kontrol eder; kanıtın doğru olduğunu, hükmün yürürlükte olduğunu veya düzeltmenin çalıştığını kanıtlamaz. Gerçek test ve hukuki kaynak okumasının yerine geçmez. Sıfır bulgulu raporda kapsam sınırlamalarını ayrıca insan okuyarak değerlendir.
