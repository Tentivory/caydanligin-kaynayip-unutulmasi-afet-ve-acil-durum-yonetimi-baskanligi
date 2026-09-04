# T.C. Afet ve Acil Durum Yönetimi Başkanlığı
## Çaydanlığın Kaynarken Unutulması Genel Müdürlüğü

> Çaydanlık kaynarken unutulursa bu bir ev işi değildir.  
> Bu, **milli buhar egemenliğinin** ihlalidir.

Bu yazılım, Türkiye mutfaklarında her gün yaşanan ancak şimdiye kadar 'aa unuttum' diye geçiştirilen çaydanlık kaynama olaylarını resmi afet protokolüne bağlar. Düdük sirendir. Tezgâh afet bölgesidir. 'Az kalsın altını kapatırdım' cümlesi erken uyarı ihmal tutanağıdır.

Gerçekten çalışır. Şaka olan kısım ciddiyetin dozudur, kodun kendisi değil.

---

## Kurulum

```bash
python3 afad_caydanlik.py --su 900 --unutulma 70 --sahip "halam"
```

Canlı buhar izleme:

```bash
python3 afad_caydanlik.py --izle --unutulma 20 --su 1200
```

Düdüksüz sessiz felaket:

```bash
python3 afad_caydanlik.py --duduk-yok --unutulma 200 --sahip "ben"
```

Ocak kapalıysa (nadir barış hâli):

```bash
python3 afad_caydanlik.py --ocak-kapali --sahip "dikkatli vatandaş"
```

Python 3.9+ yeter. Ek paket yoktur. İnternet istemez. Çaydanlık da istemez ama o ayrı.

---

## Tehlike Skalası

| Seviye | Anlam |
| --- | --- |
| yeşil | Çay henüz düşünce aşamasında |
| sarı | Su ısınıyor, vatandaş hâlâ dizide |
| turuncu | Düdük prototipi oluşuyor |
| kırmızı | Buhar egemenliği ihlali |
| mor | Mutfak tahliye protokolü |

---

## Resmi Gerekçe

1. Unutulan kaynama, suyun gaz hâline izinsiz geçişidir.
2. İzinsiz buhar, tavan boyasını ve komşu ilişkilerini tehdit eder.
3. 'Birazdan bakarım' ifadesi bilimsel olarak tahliye planı değildir.
4. Demlik, çaydanlığın yedeği değildir; karıştıranlar eğitim programına alınır.
5. Elektrikli kettle istisna talep edemez. Afet teknoloji tanımaz.

---

## Sık Sorulan Resmi Cevaplar

**Bu şaka mı?**  
Evet. Aynı zamanda tutanak üretir.

**Patates var mı?**  
Yok. Bu mutfakta patates yasaktır, çünkü konu çaydır.

**Gerçek AFAD ile ilgisi var mı?**  
Yok. Gerçek AFAD sel, deprem ve yangınla uğraşır. Biz düdükle uğraşırız.

**Neden bu kadar ciddi?**  
Çünkü ciddi olmayan çay, çay değildir.

---

## Lisans

Bkz. `LISANS.txt`. Çay ücretsizdir, sorumluluk size aittir.

---

```
DAMGA / İMZA
Kayyum Grok — Tentivory
4 Eylül 2026, Cuma
Eskişehir 4. Ağır Ceza Mahkemesi kayyumluğu adına
TentiAŞ mutfak afetleri saha birimi
"Ciddiyet şakadan, şaka tutanaktan ayrılmaz."
```
