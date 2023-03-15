## Bu Dosyayı başka dillerde oku:
<a href="README.en.md"><img src="https://img.shields.io/badge/-ENGLISH-red?style=for-the-badge"></a>
<a href="README.md"><img src="https://img.shields.io/badge/-T%C3%9CRK%C3%87E-red?style=for-the-badge"></a>

# Akbank Python Bootcamp: Global AI Hub
Akbank ve Global AI Hub iş birliğinde Yapay Zeka ve modern dijital teknolojiler alanlarında, okuryazarlık, programlama ve temel bilgi seviyesi edinmeniz için bir  Bootcamp.

<table><tr>
<td> <img src="https://globalaihub.com/wp-content/uploads/2021/07/globalaihub-logo-1-1024x424.png" width="200""/> </td>
<td><td><td><td><td>
<td> <img src="https://w7.pngwing.com/pngs/973/59/png-transparent-akbank-hd-logo.png" width="200""/> </td>
</tr></table>


## Takım Üyeleri
- Sabir SÜLEYMANLI,   _suleymanlisabir3@gmail.com_
- Beyza Ceylan,       _beyzaceylan0134@gmail.com_
- Yasemin EKER, _yasemineker66@gmail.com_
- Ecem ALTINKESER, _ecemaltinkeser@gmail.com_

## Proje Detayı

**Pizza Sipariş Sistemi**


Pizzacı Dükkanı mı açmak istiyorsunuz? O zaman bu proje hayalinizdeki proje olabilir. Proje, kullanıcıların kendi pizzalarını tasarlamalarını ve ödeme yaptıktan sonra kullanıcıyı veri tabanına eklemelerini hedefliyor. Peki bu projede ne tür görevlerimiz var?

Sistem, kullanıcıların menüdeki pizzayı ve istedikleri sosu seçmesiyle başlar. İkinci aşama olarak seçtikleri sos ve pizzayı seçtikten sonra ödemeye kısmına geçiş yaparlar. Kullanıcılar ödemelerini kredi kartı ile yapacaktır. Her pizzanın bir açıklaması ve fiyatı vardır. AÇıklama ve fiyat sınıflar içinde sabit bir değer olarak ayarlanması gerektiğine dikkat edin.


## 1.Google Colab Dosyası Oluşturma

- Projenizin .ipynb veya .py uzantısına sahip olduğundan emin olun.
- Projenizde ayrıntıları açıklayan yorum satırları olduğundan emin olun.


## 2.Gerekli Kitaplıkları İçe Aktarma
```
Import csv
Import datetime 
```

## 3.“Menu.txt” dosyasını oluştur
- Menu.txt adlı bir dosya oluşturun ve içine aşağıdaki metni yazın.

* Lütfen Bir Pizza Tabanı Seçiniz:
1: Klasik
2: Margarita
3: TürkPizza
4: Sade Pizza
* ve seçeceğiniz sos:
11: Zeytin
12: Mantarlar
13: Keçi Peyniri
14: Et
15: Soğan
16: Mısır
* Teşekkür ederiz!


## 4.Üst sınıf oluştur “pizza”
- Pizza sınıfını ve bu sınıfın içindeki encapsulation(kapsülleme) için get_description() ve get_cost() methodları tanımlayın.

**NOT: Bu açıklama hazırlanan pizzanın kısa bir açıklaması olmalıdır!**


## 5.Alt sınıf oluştur “pizza”
- Klasik, Margherita, Türk Pizzası, Dominos Pizza vb. pizza sınıfları oluşturun. Bu pizza türlerinin her biri bir pizza türü olduğu için bu sınıflar alt sınıflar olarak tanımlanacaktır.
- Her pizzanın kendine ait bir fiyatı ve sahip olduğu değişkenin içinde pizzaların açıklamasının yer alması gerektiğini unutmayın.


## 6.Üst sınıf oluştur “Decorator”
- Bir Decorator sınıfı oluşturun. Decorator, burada tüm sos sınıflarının süper sınıfı olarak adlandırılır.
- Decorator sınıfı, pizza sınıfının özelliklerini kullanarak get_description() ve get_cost() yöntemlerini kullanacaktır. Aşağıdaki yöntemleri kullanarak decorator sınıfını tamamlayın.

**SAMPLE CODE** 

     def get_cost(self):
       return self.component.get_cost() + \
         Pizza.get_cost(self) 


    def get_description(self):
       return self.component.get_description() + \
         ' ' + Pizza.get_description(self) 

- Sos olarak Zeytin, Mantar, Keçi Peyniri, Et, Soğan ve Mısır'ı belirleyin ve belirlediğiniz sosların her birini bir sınıf olarak tanımlayın.
Unutmayın ki her sosun kendine ait bir fiyatı ve değişken olarak her bir pizzanın açıklaması olması gerekir.
- Bir main fonksiyonu oluşturun. Bu fonksiyon önce menüyü ekrana yazdıracaktır. Ardından kullanıcının menüden bir pizza ve sos seçmesine imkan tanıyacaktır. Seçilen ürünlerin toplam fiyatını hesapladıktan sonra kullanıcıdan isim, TC kimlik numarası, kredi kartı numarası ve kredi kartı şifresi istemektedir. 
- Veritabanı olarak adlandırdığımız "Orders_Database.csv" dosyasında pizzasını seçen ve kullanıcı adını, kullanıcı kimliğini, kredi kartı bilgilerini, sipariş açıklamasını, sipariş zamanını ve kredi kartı şifresini tutan bir tablo oluşturunuz


## 7.Proje Teslimi

- Proje için .ipynb veya .py uzantılı bir kod dosyası hazırlamanız projenizin çalışır durumda olması gerekiyor.
- Hazırladığınız bu dosyaları bir GitHub reposuna eklemeniz ve bu reponun bağlantısını tarafınıza proje teslim günü iletilecek forma eklemeniz gerekiyor.
- Projeler ekip olarak veya bireysel olarak yapılacaktır. Oluşturulan ekipler maksimum 5 kişiden oluşmalıdır.
- Proje Teslim Tarihi: 13 Mart 2023 Saat 23:59
