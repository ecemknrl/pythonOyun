import random,time
class oyuncu():
    def __init__(self,account,money,playerLevel,xp):
        self.account=account
        self.money=money
        self.playerLevel=playerLevel
        self.xp=xp
    def oyuncuBilgiGoster(self):
        print("""
\tplayer
account: {}\tmoney: {}        
player level: {}
xp: {}
        """.format(self.account,self.money,self.playerLevel,self.xp))

class oyunKarakteri(oyuncu):
    def __init__(self,account,money,playerLevel,xp,name,power,level):
        super().__init__(account,money,playerLevel,xp)
        self.name = name
        self.power = power
        self.level = level

    def bilgileri_goster(self):
        print("""
\tGame character
name: {}\t power: {}
level: {}       
            """.format(self.name, self.power, self.level))

    def gucArttir(self, money, level, xp):
        if (level <= 10):
            print("oyuncunun gücünü arttırmak için '+' tuşunu kullanınız..\nGüç arttırmayı bitirmek için enter'ı tuşlayınız..")
            print("NOT: her arttırma, oyun karakterine +10 güç ekler")
            while (1):
                while (1):
                    artiTusla = input("\n'+' ya da enter ")
                    if (artiTusla == "+"):
                        if (money >= 100):
                            print("$-100")
                            money -= 100
                            self.power += 10
                            self.level += 1
                            xp += 100
                            print("$=", money)
                            print("lvl= ", self.level,end="\t")
                            print(" xp= ", xp)
                            print("güç= ", self.power,end="\t")
                            print("player lvl: ",level )
                        else:
                            print("bunun için yeterli paranız yoktur..")
                            self.savasAcma(money, level, xp)
                            break
                    elif (not artiTusla):
                        print("\n\toyun karakteri: {}\t\t".format(self.name))
                        print("$=", money)
                        print("lvl= ", self.level, end="\t")
                        print(" xp= ", xp)
                        print("güç= ", self.power, end="\t")
                        print("player lvl: ", level)
                        self.savasAcma(money, level, xp)
                        break
                    if (xp >= 1000):
                        xp=0
                        level += 1
                        print("\t\tTEBRİKLER {} level oldunuz!!!".format(level))
                        continue
                    continue
                break
        elif (level >= 10 and level <= 30):
            print("oyuncunun gücünü arttırmak için '+' tuşunu kullanınız..")
            print("NOT: her arttırma, oyun karakterine +20 güç ekler")
            while (1):
                while (1):
                    artiTusla = input("\n'+' ya da enter ")
                    if (artiTusla == "+"):
                        if (money >= 200):
                            print("$-200")
                            money -= 200
                            self.power += 20
                            self.level += 1
                            xp += 80
                            print("$=", money)
                            print("lvl= ", self.level, end="\t")
                            print(" xp= ", xp)
                            print("güç= ", self.power, end="\t")
                            print("player lvl: ", level)
                        else:
                            print("bunun için yeterli miktarda paranız kalmamıştır..")
                            self.savasAcma(money, level, xp)
                            break
                    elif (not artiTusla):
                        print("\n\toyun karakteri: {}\t\t".format(self.name))
                        print("$=", money)
                        print("lvl= ", self.level, end="\t")
                        print(" xp= ", xp)
                        print("güç= ", self.power, end="\t")
                        print("player lvl: ", level)
                        self.savasAcma(money,level,xp)
                        break
                    if (xp >= 1000):
                        xp=0
                        level += 1
                        print("\t\tTEBRİKLER {} level oldunuz!!!".format(level))
                        continue
                    continue
                break
        elif (level >= 30 and level <= 40):
            print("oyuncunun gücünü arttırmak için '+' tuşunu kullanınız..")
            print("NOT: her arttırma, oyun karakterine +30 güç ekler")
            while (1):
                while (1):
                    artiTusla = input("\n'+' ya da enter ")
                    if (artiTusla == "+"):
                        if (money >= 300):
                            print("$-300")
                            money -= 300
                            self.power += 30
                            self.level += 1
                            xp += 60
                            print("$=", money)
                            print("lvl= ", self.level, end="\t")
                            print(" xp= ", xp)
                            print("güç= ", self.power, end="\t")
                            print("player lvl: ", level)
                        else:
                            print("bunun için yeterli miktarda paranız kalmamıştır..")
                            self.savasAcma(money, level, xp)
                            break
                    elif (not artiTusla):
                        print("\n\toyun karakteri: {}\t\t".format(self.name))
                        print("$=", money)
                        print("lvl= ", self.level, end="\t")
                        print(" xp= ", xp)
                        print("güç= ", self.power, end="\t")
                        print("player lvl: ", level)
                        self.savasAcma(money, level, xp)
                        break
                    if (xp >= 1000):
                        xp=0
                        level += 1
                        print("\t\tTEBRİKLER {} level oldunuz!!!".format(level))
                        continue
                    continue
                break

    def savasAcma(self, money, level, xp):
        while(1):
            print("""
1-) Savaş Açma
2-) Defans
3-) Oyuncu Güçlendirme Sayfasına git
4-) Oyundan Çıkma           
            """)
            print("lütfen istediğiniz tuşu tuşlayınız:")
            try:
                tus = int(input())
                if(tus==1):
                    print("savaş açılıyor..")
                    karsiTakimGuc=random.randrange(201)
                    if (self.power > karsiTakimGuc):
                        self.power-=10
                        xp+=600
                        money+=10000
                        if(xp>=1000):
                            money += 10000
                            self.level += 2
                            level+=1
                        else:
                            self.level+=2
                        print("TEBRİKLER SAVAŞI KAZANDINIZ..\n")
                        print("""
    KAZANDIKLARINIZ:
    +10000$
    LEVEL + 1
    XP + 600                    
                                            """)
                        print("\n\toyun karakteri: {}\t\t".format(self.name))
                        print("$=", money)
                        print("lvl= ", self.level, end="\t")
                        print(" xp= ", xp)
                        print("güç= ", self.power, end="\t")
                        print("player lvl: ", level)
                        continue
                    elif(self.power< karsiTakimGuc):
                        self.power -= 100
                        if(self.power<=0):
                            self.power=0
                        xp -= 100
                        if(xp<=0):
                            xp=0
                        money -= 9000
                        if(money<=0):
                            money=0
                        print("MAALESEF MAĞLUP OLDUNUZ..\n")
                        print("""
    KAYBETTİKLERİNİZ:
    -9000$
    XP - 100                      
                        """)
                        print("\n\toyun karakteri: {}\t\t".format(self.name))
                        print("$=", money)
                        print("lvl= ", self.level, end="\t")
                        print(" xp= ", xp)
                        print("güç= ", self.power, end="\t")
                        print("player lvl: ", level)
                        continue
                    else:
                        print("BERABERE!!\n")
                        print("""
    KAZANDIKLARINIZ:
    +1000$
    XP + 100                    
                        """)
                        self.power-=50
                        xp+=100
                        money+=1000
                        self.level+=1
                        if (xp >= 1000):
                            money += 10000
                            level += 1
                        continue
                elif(tus==2):
                    print("Takım gelen saldırılara karşı savunmaya geçiyor..")
                    karsiTakimSaldiriGuc=random.randrange(201)
                    if (self.power > karsiTakimSaldiriGuc):
                        self.power-=10
                        xp += 600
                        money += 10000
                        if (xp >= 1000):
                            money += 10000
                            self.level += 2
                            level += 1
                        else:
                            self.level += 2
                        print("TEBRİKLER SAVAŞI KAZANDINIZ..\n")
                        print("""
    KAZANDIKLARINIZ:
    +10000$
    LEVEL + 1
    XP + 600                    
                        """)
                        print("\n\toyun karakteri: {}\t\t".format(self.name))
                        print("$=", money)
                        print("lvl= ", self.level, end="\t")
                        print(" xp= ", xp)
                        print("güç= ", self.power, end="\t")
                        print("player lvl: ", level)
                        continue
                    elif (self.power < karsiTakimSaldiriGuc):
                        self.power -= 100
                        if (self.power <= 0):
                            self.power = 0
                        xp -= 100
                        if (xp <= 0):
                            xp = 0
                        money -= 9000
                        if (money <= 0):
                            money = 0
                        print("MAALESEF MAĞLUP OLDUNUZ..\n")
                        print("""
    KAYBETTİKLERİNİZ:
    -9000$
    XP - 100                    
                        """)
                        print("\n\toyun karakteri: {}\t\t".format(self.name))
                        print("$=", money)
                        print("lvl= ", self.level, end="\t")
                        print(" xp= ", xp)
                        print("güç= ", self.power, end="\t")
                        print("player lvl: ", level)
                        continue
                    else:
                        print("BERABERE!!\n")
                        print("""
    KAZANDIKLARINIZ:
    +1000$
    XP + 100                        
                        """)
                        self.power -= 50
                        xp += 100
                        money += 1000
                        self.level += 1
                        if (xp >= 1000):
                            money += 10000
                            level += 1
                        continue
                elif(tus==3):
                    self.gucArttir(money,level,xp)
                elif(tus==4):
                    print("\noyundan çıkıyorsunuz..Lütfen bekleyiniz..")
                    for i in range(3, 0, -1):
                        time.sleep(0.3)
                        print(i, end=" ")
                    print("...")
                    break
                else:
                    print("lütfen verilen tuşlardan birini seçiniz..")
                    continue
                break
            except:
                print("lütfen sayı giriniz...")

kullaniciListesi=[["ecemknrl","ecmmath3"],["ahmet","171717a"]]
while(1):
    tus = input("Kayit için 'K' veya 'k' tuşlayınız, Giriş için 'G' veya 'g' tuşlayınız..")
    if (tus == "k" or tus == "K"):
        print("\t\tKAYIT\t\t")
        while (True):
            while(1):
                kullaniciAdiOlusturma = input("lütfen kendinize bir kullanici adi belirleyiniz: ")
                if(kullaniciAdiOlusturma==kullaniciListesi[0][0]):
                    print("bu kullanıcı adı alınmıştır. Lütfen farklı bir kullanıcı adı deneyiniz..")
                    time.sleep(0.6)
                    print("\nbunlara bakabilirsiniz: ")
                    print("ecemknrl1212\necem_knrl\necem_knrl123")
                    print("\n")
                    continue
                elif(kullaniciAdiOlusturma==kullaniciListesi[1][0]):
                    print("bu kullanıcı adı alınmıştır. Lütfen farklı bir kullanıcı adı deneyiniz..")
                    time.sleep(0.6)
                    print("\nbunlara bakabilirsiniz: ")
                    print("ahmet12\nahmet_\nahmet34\nahmet5858")
                    print("\n")
                    continue
                else:
                    sifreOlusturma = input("lütfen şifrenizi belirleyiniz: ")
                    sifreKontrol = input("lütfen şifrenizi doğrulamak için bir daha giriniz: ")

                    if (sifreOlusturma == sifreKontrol):
                        kullaniciListesi.append([kullaniciAdiOlusturma, sifreOlusturma])
                        mailVer = input("lütfen size ulaşabileceğimiz bir eposta giriniz: ")
                        print("KAYIT ISLEMLERİNİZ TAMAMLANMIŞTIR.\nGiriş için başlangıç sayfasına yönlendiriliyorsunuz..")
                        time.sleep(0.8)
                        break
                    else:
                        print("sifreleriniz eşleşmemiştir lütfen tekrar deneyiniz..")
                        continue
            break

    elif (tus == "g" or tus == "G"):
        account = input("lütfen kullanıcı adınızı giriniz: ")
        password = input("şifreniz: ")
        if (account == kullaniciListesi[0][0]):
            if (password == kullaniciListesi[0][1]):
                print("HOŞGELDİNİZ {}".format(account))
                oyuncu1=oyuncu(account,random.randrange(10001),random.randrange(41),200)
                oyuncu1.oyuncuBilgiGoster()
                oyuncukarakter1=oyunKarakteri(oyuncu1.account,oyuncu1.money,oyuncu1.playerLevel,oyuncu1.xp,"sinyor",random.randrange(101),random.randrange(21))
                oyuncukarakter1.bilgileri_goster()
                oyuncukarakter1.gucArttir(oyuncu1.money,oyuncu1.playerLevel,oyuncu1.xp)
                break
            else:
                print("giriş bilgileriniz hatalıdır..")
                print("tekrar giriş yapmak için enter'ı tuşlayınız,siteden çıkmak için '.' tuşlayınız..")
                deneme = input()
                if (not deneme):
                    continue
                elif (deneme == "."):
                    print("oyundan çıkıyorsunuz..Lütfen bekleyiniz..")
                    for i in range(3, -1, -1):
                        time.sleep(0.3)
                        print(i, end="")
                        break
        elif (account == kullaniciListesi[1][0]):
            if (password == kullaniciListesi[1][1]):
                print("HOŞGELDİNİZ {}".format(account))
                oyuncu2 = oyuncu(account, random.randrange(10001),random.randrange(41),800)
                oyuncu2.oyuncuBilgiGoster()
                oyuncukarakter2 = oyunKarakteri(oyuncu2.account,oyuncu2.money,oyuncu2.playerLevel,oyuncu2.xp,"Live",random.randrange(101) , random.randrange(21))
                oyuncukarakter2.bilgileri_goster()
                oyuncukarakter2.gucArttir(oyuncu2.money,oyuncu2.playerLevel,oyuncu2.xp)
                break
            else:
                print("giriş bilgileriniz hatalıdır..")
                print("tekrar giriş yapmak için enter'ı tuşlayınız,siteden çıkmak için '.' tuşlayınız..")
                deneme = input()
                if (not deneme):
                    continue
                elif (deneme == "."):
                    print("oyundan çıkıyorsunuz..Lütfen bekleyiniz..")
                    for i in range(3, -1, -1):
                        time.sleep(0.3)
                        print(i, end=" ")
                    break
        else:
            if(len(kullaniciListesi)>2):
                if (account == kullaniciListesi[2][0]):
                    if (password == kullaniciListesi[2][1]):
                        print("HOŞGELDİNİZ {}".format(account))
                        oyuncu3 = oyuncu(account, 2000, 0, 0)
                        oyuncu3.oyuncuBilgiGoster()
                        oyuncukarakter3 = oyunKarakteri(oyuncu3.account, oyuncu3.money, oyuncu3.playerLevel, oyuncu3.xp,
                                                        "Kale Burcu", 0, 0)
                        oyuncukarakter3.bilgileri_goster()
                        oyuncukarakter3.gucArttir(oyuncu3.money, oyuncu3.playerLevel, oyuncu3.xp)
                        break
                    else:
                        print("giriş bilgileriniz hatalıdır..")
                        print("tekrar giriş yapmak için enter'ı tuşlayınız,siteden çıkmak için '.' tuşlayınız..")
                        deneme = input()
                        if (not deneme):
                            continue
                        elif (deneme == "."):
                            print("oyundan çıkıyorsunuz..Lütfen bekleyiniz..")
                            for i in range(3, 0, -1):
                                time.sleep(0.3)
                                print(i, end="")
                            break
            else:
                print("böyle bir kullanıcı yoktur..")
                print("tekrar giriş yapmak için enter'ı tuşlayınız,siteden çıkmak için '.' tuşlayınız..")
                deneme = input()
                if(not deneme):
                    continue
                elif(deneme == "."):
                    print("oyundan çıkıyorsunuz..Lütfen bekleyiniz..")
                    for i in range(3, 0, -1):
                        time.sleep(0.3)
                        print(i, end=" ")
                    print("...")
                    break
                else:
                    print("lütfen enter ya da '.' tuşlayınız..")
                    continue
        break
