#Gorev1 verilen degerlerin veri yapilarini inceleyiniz
x= 8
type(x)
y= 3.2
type(y)
z= 8j + 13
type(z)
a= "Hello World"
type(a)
b= True
type(b)
c= 23 < 22
type(c)
l= [1,2,3,4]
type(l)
# Sıralıdır
# Kapsayıcıdır
# Değiştirilebilir
d= {"Name" : "Jake", "Age": 23, "Adress" : "Downtown"}
type(d)
# Değiştirilebilir
# Kapsayıcı
# Sırasız
# Key değerleri farklı olacak
t= ("Machine Learning", "Data Science")
type(t)
# Değiştirilemez
# Kapsayıcı
# Sıralı
s= {"Python", "Machine Learning", "Data Science"}
type(s)
# Değiştirilebilir
# Sırasız + Eşsiz
# Kapsayıcı



x= 8
y= 3.2
z= 8j + 13
a= "Hello World"

tipler= [x, y, z, a]
tip= lambda i: type(i)
list(map(tip, tipler))


#Gorev2: verilen string ifadenin tüm hareflerini büyük harfe ceviriniz,
# virgul ve nokta yerine space koyunuz
# ve kelime kelime ayiriniz

text= "The goal is to turn data into information, and information into insight."
text= text.upper()
text= text.replace(",", " ")
text= text.replace(".", " ")
text= text.split()
print(text)

#Gorev3:Vereilen listeye asagidaki adimlari uygulayiniz
#adim1 verilen listenin eleman sayisina bakiniz
#adim2 0. ve 10. indeksteki elemanlari cagiriniz
#adim3 verilen liste ustunden ["D", "A", "T", "A"] listesi olusturunuz
#adim4 sekizinci indeksteki elemani siliniz
#adim5 yeni bir eleman ekleyiniz
#adim6 sekizinci indekse N elemanini tekrar ekleyiniz

lst= ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
len(lst)
lst[0]
lst[10]
lst_k= print(lst[0:4])
del lst[8]
print(lst)
lst + ["X"]
lst= lst + ["X"]
lst.insert(8, "N")
print(lst)


#Gorev4: Verilen sözlük yapisina asagidakileri uygulayiniz
#adim1 key degerlerine erisiniz
#adim2 valuelara erisiniz
#adim3 Daisy keyine ait 12 degerini 13 olarak güncelle
#adim4 Key degeri Ahmet value degeri [Turkey, 24] olan yeni bir deger ekleyiniz
#adim5 Antonio yu dictionaryden siliniz

dict= {'Christian': ["America", 18],
       'Daisy': ["England", 12],
       'Antonio': ["Spain", 22],
       'Dante': ["Italy", 25]}
dict.keys()
dict.values()
dict.get('Daisy')[1]=13
dict.values()
dict.update({"Daisy": ["England",13]})
dict.update({'Ahmet': ["Turkey", 24]})
dict.items()
dict.pop('Antonio')
dict.items()

#Gorev5 Arguman olarak bir liste alan, listenin icerisindeki tek ve cift sayilari ayri listelere atayan
#ve bu listeleri return eden bir fonksiyon yaziniz

#even_list, odd_list=func(l)

l= [2, 13, 18, 93, 22]
def func(list):
    even_list= []
    odd_list= []
    for i in l:
        if i %2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list, odd_list
even_list, odd_list= func(list)
print(even_list)
print(odd_list)

l= [2, 13, 18, 93, 22]
def func(list):
    even_list= [i for i in l if i %2==0]
    odd_list= [i for i in l if i %2!=0]
    return even_list, odd_list

even_list, odd_list = func(list)



#Gorev6 Asagida verilen listede mühendislik ve tip fakültelerinde dereceye giren
#ögrencilerin isimleri bulunmaktadir. Sirasiyla ilk uc ogrenci mühendislik fakültesinin
#basari sirasini temsil ederken, son üc ögrenci de tip fakültesi ögrenci sirasina aittir.
#Enumarate kullanarak ögrenci derecelerini fakulte özelinde yazdiriniz.

ogrenciler= ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece"]

for index, o in enumerate(ogrenciler, start=1):
    if index < 4:
        print("Mühendislik Fakültesi", index, ".", "ögrenci:", o)
    else:
        print("Tip Fakültesi", index-3, ".", "ögrenci:", o)

ogrenciler= ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece"]
Muh= (list(ogrenciler[0:3]))
Tip= (list(ogrenciler[3:]))
for index, m in enumerate(Muh, start=1):
    print("Mühendislik Fakültesi", index, ".", "ögrenci:", m)
for index, t in enumerate(Tip, start=1):
    print("Tip Fakültesi", index, ".", "ögrenci:", t)


ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]
for i,x in enumerate(ogrenciler):
    if i<3:
        i += 1
        print("Mühendislik Fakültesi",i,". öğrenci: ",x)
    else:
        i -= 2
        print("Tıp Fakültesi",i,". öğrenci: ",x)


### ya da bir başka çözüm:

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

# Mühendislik Fakültesi
for index, ogrenci in enumerate(ogrenciler[:3], 1):
    print(f"Mühendislik Fakültesi {index}. öğrenci: {ogrenci}")

# Tıp Fakültesi
for index, ogrenci in enumerate(ogrenciler[3:], 1):
    print(f"Tıp Fakültesi {index}. öğrenci: {ogrenci}")

#Gorev7 Asagida üc adet liste verilmistir. Listelerde sirasi ile bir dersin kodu,
# kredisi ve kontenjan bilgileri yer almaktadir.
# Zip kullanarak ders bilgilerini bastiriniz.

ders_kodu= ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi= [3, 4, 2, 4]
kontenjan= [30, 75, 150, 25]
list(zip(ders_kodu,kredi,kontenjan))

for ders_kodu, kredi, kontenjan in zip(ders_kodu,kredi,kontenjan):
    print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjani {kontenjan} kisidir.")
#f-string



#Gorev8 Asagida iki adet set verilmistir.
# Eger 1. küme 2. kümeyi kapsiyor ise ortak elemanlarini,
#kapsamiyor ise 2. kümenin 1. kümeden farkini
# yazdiracak fonkiyonu tanimlayiniz.
#issupperset
#intersection-difference

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda","python", "miuul"])
def sonuc(kume1, kume2):
    if kume1.issuperset(kume2):
        print(kume1.intersection(kume2))
    else:
        print(kume2.difference(kume1))

sonuc(kume1, kume2)

