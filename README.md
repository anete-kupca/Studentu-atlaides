# Studentu-atlaides
Atrodi, kur vari dabūt studentu atlaidīti

# Studentu atlaides — ISIC.lv skrāperis

## Projekta uzdevums

Projekta mērķis ir izveidot Python programmu, kas automātiski iegūst informāciju par studentiem paredzētajām atlaidēm no vietnes [isic.lv/lv/atlaides](https://isic.lv/lv/atlaides/). Programma automātiski apstrādā datus un saglabā tos strukturētā JSON formātā.

## Izmantotās Python bibliotēkas

- `requests`: HTTP pieprasījumu veikšanai, lai ielādētu tīmekļa lapas saturu.
- `beautifulsoup4`: HTML dokumentu parsēšanai un vajadzīgo elementu izgūšanai no lapas.

## Izmantotās datu struktūras

Skripts izmanto Python vārdnīcu (`dict`) un sarakstu (`list`) kombināciju, lai saglabātu atlaides ar nosaukumu un aprakstu:
```python
[
  {
    "nosaukums": "McDonald’s",
    "apraksts": "15% atlaide uz visiem produktiem ar ISIC karti."
  },
  ...
]
