# Akbank Python Bootcamp: Global AI Hub
Akbank ve Global AI Hub iş birliğinde Yapay Zeka ve modern dijital teknolojiler alanlarında, okuryazarlık, programlama ve temel bilgi seviyesi edinmeniz için bir  Bootcamp.

## Takım Üyeleri
- Sabir SÜLEYMANLI,   _suleymanlisabir3@gmail.com_
- Beyza Ceylan,       _beyzaceylan0134@gmail.com_
- Nizam Doğan Çinar,  _doganccinar@gmail.com_
- Yasemin EKER, _yasemineker06@hotmail.com_
- Ecem Altınkeser, 

## Proje Detayı

**Pizza Sipariş Sistemi**


Pizzacı Dükkanı mı açmak istiyorsunuz? O zaman bu proje hayalinizdeki proje olabilir. Proje, kullanıcıların kendi pizzalarını tasarlamalarını ve ödeme yaptıktan sonra kullanıcıyı veri tabanına eklemelerini hedefliyor. Peki bu projede ne tür görevlerimiz var?

Sistem, kullanıcıların menüdeki pizzayı ve istedikleri sosu seçmesiyle başlar. İkinci aşama olarak seçtikleri sos ve pizzayı seçtikten sonra ödemeye kısmına geçiş yaparlar. Kullanıcılar ödemelerini kredi kartı ile yapacaktır. Her pizzanın bir açıklaması ve fiyatı vardır. AÇıklama ve fiyat sınıflar içinde sabit bir değer olarak ayarlanması gerektiğine dikkat edin.

## 1.Google Colab Dosyası Oluşturma

- Projenizin .ipynb veya .py uzantısına sahip olduğundan emin olun.
- Projenizde ayrıntıları açıklayan yorum satırları olduğundan emin olun.

## 2.Gerekli Kitaplıkları İçe Aktarma
_Import csv
_Import datetime 

## 3.“Menu.txt” dosyasını oluştur
- Menu.txt adlı bir dosya oluşturun ve içine aşağıdaki metni yazın.

_* Lütfen Bir Pizza Tabanı Seçiniz:
_1: Klasik
_2: Margarita
_3: TürkPizza
_4: Sade Pizza
_* ve seçeceğiniz sos:
_11: Zeytin
_12: Mantarlar
_13: Keçi Peyniri
_14: Et
_15: Soğan
_16: Mısır
_* Teşekkür ederiz!

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

   _def get_cost(self):
       return self.component.get_cost() + \
         Pizza.get_cost(self)_


   _def get_description(self):
       return self.component.get_description() + \
         ' ' + Pizza.get_description(self)_

- Sos olarak Zeytin, Mantar, Keçi Peyniri, Et, Soğan ve Mısır'ı belirleyin ve belirlediğiniz sosların her birini bir sınıf olarak tanımlayın.
Unutmayın ki her sosun kendine ait bir fiyatı ve değişken olarak her bir pizzanın açıklaması olması gerekir.
- Bir main fonksiyonu oluşturun. Bu fonksiyon önce menüyü ekrana yazdıracaktır. Ardından kullanıcının menüden bir pizza ve sos seçmesine imkan tanıyacaktır. Seçilen ürünlerin toplam fiyatını hesapladıktan sonra kullanıcıdan isim, TC kimlik numarası, kredi kartı numarası ve kredi kartı şifresi istemektedir. 
- Veritabanı olarak adlandırdığımız "Orders_Database.csv" dosyasında pizzasını seçen ve kullanıcı adını, kullanıcı kimliğini, kredi kartı bilgilerini, sipariş açıklamasını, sipariş zamanını ve kredi kartı şifresini tutan bir tablo oluşturunuz

## 7.Proje Teslimi

- Proje için .ipynb veya .py uzantılı bir kod dosyası hazırlamanız projenizin çalışır durumda olması gerekiyor.
- Hazırladığınız bu dosyaları bir GitHub reposuna eklemeniz ve bu reponun bağlantısını tarafınıza proje teslim günü iletilecek forma eklemeniz gerekiyor.
- Projeler ekip olarak veya bireysel olarak yapılacaktır. Oluşturulan ekipler maksimum 5 kişiden oluşmalıdır.
- Proje Teslim Tarihi: 13 Mart 2023 Saat 23:59
