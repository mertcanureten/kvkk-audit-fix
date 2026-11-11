# KVKK Audit & Fix

Yapay zekâ kodlama ajanları için Türkçe, kanıta dayalı KVKK denetim ve düzeltme skill’i.

Projenin veri akışlarını ve ilgili belgelerini inceler; uygulanabilir mevzuatı resmî kaynaklardan doğrular, bulguları raporlar, yetkilendirilmiş teknik düzeltmeleri uygular ve test eder.

## Kapsam

- 50 kontrol: aydınlatma ve rıza, çerezler, API yetkileri, tenant izolasyonu, loglar, saklama ve imha, ilgili kişi başvuruları, aktarım, VERBİS, özel nitelikli veriler ve yapay zekâ sistemleri.
- Mevzuat kaynakları ve sektöre göre ek inceleme yolları.
- Teknik düzeltme tarifleri, test senaryoları ve rapor şablonu.
- JSON rapor yapısını ve kapanış kanıtı alanlarını kontrol eden Python aracı.

## Kurulum ve kullanım

### Claude Code

Kullanıcı genelinde kurulum (hedef klasör henüz yoksa):

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/mertcanureten/kvkk-audit-fix.git ~/.claude/skills/kvkk-audit-fix
```

Yalnız belirli projede kullanmak için aynı depoyu o projenin `.claude/skills/kvkk-audit-fix` dizinine klonlayın. Mevcut kurulum varsa üzerine klonlamayın; kendi değişikliklerinizi koruyarak güncelleyin.

Claude Code içinde:

```text
/kvkk-audit-fix Bu projeyi KVKK açısından denetle, kanıtlı bulguları raporla,
güvenli yerel düzeltmeleri uygula ve test et.
```

Paket, [Claude Code’un belgelenmiş skill biçimi](https://code.claude.com/docs/en/skills) ile uyumludur: `SKILL.md`, `name`/`description` ön bilgisi ve göreli destek dosyaları kullanır. `agents/openai.yaml` denetimin çalışması için gerekli değildir. Python 3 yalnız rapor doğrulayıcısı için gerekir. Gerçek projede Claude Code ile uçtan uca denetim testi henüz yapılmamıştır.

### Codex

Depoyu `~/.codex/skills/kvkk-audit-fix` dizinine yerleştirin. Projenin çalışma alanında:

```text
$kvkk-audit-fix Bu projeyi KVKK açısından denetle, veri akışlarını çıkar,
kanıtlı bulguları raporla, güvenli yerel düzeltmeleri uygula ve test et.
```

Yalnız inceleme için “uygulama kodunu değiştirme” belirtin. Önceki raporu tekrar değerlendirmek için “bulguları aynı kimliklerle yeniden doğrula” isteyin.

Başlangıç dosyası: [SKILL.md](SKILL.md).

## Dosyalar

| Yol | İçerik |
|---|---|
| `references/mevzuat-kaynaklar.md` | Hukuki temel, kaynaklar, güncellik ve erişim sınırları |
| `references/kontrol-katalogu.md` | 50 denetim kontrolü |
| `references/sektorler.md` | Sektör tetikleyicileri ve ilgili kararlar |
| `references/duzeltme-dogrulama.md` | Düzeltme ve doğrulama yöntemleri |
| `references/raporlama.md` | Rapor ve bulgu veri sözleşmesi |
| `assets/rapor-sablonu.md` | Rapor şablonu |
| `scripts/validate_report.py` | Rapor yapısı ve kapanış alanlarının doğrulayıcısı |

Doğrulayıcı yalnızca Python standart kütüphanesini kullanır:

```bash
python3 scripts/validate_report.py /path/to/bulgular.json
```

## Sınırlar

Araştırma tarihi **11 Kasım 2026**. Her denetimde uygulanabilir hükümlerin güncel resmî metinleri yeniden doğrulanmalıdır. Erişilemeyen veya yalnızca bağlantısı keşfedilen kaynaklar kaynak dosyalarında belirtilmiştir. Bu paket bütün sektör mevzuatının eksiksiz konsolide arşivi değildir.

Skill hukuki uygunluk sertifikası vermez. Kaynak ve teknik kanıtları ayırır; belge eksikliğini otomatik ihlal saymaz. Yerel düzeltme, üretimde doğrulanmış kapanış değildir. Canlı veri silme, deploy, sözleşme imzalama veya resmî bildirim gönderme için mevcut yetki kapsamı ayrıca değerlendirilir.

Rapor doğrulayıcısının başarılı olması hukuki doğruluğu veya projenin uyumunu kanıtlamaz. Araç, bağımsız çalışan otomatik bir proje tarayıcısı değildir; denetimi yürüten ajanın ürettiği raporu kontrol eder.
