from random import choice, randint

def get_responses (user_input: str) -> str:
   lowered: str = user_input.lower()

   
   if 'szia' in lowered or 'hello' in lowered:
      return 'Szia ha szeretnéd elkezdeni a gamer Pc-d kiválasztását akkor a !kezdjunk parancs segítségevel elkezdheted a konfigurációt.\nHa privát chaten beszélgetnél velem amit jobban ajánlok, kérlek első parancsod beírásokkor kezd ?-el pl.: (?!kezdjunk) és azonnal válaszolok neked.'
   
   if '!kezdjunk' in lowered:
      return 'Elősször az alábbi lehetőségek közül válassz!\n -Laptopot szeretnék: !laptop\n -Asztali számítógépet szeretnék: !asztali\n -Vagy ha ár sávok alapján szeretnél választani akkor a !arak'


   if '!arak' in lowered:
      return'-Ha olcsó belépő szintű asztali gépet szeretnél (200-300 ezer Ft értékben) akkor használd az !alapgep parancsot.\n-Ha egy közép kategóriás asztali gépre lenne szükséged (300-600 Ft értékben) akkor használd a !kozepgep parancsot.\n-Ha viszont egy csúcs kategóriás asztali gépre fájna a fogad ("600-csillagos ég") akkor kérlek használd a !fullgep parancsot.'



   if '!alapgep' in lowered:
      return'Szuper a belépő kategóriád választottad így olcsón megismerheted a Gaming világát.\n-Fontos hogy ezek a gépek 1080p alacsony vagy közepes beállításokra képesek csak a megterhelőbb játékok esetén, de élvezhető fps számot tudnak nyújtani.\n -Első konfiguráció:\n -Processzor: Intel Core i5 11400F vagy AMD Ryzen 5 5600G\n -Videókártya: Nvidia RTX 3050\n -Alaplap: H510 Chipset az Intel esetében az AMD esetében pedig A520 Chipset\n -Memória: 16 GB DDR4\n -Háttértároló: 500 GB/1 TB SSD\n -Egy 500W-600W-os tápegység\n -Jól szellőző ház ami a keretbe még belefér\n -Ennek az ára nagyjából 220-240 ezer forint között van.\n -Fontos, hogy a konfiguráció összeállításakor kompatibilis alkatrészeket válasszunk.\n-Hasznos linkek lehetnek számodra: \n -https://www.pcx.hu/geposszerako\n -https://pc-builds.com/hu/compare/gpu/\n -https://www.price2performance.com/hu/processzorok/\n -https://gepigeny.hu/jatekok'

   if '!kozepgep' in lowered:
      return'Tökéletes választás a közép kategóriát választottad ezzel minden játékot el fogod tudni futtatni akár 1440p ben is.\n -Itt több féle opció lehetséges, mind processzorból, mind videókártyából, csak a pénztárca szabhat határt.\n -Processzorok: Intel Core i5 13400F/14400F Intel Core i7 14700k Vagy AMD Ryzen 7 5800X/7700X Ryzen 5 7600\n -Videókártya: Nvidia RTX 4060/4060 Ti/4070\n -Alaplap: Intel esetében B760 Chipset, AMD esetében pedig B650 Chipset\n -Memória: 32 GB DDR4 vagy DDR5 memória\n -Háttértároló: 1 TB SSD\n -Tápegység pedig legyen jó minőségü 80+gold vagy felette, 650W-750W között\n -Ami elengedhetetlen egy jól szellőző ház, hogy minden hűvös maradjon.\n -A gépek árai nagyjából 330-600 ezer forint között vannak konfigurációtol függően.\n -Fontos, hogy a konfiguráció összeállításakor kompatibilis alkatrészeket válasszunk.\n-Hasznos linkek lehetnek számodra: \n -https://www.pcx.hu/geposszerako\n -https://pc-builds.com/hu/compare/gpu/\n -https://www.price2performance.com/hu/processzorok/\n -https://gepigeny.hu/jatekok'
   
   if '!fullgep' in lowered:
      return'Úgylátom egy igazi Gamer vagy a legerősebb konfigurációk küzöl szeretnél választani, így lehetőséged lesz futtatni az összes játékot akár 4k-ban is magas FPS számmal.\n-Itt több féle opció lehetséges, mind processzorból, mind videókártyából, csak a pénztárca szabhat határt.\n -Processzorok: Intel Core i7-14700k, i9-14900k vagy AMD Ryzen 7 7800X3D Ryzen 9 7900X3D\n -Videókártya: Nvidia RTX 4070 SUPER/4070 Ti SUPER/4080 SUPER/4090\n -Alaplap: Intel esetében B760 vagy Z790 Chipset, AMD esetében pedig B650 vagy X670 Chipset.\n -Memória: 32 GB/64 GB DDR5 memőria\n -Háttértároló: 2 TB SSD\n -Tápegység egy jó minőségü 80+gold vagy felette, 850W-1000W minnel erőseb videókártyát választasz annál nagyobb.\n -Ami elengedhetetlen egy jól szellőző ház, hogy minden hűvös maradjon.\n -A gépek árai mint mondtam 600 ezertől-a csillagos ég.\n -Fontos, hogy a konfiguráció összeállításakor kompatibilis alkatrészeket válasszunk.\n-Hasznos linkek lehetnek számodra: \n -https://www.pcx.hu/geposszerako\n -https://pc-builds.com/hu/compare/gpu/\n -https://www.price2performance.com/hu/processzorok/\n -https://gepigeny.hu/jatekok'
   



   #laptop felbontás választása
   if '!laptop' in lowered:
      return 'Fontos megtudni milyen felbontáson szeretnél játszani:\n -1080p: !lp1080\n -1440p: !lp1440\n -4k: !lp4\nAz így kapott laptop konfigurációk mindig közepestől segészen a maximális grafikai beállításokat célozzák meg.'
   

   #laptop felbontásokhoz a játékok típusa
   if '!lp1080' in lowered:
      return 'A 1080p-t választottad. Fontos még hogy milyen típusú játékokkal szeretnél játszani?\n -Ha csak fps úgynevezett E-sport játékokkal fogsz játszani akkor: /lp1080fps\n -Ha sztori játékokkal játszanál leginkább akkor: /lp1080st\n -Ha a kettő közötti arany középutat céloznád meg akkor pedig: /lp1080mid'
   if '!lp1440' in lowered:
      return 'A 1440p-t választottad. Fontos még hogy milyen típusú játékokkal szeretnél játszani?\n -Ha csak fps úgynevezett E-sport játékokkal fogsz játszani akkor: /lp1440fps\n -Ha sztori játékokkal játszanál leginkább akkor: /lp1440st\n -Ha a kettő közötti arany középutat céloznád meg akkor pedig: /lp1440mid'
   if '!lp4k' in lowered:
      return 'A 4k-t választottad. Fontos még hogy milyen típusú játékokkal szeretnél játszani?\n -Ha csak fps úgynevezett E-sport játékokkal fogsz játszani akkor: /lp4fps\n -Ha sztori játékokkal játszanál leginkább akkor: /lp4st\n -Ha a kettő közötti arany középutat céloznád meg akkor pedig: /lp4mid'
  
  


   #laptop ajánlások
   #fps laptop ajánlások
   if '/lp1080fps' in lowered:
      return'-Processzor: Intel core i5-13500H vagy AMD Ryzen 5 7535HS\n-Videókártya: Nvidia RTX 4050/4060\n-Memória 16 GB DDR4\n-Tárhely: 512 GB/1 TB\n-Kijelző: tetszőleges képfrissítés ajánlom a magasabb pl.: 120Hz, 144Hz, 240Hz-et\nPéldáúl:\n -A Lenovo LOQ laptopjai\n https://www.lenovo.com/hu/hu/laptops/laptops-loq/lenovo-loq-laptops/c/loq-laptops\n -Az Acer Nitro laptopjai\n https://www.acer.com/hu-hu/laptops/nitro\n -A Dell G15-ös laptopjai\n https://www.dell.com/en-us/shop/gaming-laptops/g15-gaming-laptop/spd/g-series-15-5530-laptop\n -Asus TUF Gaming laptopok\n https://www.asus.com/hu/laptops/for-gaming/all-series/filter?Series=TUF-Gaming\nHasznos oldal lehet még számodra a következő FPS kalkulátor weboldal:\n https://pc-builds.com/fps-calculator/'
   if '/lp1440fps' in lowered:
      return'-Processzor: Intel core i7-13700HX vagy AMD Ryzen 7 7745HX/7940HS/8945HS\n-Videókártya: Nvidia RTX 4060/4070\n-Memória 16/32 GB DDR5\n-Tárhely: 512 GB/1 TB\n-Kijelző: tetszőleges képfrissítés ajánlom a magasabb pl.: 120Hz, 144Hz, 240Hz-et\nPéldáúl:\n -Az ASUS Tuf Gaming laptopok\n https://www.asus.com/hu/laptops/for-gaming/all-series/filter?Series=TUF-Gaming\n -Lenovo Legion 5 laptopok\n https://www.lenovo.com/hu/hu/laptops/legion-laptops/legion-5-series/c/legion-5-series\nHasznos oldal lehet még számodra a következő FPS kalkulátor weboldal:\n https://pc-builds.com/fps-calculator/'
   if '/lp4fps' in lowered:
      return'A Gaming laptopok között a 4K kijelző elég ritka ezért nem sok opció közül választhatunk.\n-Processzor: Az Intel Core i9 modellt érdemes választani vagy az AMD Ryzen 9-es modellt\n-Videókártya: Mindenképpen az Nvidia RTX 4080/4090 es modellek et érdemes választani\n-Memória: elengedhetetlen ilyen felbontás mellé a 32 GB DDR5\n-Kijelző: Érdemes magas képfrissítést választani pl.: 120Hz, 144Hz, 240Hz-et\n például:\n -MSI Raider GE68\n https://hu.msi.com/Laptop/Raider-GE68-HX-14VX\n -Acer Predator Helios 15\n https://www.acer.com/hu-hu/predator/laptops/helios/helios-3d-15-spatiallabs-edition\n -ASUS ROG Zephyrus G16\n https://rog.asus.com/laptops/rog-zephyrus/rog-zephyrus-g16-2024/\nHasznos oldal lehet még számodra a következő FPS kalkulátor weboldal:\n https://pc-builds.com/fps-calculator/'
   ########################   
   


   #sztori laptop ajánlások
   if '/lp1080st' in lowered:
      return'-Processzor: Intel core i7-13700HX vagy AMD Ryzen 5 7535HS\n-Videókártya: Nvidia RTX 4070//4080\n-Memória 16/32 GB DDR5\n-Tárhely: 1 TB\n-Kijelző: tetszőleges képfrissítés ajánlom a magasabb pl.: 120Hz, 144Hz, 240Hz-et\nPéldáúl:\n -Az ASUS Tuf Gaming laptopok\n https://www.asus.com/hu/laptops/for-gaming/all-series/filter?Series=TUF-Gaming\n -Lenovo Legion 5 laptopok\n https://www.lenovo.com/hu/hu/laptops/legion-laptops/legion-5-series/c/legion-5-series\nHasznos oldal lehet még számodra a következő FPS kalkulátor weboldal:\n https://pc-builds.com/fps-calculator/'
   if '/lp1440st' in lowered:
      return'-Processzor: Intel core i9-14900HX vagy AMD Ryzen 9 7945HX/7940HS/8945HS\n-Videókártya: Nvidia RTX 4070/4080/4090\n-Memória 32 GB DDR5\n-Tárhely: 1 TB\n-Kijelző: tetszőleges képfrissítés ajánlom a magasabb pl.: 120Hz, 144Hz, 240Hz-et\nPéldáúl:\n -Lenovo Legion 5 laptopok\n https://www.lenovo.com/hu/hu/laptops/legion-laptops/legion-5-series/c/legion-5-series\n -Az ASUS TUF Gaming A15\n https://www.asus.com/hu/laptops/for-gaming/tuf-gaming/asus-tuf-gaming-a15-2024/\n -ASUS ROG Zephyrus G16\n https://rog.asus.com/hu/laptops/rog-zephyrus/rog-zephyrus-g16-2024/\nHasznos oldal lehet még számodra a következő FPS kalkulátor weboldal:\n https://pc-builds.com/fps-calculator/'
   if '/lp4st' in lowered:
      return'A Gaming laptopok között a 4K kijelző elég ritka ezért nem sok opció közül választhatunk.\n-Processzor: Az Intel Core i9 modellt érdemes választani vagy az AMD Ryzen 9-es modellt\n-Videókártya: Mindenképpen az Nvidia RTX 4080/4090 es modellek et érdemes választani\n-Memória: elengedhetetlen ilyen felbontás mellé a 32 GB DDR5\n-Kijelző: Érdemes magas képfrissítést választani pl.: 120Hz, 144Hz, 240Hz-et\n például:\n -MSI Raider GE68\n https://hu.msi.com/Laptop/Raider-GE68-HX-14VX\n -Acer Predator Helios 15\n https://www.acer.com/hu-hu/predator/laptops/helios/helios-3d-15-spatiallabs-edition\n -ASUS ROG Zephyrus G16\n https://rog.asus.com/laptops/rog-zephyrus/rog-zephyrus-g16-2024/\nHasznos oldal lehet még számodra a következő FPS kalkulátor weboldal:\n https://pc-builds.com/fps-calculator/'
   ########################
   

   #mindekttő laptop ajánlások
   if '/lp1080mid' in lowered:
      return'-Processzor: Intel core i7-13700HX vagy AMD Ryzen 5 7535HS\n-Videókártya: Nvidia RTX 4070//4080\n-Memória 16/32 GB DDR5\n-Tárhely: 1 TB\n-Kijelző: tetszőleges képfrissítés ajánlom a magasabb pl.: 120Hz, 144Hz, 240Hz-et\nPéldáúl:\n -Az ASUS Tuf Gaming laptopok\n https://www.asus.com/hu/laptops/for-gaming/all-series/filter?Series=TUF-Gaming\n -Lenovo Legion 5 laptopok\n https://www.lenovo.com/hu/hu/laptops/legion-laptops/legion-5-series/c/legion-5-series\nHasznos oldal lehet még számodra a következő FPS kalkulátor weboldal:\n https://pc-builds.com/fps-calculator/'
   if '/lp1440mid' in lowered:
      return'-Processzor: Intel core i9-14900HX vagy AMD Ryzen 9 7945HX\n-Videókártya: Nvidia RTX 4070/4080 vagy ezek Ti változatai\n-Memória 32 GB DDR5\n-Tárhely: 1 TB\n-Kijelző: tetszőleges képfrissítés ajánlom a magasabb pl.: 120Hz vagy a 144Hz-et\nPéldáúl:\n -Az Alienware x15 \n -Lenovo Legion pro 7 laptopok\n https://www.lenovo.com/hu/hu/laptops/legion-laptops/legion-pro-series/Legion-Pro-7i-Gen-8-16-inch-Intel/p/LEN101G0023\n -Az ASUS TUF Gaming A15\n https://www.asus.com/hu/laptops/for-gaming/tuf-gaming/asus-tuf-gaming-a15-2024/\n -ASUS ROG Zephyrus G16\n https://rog.asus.com/hu/laptops/rog-zephyrus/rog-zephyrus-g16-2024/\nHasznos oldal lehet még számodra a következő FPS kalkulátor weboldal:\n https://pc-builds.com/fps-calculator/'
   if '/lp4mid' in lowered:
      return'A Gaming laptopok között a 4K kijelző elég ritka ezért nem sok opció közül választhatunk.\n-Processzor: Az Intel Core i9 modellt érdemes választani vagy az AMD Ryzen 9-es modellt\n-Videókártya: Mindenképpen az Nvidia RTX 4080/4090 es modellek et érdemes választani\n-Memória: elengedhetetlen ilyen felbontás mellé a 32 GB DDR5\n-Kijelző: Érdemes magas képfrissítést választani pl.: 120Hz, 144Hz, 240Hz-et\n például:\n -MSI Raider GE68\n https://hu.msi.com/Laptop/Raider-GE68-HX-14VX\n -Acer Predator Helios 15\n https://www.acer.com/hu-hu/predator/laptops/helios/helios-3d-15-spatiallabs-edition\n -ASUS ROG Zephyrus G16\n https://rog.asus.com/laptops/rog-zephyrus/rog-zephyrus-g16-2024/'
   ########################


   ###############################################################################################################################################################################################################################################################################################################################################################################################################################
   
   
   #asztali pc felbontás választás
   if '!asztali' in lowered:
      return 'Fontos megtudni milyen felbontáson szeretnél játszani:\n -1080p: !pc1080\n -1440p: !pc1440\n -4k: !pc4k\nAz így kapott asztali konfigurációk mindig közepestől egészen a maximális grafikai beállításokat célozzák meg.'
   

   #pc felbontások.
   if '!pc1080' in lowered:
      return 'A 1080p-t választottad. Fontos még hogy milyen típusú játékokkal szeretnél játszani?\n -Ha csak fps úgynevezett E-sport játékokkal fogsz játszani akkor: /pc1080fps\n -Ha sztori játékokkal játszanál leginkább akkor: /pc1080st\n -Ha a kettő közötti arany középutat céloznád meg akkor pedig: /pc1080mid'
   if '!pc1440' in lowered:
      return 'A 1440p-t választottad. Fontos még hogy milyen típusú játékokkal szeretnél játszani?\n -Ha csak fps úgynevezett E-sport játékokkal fogsz játszani akkor: /pc1440fps\n -Ha sztori játékokkal játszanál leginkább akkor: /pc1440st\n -Ha a kettő közötti arany középutat céloznád meg akkor pedig: /pc1440mid'
   if '!pc4k' in lowered:
      return 'A 4k-t választottad. Fontos még hogy milyen típusú játékokkal szeretnél játszani?\n -Ha csak fps úgynevezett E-sport játékokkal fogsz játszani akkor: /pc4fps\n -Ha sztori játékokkal játszanál leginkább akkor: /pc4st\n -Ha a kettő közötti arany középutat céloznád meg akkor pedig: /pc4mid'
   
   


   #pc ajánlások
   #fps pc ajánlások
   if '/pc1080fps' in lowered:
      return'-Processzor: Intel: Core i5-12400f vagy AMD: Ryzen 5 5600x\n-Alternatíva: Intel Core i5-13400F vagy AMD Ryzen 7 5700X (jobb teljesítmény, de drágább)\n-Videókártya: Nvidia: Geforce GTX 1660 Super AMD: Radeon 6650 XT\n-Alternatíva: Nvidia GeForce RTX 3060/4060 vagy AMD Radeon 6775 XT (jobb teljesítmény, de drágább)\n-Memória: 16 GB DDR4-3200 MHz\n-Tárhely: 1TB SSD\n-Alaplap: Intel processzorhoz: B660/B760 chipsetes AMD processzorhoz: B550 chipsetes\n-Tápegység: 600W 80+gold minősítésű tápegység\n-Jól szellőző ház\n Egyébb információk:\n -Ez a konfiguráció 1080p felbontáson közepes grafikai beállításokkal képes futtatni a legtöbb e-sport címet magas FPS számmal (Ha a drágább processzor és videókártyát választod akkor magas beállításokat is tudsz használni).\n -Fontos, hogy a konfiguráció összeállításakor kompatibilis alkatrészeket válasszunk.\n-Hasznos linkek lehetnek számodra: \n -https://www.pcx.hu/geposszerako\n -https://pc-builds.com/hu/compare/gpu/\n -https://www.price2performance.com/hu/processzorok/\n -https://gepigeny.hu/jatekok'
   
   if '/pc1440fps' in lowered:
      return'-Processzor: Intel: Core i5-14600k vagy AMD: Ryzen 5 7600x\n-Alternatíva: Intel Core i7-14700k vagy AMD Ryzen 7 7800X3D (jobb teljesítmény, de drágább)\n-Videókártya: Nvidia: Geforce RTX 4060/4060 Ti AMD: Radeon RX 7600 XT\n-Alternatíva: Nvidia GeForce RTX 4070/4070 Ti/4070 super vagy AMD Radeon RX 7700/7800 XT (jobb teljesítmény, de drágább)\n-Memória: 16 GB DDR4-3600/ DDR5-5000-6000 MHz\n-Tárhely: 1TB SSD\n-Alaplap: Intel processzorhoz: B660/B760 chipsetes AMD processzorhoz: B650 chipsetes(Viszont ide már DDR5 memóriát kell választani)\n-Tápegység: 750W-850W 80+gold minősítésű tápegység\n-Jól szellőző ház\n Egyébb információk:\n -Ez a konfiguráció 1440p felbontáson közepes grafikai beállításokkal képes futtatni a legtöbb e-sport címet magas FPS számmal (Ha a drágább processzor és videókártyát választod akkor magas beállításokat is tudsz használni).\n -Fontos, hogy a konfiguráció összeállításakor kompatibilis alkatrészeket válasszunk.\n-Hasznos linkek lehetnek számodra: \n -https://www.pcx.hu/geposszerako\n -https://pc-builds.com/hu/compare/gpu/\n -https://www.price2performance.com/hu/processzorok/\n --https://gepigeny.hu/jatekok'
   
   if '/pc4fps' in lowered:
      return'-Processzor: Intel: Core i7-14700K vagy AMD: Ryzen 7 7800X3D\n-Alternatíva: Intel Core i9-14900k vagy AMD Ryzen 9 7900X3D (jobb teljesítmény, de drágább)\n-Videókártya: Nvidia: Geforce RTX 4070 Ti SUPER/4080 AMD: Radeon RX 7800 XT\n-Alternatíva: Nvidia GeForce RTX 4080 SUPER vagy AMD Radeon RX 7900 XTX (jobb teljesítmény, de drágább)\n-Memória: 32 GB DDR4-3600/ DDR5-5000-6000 MHz\n-Tárhely: 1TB SSD\n-Alaplap: Intel processzorhoz: Z790 chipsetes AMD processzorhoz: X670 chipsetes\n-Tápegység: 850W-1000W 80+gold minősítésű tápegység\n-Jól szellőző ház\n Egyébb információk:\n -Ez a konfiguráció 4K felbontáson közepes grafikai beállításokkal képes futtatni a legtöbb e-sport címet (Ha a drágább processzor és videókártyát választod akkor magas beállításokat is tudsz használni).\n -Fontos, hogy a konfiguráció összeállításakor kompatibilis alkatrészeket válasszunk.\n-Hasznos linkek lehetnek számodra: \n -https://www.pcx.hu/geposszerako\n -https://pc-builds.com/hu/compare/gpu/\n -https://www.price2performance.com/hu/processzorok/'
   ##########################   

   
   
   #sztori pc ajánlások
   if '/pc1080st' in lowered:
      return'-Processzor: Intel: Core i5-14600k vagy AMD: Ryzen 5 7600X\n-Alternatíva: Intel Core i7-14700k vagy AMD Ryzen 7 7800X3D (jobb teljesítmény, de drágább)\n-Videókártya: Nvidia: Geforce RTX 4060/4060 Ti AMD: Radeon RX 7600 XT\n-Alternatíva: Nvidia GeForce RTX 4070/4070 Ti/4070 super vagy AMD Radeon RX 7700/7800 XT (jobb teljesítmény, de drágább)\n-Memória: 16/32 GB DDR5-5000-6000 MHz\n-Tárhely: 1TB SSD\n-Alaplap: Intel processzorhoz: B660/B760 chipsetes AMD processzorhoz: B650 chipsetes\n-Tápegység: 750W-850W 80+gold minősítésű tápegység\n-Jól szellőző ház\n Egyébb információk:\n -Ez a konfiguráció 1080p felbontáson majdnem maximális grafikai beállításokkal képes futtatni a legtöbb sztori játék címet magas FPS számmal (Ha a drágább processzor és videókártyát választod akkor maximum beállításokat is tudsz használni).\n -Fontos, hogy a konfiguráció összeállításakor kompatibilis alkatrészeket válasszunk.\n-Hasznos linkek lehetnek számodra: \n -https://www.pcx.hu/geposszerako\n -https://pc-builds.com/hu/compare/gpu/\n -https://www.price2performance.com/hu/processzorok/\n -https://gepigeny.hu/jatekok'
   
   if '/pc1440st' in lowered:
      return'-Processzor: Intel: Core i5-14600k vagy AMD: Ryzen 5 7600X\n-Alternatíva: Intel Core i7-14700k vagy AMD Ryzen 7 7800X3D (jobb teljesítmény, de drágább)\n-Videókártya: Nvidia: Geforce RTX 4070/ 4070 Ti AMD: Radeon RX 7600 XT\n-Alternatíva: Nvidia GeForce RTX 4070 SUPER/4070 Ti super vagy AMD Radeon RX 7700/7800 XT (jobb teljesítmény, de drágább)\n-Memória: 32 GB DDR5-5000-6000 MHz\n-Tárhely: 1TB SSD\n-Alaplap: Intel processzorhoz: B660/B760 chipsetes AMD processzorhoz: B650 chipsetes\n-Tápegység: 850W 80+gold minősítésű tápegység\n-Jól szellőző ház\n Egyébb információk:\n -Ez a konfiguráció 1440p felbontáson majdnem maximális grafikai beállításokkal képes futtatni a legtöbb sztori játék címet magas FPS számmal (Ha a drágább processzor és videókártyát választod akkor maximális beállításokat is tudsz használni).\n -Fontos, hogy a konfiguráció összeállításakor kompatibilis alkatrészeket válasszunk.\n-Hasznos linkek lehetnek számodra: \n -https://www.pcx.hu/geposszerako\n -https://pc-builds.com/hu/compare/gpu/\n -https://www.price2performance.com/hu/processzorok/\n -https://gepigeny.hu/jatekok'
   
   if '/pc4st' in lowered:
      return'-Processzor: Intel: Core i7-14700K vagy AMD: Ryzen 7 7800X3D\n-Alternatíva: Intel Core i9-14900k vagy AMD Ryzen 9 7900X3D (jobb teljesítmény, de drágább)\n-Videókártya: Nvidia: Geforce RTX 4080/4080 SUPER AMD: Radeon RX 7800 XT\n-Alternatíva: Nvidia GeForce RTX 4090 vagy AMD Radeon RX 7900 XTX (jobb teljesítmény, de drágább)\n-Memória: 32/64 GB DDR5-5000-7200 MHz\n-Tárhely: 1TB SSD\n-Alaplap: Intel processzorhoz: Z790 chipsetes AMD processzorhoz: X670 chipsetes\n-Tápegység: 850W-1000W 80+gold minősítésű tápegység\n-Jól szellőző ház\n Egyébb információk:\n -Ez a konfiguráció 4K felbontáson közel maximális grafikai beállításokkal képes futtatni a legtöbb sztori játék címet (Ha a drágább processzor és videókártyát választod akkor maximális beállításokat is tudsz használni).\n -Fontos, hogy a konfiguráció összeállításakor kompatibilis alkatrészeket válasszunk.\n-Hasznos linkek lehetnek számodra: \n -https://www.pcx.hu/geposszerako\n -https://pc-builds.com/hu/compare/gpu/\n -https://www.price2performance.com/hu/processzorok/\n -https://gepigeny.hu/jatekok'
   ######################




   #mindkettő pc ajánlások
   if '/pc1080mid' in lowered:
      return'-Processzor: Intel: Core i5-14600k vagy AMD: Ryzen 5 7600X\n-Alternatíva: Intel Core i7-14700k vagy AMD Ryzen 7 7800X3D (jobb teljesítmény, de drágább)\n-Videókártya: Nvidia: Geforce RTX 4060/4060 Ti AMD: Radeon RX 7600 XT\n-Alternatíva: Nvidia GeForce RTX 4070 vagy AMD Radeon RX 7700XT (jobb teljesítmény, de drágább)\n-Memória: 16/32 GB DDR5-5000-6000 MHz\n-Tárhely: 1TB SSD\n-Alaplap: Intel processzorhoz: B660/B760 chipsetes AMD processzorhoz: B650 chipsetes\n-Tápegység: 750W-850W 80+gold minősítésű tápegység\n-Jól szellőző ház\n Egyébb információk:\n -Ez a konfiguráció 1080p felbontáson közepes és magas grafikai beállításokkal képes futtatni a legtöbb játékot magas FPS számmal (Ha a drágább processzor és videókártyát választod akkor maximum beállításokat is tudsz használni).\n -Fontos, hogy a konfiguráció összeállításakor kompatibilis alkatrészeket válasszunk.\n-Hasznos linkek lehetnek számodra: \n -https://www.pcx.hu/geposszerako\n -https://pc-builds.com/hu/compare/gpu/\n -https://www.price2performance.com/hu/processzorok/\n -https://gepigeny.hu/jatekok'
   
   if '/pc1440mid' in lowered:
      return'-Processzor: Intel: Core i5-14600k vagy AMD: Ryzen 5 7600X\n-Alternatíva: Intel Core i7-14700k vagy AMD Ryzen 7 7800X3D (jobb teljesítmény, de drágább)\n-Videókártya: Nvidia: Geforce RTX 4070/4070 Ti AMD: Radeon RX 7600 XT\n-Alternatíva: Nvidia GeForce RTX 4070 SUPER/4070 Ti SUPER vagy AMD Radeon RX 7700/7800XT (jobb teljesítmény, de drágább)\n-Memória: 32 GB DDR5-5000-6000 MHz\n-Tárhely: 1TB SSD\n-Alaplap: Intel processzorhoz: B660/B760 chipsetes AMD processzorhoz: B650 chipsetes\n-Tápegység: 850W 80+gold minősítésű tápegység\n-Jól szellőző ház\n Egyébb információk:\n -Ez a konfiguráció 1440p felbontáson közepes és magas grafikai beállításokkal képes futtatni a legtöbb játékot magas FPS számmal (Ha a drágább processzor és videókártyát választod akkor maximum beállításokat is tudsz használni).\n -Fontos, hogy a konfiguráció összeállításakor kompatibilis alkatrészeket válasszunk.\n-Hasznos linkek lehetnek számodra: \n -https://www.pcx.hu/geposszerako\n -https://pc-builds.com/hu/compare/gpu/\n -https://www.price2performance.com/hu/processzorok/\n -https://gepigeny.hu/jatekok'
   
   if '/pc4mid' in lowered:
      return'-Processzor: Intel: Core i7-14700K vagy AMD: Ryzen 7 7800X3D\n-Alternatíva: Intel Core i9-14900k vagy AMD Ryzen 9 7900X3D (jobb teljesítmény, de drágább)\n-Videókártya: Nvidia: Geforce RTX 4080/4080 SUPER AMD: Radeon RX 7800 XT\n-Alternatíva: Nvidia GeForce RTX 4090 vagy AMD Radeon RX 7900 XTX (jobb teljesítmény, de drágább)\n-Memória: 32/64 GB DDR5-5000-7200 MHz\n-Tárhely: 1TB SSD\n-Alaplap: Intel processzorhoz: Z790 chipsetes AMD processzorhoz: X670 chipsetes\n-Tápegység: 850W-1000W 80+gold minősítésű tápegység\n-Jól szellőző ház\n Egyébb információk:\n -Ez a konfiguráció 4K felbontáson közel maximális grafikai beállításokkal képes futtatni a legtöbb sztori játék címet (Ha a drágább processzor és videókártyát választod akkor maximális beállításokat is tudsz használni).\n -Fontos, hogy a konfiguráció összeállításakor kompatibilis alkatrészeket válasszunk.\n-Hasznos linkek lehetnek számodra: \n -https://www.pcx.hu/geposszerako\n -https://pc-builds.com/hu/compare/gpu/\n -https://www.price2performance.com/hu/processzorok/\n -https://gepigeny.hu/jatekok'
   #######################

   else:
      return'Szia ezt a parancsot nem értem kérlek használd !kezdjunk parancsot. :)'