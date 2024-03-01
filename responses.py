from random import choice, randint

def get_responses (user_input: str) -> str:
   lowered: str = user_input.lower()

   
   if 'szia' in lowered or 'hello' in lowered:
      return 'Szia ha szeretnéd elkezdeni a gamer Pc-d kiválasztását akkor a !kezdjunk parancs segítségevel elkezdheted a konfigurációt.'
   
   if '!kezdjunk' in lowered:
      return 'Elősször az alábbi lehetőségek közül válassz!\n -Laptopot szeretnék: !laptop\n -Asztali számítógépet szeretnék: !asztali\nVagy ha ár sávok alapján szeretnél választani akkor a !arak'


   if '!arak' in lowered:
      return''


   #laptop felbontás választása
   if '!laptop' in lowered:
      return 'Fontos megtudni milyen felbontáson szeretnél játszani:\n -1080p: !lp1080\n -1440p: !lp1440\n -4k: !lp4\nAz így kapott laptop konfigurációk mindig a maximális grafikai beállításokat célozzák meg.'
   

   #laptop felbontásokhoz a játékok típusa
   if '!lp1080' in lowered:
      return 'A 1080p-t választottad. Fontos még hogy milyen típusú játékokkal szeretnél játszani?\n -Ha csak fps úgynevezett E-sport játékokkal fogsz játszani akkor: /lp1080fps\n -Ha sztori játékokkal játszanál leginkább akkor: /lp1080st\n -Ha a kettő közötti arany középutat céloznád meg akkor pedig: !lp1080mid'
   if '!lp1440' in lowered:
      return 'A 1440p-t választottad. Fontos még hogy milyen típusú játékokkal szeretnél játszani?\n -Ha csak fps úgynevezett E-sport játékokkal fogsz játszani akkor: /lp1440fps\n -Ha sztori játékokkal játszanál leginkább akkor: /lp1440st\n -Ha a kettő közötti arany középutat céloznád meg akkor pedig: !lp1440mid'
   if '!lp4k' in lowered:
      return 'A 4k-t választottad. Fontos még hogy milyen típusú játékokkal szeretnél játszani?\n -Ha csak fps úgynevezett E-sport játékokkal fogsz játszani akkor: /lp4fps\n -Ha sztori játékokkal játszanál leginkább akkor: /lp4st\n -Ha a kettő közötti arany középutat céloznád meg akkor pedig: !lp4mid'
  
  


   #laptop ajánlások
   #fps laptop ajánlások
   if '/lp1080fps' in lowered:
      return'-Processzor: Intel core i5-13500H vagy AMD Ryzen 5 7535HS\n-Videókártya: Nvidia RTX 4050\n-Memória 16 GB DDR4\n-Tárhely: 512 GB/1 TB\n-Kijelző: tetszőleges képfrissítés ajánlom a magasabb pl.: 120Hz, 144Hz, 240Hz-et\nPéldáúl:\n -A Lenovo LOQ laptopjai\n https://www.lenovo.com/hu/hu/laptops/laptops-loq/lenovo-loq-laptops/c/loq-laptops\n -Az Acer Nitro laptopjai\n https://www.acer.com/hu-hu/laptops/nitro\n -A Dell G15-ös laptopjai\n https://www.dell.com/en-us/shop/gaming-laptops/g15-gaming-laptop/spd/g-series-15-5530-laptop\n -Asus TUF Gaming laptopok\n https://www.asus.com/hu/laptops/for-gaming/all-series/filter?Series=TUF-Gaming\nHasznos oldal lehet még számodra a következő FPS kalkulátor weboldal:\n https://pc-builds.com/fps-calculator/'
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
   if '/pc1080mid' in lowered:
      return'-Processzor: Intel core i7-13700HX vagy AMD Ryzen 5 7535HS\n-Videókártya: Nvidia RTX 4070//4080\n-Memória 16/32 GB DDR5\n-Tárhely: 1 TB\n-Kijelző: tetszőleges képfrissítés ajánlom a magasabb pl.: 120Hz, 144Hz, 240Hz-et\nPéldáúl:\n -Az ASUS Tuf Gaming laptopok\n https://www.asus.com/hu/laptops/for-gaming/all-series/filter?Series=TUF-Gaming\n -Lenovo Legion 5 laptopok\n https://www.lenovo.com/hu/hu/laptops/legion-laptops/legion-5-series/c/legion-5-series\nHasznos oldal lehet még számodra a következő FPS kalkulátor weboldal:\n https://pc-builds.com/fps-calculator/'
   if '/pc1440mid' in lowered:
      return'-Processzor: Intel core i9-14900HX vagy AMD Ryzen 9 7945HX\n-Videókártya: Nvidia RTX 4070/4080 vagy ezek Ti változatai\n-Memória 32 GB DDR5\n-Tárhely: 1 TB\n-Kijelző: tetszőleges képfrissítés ajánlom a magasabb pl.: 120Hz vagy a 144Hz-et\nPéldáúl:\n -Az Alienware x15 \n -Lenovo Legion pro 7 laptopok\n https://www.lenovo.com/hu/hu/laptops/legion-laptops/legion-pro-series/Legion-Pro-7i-Gen-8-16-inch-Intel/p/LEN101G0023\n -Az ASUS TUF Gaming A15\n https://www.asus.com/hu/laptops/for-gaming/tuf-gaming/asus-tuf-gaming-a15-2024/\n -ASUS ROG Zephyrus G16\n https://rog.asus.com/hu/laptops/rog-zephyrus/rog-zephyrus-g16-2024/\nHasznos oldal lehet még számodra a következő FPS kalkulátor weboldal:\n https://pc-builds.com/fps-calculator/'
   if '/pc4mid' in lowered:
      return'A Gaming laptopok között a 4K kijelző elég ritka ezért nem sok opció közül választhatunk.\n-Processzor: Az Intel Core i9 modellt érdemes választani vagy az AMD Ryzen 9-es modellt\n-Videókártya: Mindenképpen az Nvidia RTX 4080/4090 es modellek et érdemes választani\n-Memória: elengedhetetlen ilyen felbontás mellé a 32 GB DDR5\n-Kijelző: Érdemes magas képfrissítést választani pl.: 120Hz, 144Hz, 240Hz-et\n például:\n -MSI Raider GE68\n https://hu.msi.com/Laptop/Raider-GE68-HX-14VX\n -Acer Predator Helios 15\n https://www.acer.com/hu-hu/predator/laptops/helios/helios-3d-15-spatiallabs-edition\n -ASUS ROG Zephyrus G16\n https://rog.asus.com/laptops/rog-zephyrus/rog-zephyrus-g16-2024/'
   ########################


   ###############################################################################################################################################################################################################################################################################################################################################################################################################################
   
   
   #asztali pc felbontás választás
   if '!asztali' in lowered:
      return 'Fontos megtudni milyen felbontáson szeretnél játszani:\n -1080p: !pc1080\n -1440p: !pc1440\n -4k: !pc4k\nAz így kapott asztali konfigurációk mindig a maximális grafikai beállításokat célozzák meg.'
   

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
      return'-Processzor: Intel: Core i3-12100f vagy AMD: Ryzen 3 3300x\n-Alternatíva: Intel Core i5-12400F vagy AMD Ryzen 5 5600X (jobb teljesítmény, de drágább)\n-Videókártya: Nvidia: Geforce GTX 1660 Super AMD: Radeon RX 5600 XT\n-Alternatíva: Nvidia GeForce RTX 3060 vagy AMD Radeon RX 6600 XT (jobb teljesítmény, de drágább)\n-Memória: 16 GB DDR4-3200 MHz\n-Tárhely: 1TB SSD\n-Alaplap: Intel processzorhoz: B660 chipsetes AMD processzorhoz: B550 chipsetes\n-Tápegység: 600W 80+gold minősítésű tápegység\n-Jól szellőző ház\n Egyébb információk:\n -Ez a konfiguráció 1080p felbontáson közepes grafikai beállításokkal képes futtatni a legtöbb e-sport címet (Ha a drágább processzor és videókártyát választod akkor maxas beállításokat is tudsz használni).\n -Fontos, hogy a konfiguráció összeállításakor kompatibilis alkatrészeket válasszunk.\n-Hasznos linkek lehetnek számodra: \n -https://www.pcx.hu/geposszerako\n -https://pc-builds.com/hu/compare/gpu/\n -https://www.price2performance.com/hu/processzorok/'
   
   if '/pc1440fps' in lowered:
      return'-Processzor: Intel: Core i5-12400f vagy AMD: Ryzen 5 5600x\n-Alternatíva: Intel Core i7-12700F vagy AMD Ryzen 7 5800X (jobb teljesítmény, de drágább)\n-Videókártya: Nvidia: Geforce RTX 3060 Ti AMD: Radeon RX 6700 XT\n-Alternatíva: Nvidia GeForce RTX 3070 Ti vagy AMD Radeon RX 6800 XT (jobb teljesítmény, de drágább)\n-Memória: 16 GB DDR4-3600 MHz\n-Tárhely: 1TB SSD\n-Alaplap: Intel processzorhoz: B660 chipsetes AMD processzorhoz: B550 chipsetes\n-Tápegység: 700W 80+gold minősítésű tápegység\n-Jól szellőző ház\n Egyébb információk:\n -Ez a konfiguráció 1440p felbontáson közepes grafikai beállításokkal képes futtatni a legtöbb e-sport címet (Ha a drágább processzor és videókártyát választod akkor maxas beállításokat is tudsz használni).\n -Fontos, hogy a konfiguráció összeállításakor kompatibilis alkatrészeket válasszunk.\n-Hasznos linkek lehetnek számodra: \n -https://www.pcx.hu/geposszerako\n -https://pc-builds.com/hu/compare/gpu/\n -https://www.price2performance.com/hu/processzorok/'
   
   if '/pc4fps' in lowered:
      return'-Processzor: Intel: Core i7-12700f vagy AMD: Ryzen 7 5800x\n-Alternatíva: Intel Core i9-12900k vagy AMD Ryzen 9 5900X (jobb teljesítmény, de drágább)\n-Videókártya: Nvidia: Geforce RTX 3080 Ti AMD: Radeon RX 6900 XT\n-Alternatíva: Nvidia GeForce RTX 3090 Ti vagy AMD Radeon RX 6950 XT (jobb teljesítmény, de drágább)\n-Memória: 32 GB DDR4-3600 MHz\n-Tárhely: 1TB SSD\n-Alaplap: Intel processzorhoz: Z690 chipsetes AMD processzorhoz: X570 chipsetes\n-Tápegység: 850W 80+gold minősítésű tápegység\n-Jól szellőző ház\n Egyébb információk:\n -Ez a konfiguráció 4K felbontáson közepes grafikai beállításokkal képes futtatni a legtöbb e-sport címet (Ha a drágább processzor és videókártyát választod akkor maxas beállításokat is tudsz használni).\n -Fontos, hogy a konfiguráció összeállításakor kompatibilis alkatrészeket válasszunk.\n-Hasznos linkek lehetnek számodra: \n -https://www.pcx.hu/geposszerako\n -https://pc-builds.com/hu/compare/gpu/\n -https://www.price2performance.com/hu/processzorok/'
   ##########################   

   
   
   #sztori pc ajánlások
   if '/pc1080st' in lowered:
      return'-Processzor: Intel: Core i5-13400f vagy AMD: Ryzen 5 7600x\n-Alternatíva: Intel Core i7-13700k vagy AMD Ryzen 7 7700X (jobb teljesítmény, de drágább)\n-Videókártya: Nvidia: Geforce RTX 3060 AMD: Radeon RX 6600 XT\n-Alternatíva: Nvidia GeForce RTX 4060 Ti vagy AMD Radeon RX 6800 XT (jobb teljesítmény, de drágább)\n-Memória: 16 GB DDR4-3600 MHz\n-Tárhely: 1TB SSD\n-Alaplap: Intel processzorhoz: B660 chipsetes AMD processzorhoz: B550 chipsetes\n-Tápegység: 700W 80+gold minősítésű tápegység\n-Jól szellőző ház\n Egyébb információk:\n -Ez a konfiguráció 1080p felbontáson közepes grafikai beállításokkal képes futtatni a legtöbb sztori címet (Ha a drágább processzor és videókártyát választod akkor maxas beállításokat is tudsz használni).\n -Fontos, hogy a konfiguráció összeállításakor kompatibilis alkatrészeket válasszunk.\n-Hasznos linkek lehetnek számodra: \n -https://www.pcx.hu/geposszerako\n -https://pc-builds.com/hu/compare/gpu/\n -https://www.price2performance.com/hu/processzorok/'
   
   if '/pc1440st' in lowered:
      return'Királyság5'
   
   if '/pc4st' in lowered:
      return'Királyság6'
   ######################




   #mindkettő pc ajánlások
   if '/pc1080mid' in lowered:
      return'Királyság4'
   if '/pc1440mid' in lowered:
      return'Királyság5'
   if '/pc4mid' in lowered:
      return'Királyság6'
   #######################
