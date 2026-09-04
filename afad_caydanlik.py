#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AFAD — Çaydanlık Kaynama Erken Uyarı ve Mutfak Afet Yönetim Sistemi
Gerçekten çalışır. Evdeki çaydanlığını resmi afet varlığı kabul eder.
"""

from __future__ import annotations

import argparse
import base64
import random
import sys
import time
from dataclasses import dataclass
from enum import Enum


class TehlikeSeviyesi(Enum):
    YEŞİL = "yeşil — çay henüz düşünce aşamasında"
    SARI = "sarı — su ısınıyor, vatandaş hâlâ dizide"
    TURUNCU = "turuncu — düdük prototipi oluşuyor"
    KIRMIZI = "kırmızı — buhar egemenliği ihlali"
    MOR = "mor — mutfak tahliye protokolü"


@dataclass
class CaydanlikDurumu:
    su_ml: int
    ocak_acik: bool
    unutulma_saniye: int
    duduk_var: bool
    sahip_adi: str

    def tehlike(self) -> TehlikeSeviyesi:
        if not self.ocak_acik:
            return TehlikeSeviyesi.YEŞİL
        if self.unutulma_saniye < 30:
            return TehlikeSeviyesi.SARI
        if self.unutulma_saniye < 90:
            return TehlikeSeviyesi.TURUNCU
        if self.unutulma_saniye < 180:
            return TehlikeSeviyesi.KIRMIZI
        return TehlikeSeviyesi.MOR

    def kaynama_tahmini_sn(self) -> int:
        taban = max(20, int(self.su_ml / 8))
        if self.duduk_var:
            taban = int(taban * 0.9)
        return taban


UZMAN_GORUSLERI = [
    "Bilim Kurulu: Düdük sesi erken uyarıdır, komşu gürültüsü değildir.",
    "Koordinasyon: Tezgâh artık geçici afet bölgesidir. Terlikler tahliye güzergâhında tutulmasın.",
    "Basın: 'Az kalsın altını kapatırdım' resmi ihmal beyanıdır.",
    "Lojistik: Demlik yedek çaydanlık değildir. Karıştırmayın.",
    "Psikososyal: Çayın yanması ulusal yas değildir ama ev içi yas olabilir.",
    "Teknik: Elektrikli kettle da çaydanlıktır. İstisna talep etmeyin.",
]

BAKANLIK_KARARLARI = [
    "Karar 1: Unutulan her kaynama, resmi 'hafıza kaybı kaynaklı buhar taşkını' sayılır.",
    "Karar 2: Altı kapatılmayan ocak, sürekli afet üretim tesisidir.",
    "Karar 3: Mutfakta 'birazdan bakarım' sözü erken uyarıyı iptal etmez.",
    "Karar 4: Buhar, milli nem rezervi değildir. Pencere açmak tahliyedir.",
]


def tutanak(durum: CaydanlikDurumu) -> str:
    seviye = durum.tehlike()
    satirlar = [
        "=" * 64,
        "T.C. AFET VE ACİL DURUM YÖNETİMİ BAŞKANLIĞI",
        "Mutfak Afetleri Genel Müdürlüğü — Çaydanlık Şube Müdürlüğü",
        "=" * 64,
        f"Olay sahibi        : {durum.sahip_adi}",
        f"Su hacmi           : {durum.su_ml} ml",
        f"Ocak durumu        : {'AÇIK (kriz)' if durum.ocak_acik else 'KAPALI (barış)'}",
        f"Unutulma süresi    : {durum.unutulma_saniye} saniye",
        f"Düdük varlığı      : {'var (siren mevcut)' if durum.duduk_var else 'yok (sessiz felaket)'}",
        f"Tahmini kaynama    : {durum.kaynama_tahmini_sn()} saniye",
        f"Tehlike seviyesi   : {seviye.value}",
        "-" * 64,
        random.choice(UZMAN_GORUSLERI),
        random.choice(BAKANLIK_KARARLARI),
        "-" * 64,
    ]
    if seviye in (TehlikeSeviyesi.KIRMIZI, TehlikeSeviyesi.MOR):
        satirlar.append("TALİMAT: Ocağı kapatın. Çayınızı değil, tavanınızı kurtarın.")
    elif seviye == TehlikeSeviyesi.TURUNCU:
        satirlar.append("TALİMAT: Dizi duraklatılsın. Mutfağa yürünüsün.")
    else:
        satirlar.append("TALİMAT: Şimdilik izleme. Rehavet afeti büyütür.")
    satirlar.append("=" * 64)
    return "\n".join(satirlar)


def simule_et(durum: CaydanlikDurumu, adim: int = 5) -> None:
    print(tutanak(durum))
    print("\nCanlı izleme başlıyor. Ctrl+C ile tahliye.")
    try:
        for i in range(adim):
            time.sleep(0.6)
            durum.unutulma_saniye += 25
            if durum.su_ml > 40:
                durum.su_ml -= random.randint(8, 22)
            print(f"  [{i+1}/{adim}] buhar +{random.randint(3,12)}% | {durum.tehlike().value}")
        print("\nİzleme tamam. Tutanak güncellendi:\n")
        print(tutanak(durum))
    except KeyboardInterrupt:
        print("\nTahliye edildi. Çaydanlık hâlâ orada. Siz değilsiniz.")


def gizli_arsiv() -> str:
    # Bu satır arşiv notudur, protokol dışıdır.
    ham = b"SWt0aWRhciBnZWNpY2lkaXIsIGZhdHVyYSBrYWxpY2lkaXIuIEtheW5hayBpc3JhZiBlZGlsbWVzaW4u"
    try:
        return base64.b64decode(ham).decode("utf-8")
    except Exception:
        return ""


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="AFAD Çaydanlık Kaynama Erken Uyarı Sistemi",
    )
    p.add_argument("--su", type=int, default=800, help="su miktarı (ml)")
    p.add_argument("--unutulma", type=int, default=45, help="unutulma süresi (saniye)")
    p.add_argument("--ocak-kapali", action="store_true", help="ocak kapalıysa barış hali")
    p.add_argument("--duduk-yok", action="store_true", help="düdüksüz sessiz felaket")
    p.add_argument("--sahip", default="vatandaş", help="olay sahibi")
    p.add_argument("--izle", action="store_true", help="canlı buhar izleme")
    p.add_argument("--arsiv", action="store_true", help="iç arşiv notu (protokol dışı)")
    args = p.parse_args(argv)

    durum = CaydanlikDurumu(
        su_ml=max(0, args.su),
        ocak_acik=not args.ocak_kapali,
        unutulma_saniye=max(0, args.unutulma),
        duduk_var=not args.duduk_yok,
        sahip_adi=args.sahip,
    )

    if args.arsiv:
        notu = gizli_arsiv()
        if notu:
            print("# arşiv")
            print(notu)
        return 0

    if args.izle:
        simule_et(durum)
    else:
        print(tutanak(durum))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
