# ISIC atlaides — tīmekļa skrāpētājs

## Problēmas apraksts

Mums nepieciešams ātrs veids, kā pārskatīt visus pieejamos piedāvājumus, kur varam izmantot studentu atlaižu karti. Vēlamies arī iespēju ātri pārbaudīt vai kādam konkrētam uzņēmumam ir pieejama atlaide vai nē

## Mērķis

Programmas mērķis ir prast automātiski nolasīt ISIC mājaslapā pieejamo atlaižu informāciju — uzņēmumu nosaukumus un attiecīgās atlaides. Vēlamies arī lai būtu iespēja to izvadīt pārskatāmā veidā 

## Izmantotās Python bibliotēkas

- `beautifulsoup4`: analizē HTML saturu un ļauj viegli atrast vajadzīgos elementus lapā
-  `selenium`: ļauj mijiedarboties ar mājaslapu
-  `webdriver_manager`: sagatavo visu, kas vajadzīgs, lai selenium varētu palaist pārlūku
-  `time`: ļauj uzlikt pauzi starp darbībām, lai mājaslapa paspēj ielādēties

## Programmas darbības apraksts

- Atver ISIC atlaižu lapu
- Nolasa informāciju par katru uzņēmumu, kam pieejama atlaide
- Izvada katra uzņēmuma nosaukumu konsolē un izvada konsolē atlaides apjomu
- Saglabā atlaižu datus vārdnīcas formātā
- Ļauj lietotājam ievadīt uzņēmuma nosaukumu un uzzināt pieejamo atlaidi ja tāda ir
- pievienoju funkcijai iespēju ļaut meklēšanu veikt pēc daļēja nosaukuma(piemēram ar mazajiem burtim vai kādu gramatisku kļūdu)

## Iespējamie uzlabojumi

- Saglabā datus excel tabulā
  
