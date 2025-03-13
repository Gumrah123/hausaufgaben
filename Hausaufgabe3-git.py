#Görev1 Seaborn kütüphanesi icinde Titanic veri setini tanimlayiniz


import pandas as pd

import seaborn as sns
tit = sns.load_dataset("titanic")
tit.head()
tit.shape
tit.describe()


#Görev2 Titanic veri setindeki kadin ve erkek yolcu sayilarini bulunuz
tit.groupby("sex")["sex"].count()
gender_count = tit["sex"].value_counts()
print(gender_count)

#Görev3 Her bir sütuna ait unique degerlerin sayisini bulunuz

tit.nunique()

#Görev4 pclass degiskeninin unique degerlerin sayisini bulunuz

tit["pclass"].nunique()

#Görev5 pclass ve parch degiskenlerinin unique degerlerin sayisini bulunuz

tit[["pclass", "parch"]].nunique()

#Görev6 embarket degiskeninin tipini kontrol ediniz.
# Tipini category olarak degistiriniz ve tekrar kontrol ediniz.

tit["embarked"].dtype
tit["embarked"] = tit["embarked"].astype("category")
tit["embarked"].info

#Görev7 embarked degeri C olanlarin tüm bilgilerini gösteriniz

tit[tit["embarked"] == "C"]

#Görev8 embarked degeri S olmayanlarin tüm bilgilerini gösteriniz

tit[tit["embarked"] != "S"]
tit[tit["embarked"] != "S"]["embarked"]

#Görev9 Yasi 30 dan kücük ve kadin olan yolcularin tüm bilgilerini gösterin
tit.loc[(tit["age"] < 30) & (tit["sex"] == "female")]

#Görev10 Fare'i 500 den büyük veya yasi 70 den buyuk yolcularin bilgilerini gösterin

tit.loc[(tit["fare"] > 500) | (tit["age"] > 70)]

#Görev11 Her bir degiskendeki bos degerlerin toplamini bulunuz

tit.isnull().sum()

#Görev12 WHO degiskenini df den cikarin
tit.drop("who", axis=1, inplace= True)
#inplace= True kalici degisiklik yapiyordu

#Görev13 Deck degiskenindeki bos degerleri deck degiskeninin
#en cok tekrar eden degeri (mode) ile doldurunuz

tit["deck"].isnull().sum()
tit["deck"].mode()
tit["deck"] = tit["deck"].fillna(tit["deck"].mode()[0])
tit["deck"].isnull().sum()
##tit["deck"].fillna(tit["deck"].mode()[0], inplace= True)
# pandas 3.0 versiyonundan sonra inplace kullanimi degismis !!!


#Görev14 Age degiskenindeki bos degerleri age degiskeninin mediani ile doldurunuz

tit["age"].isnull().sum()

tit["age"]  = tit["age"].fillna(tit["age"].median())
tit["age"].isnull().sum()

#Görev15 survived degiskeninin pclass ve cinsiyet degiskenleri kiriliminda
# sum, count, mean degerlerini bulun
tit.groupby(["pclass", "sex"])[["survived"]].aggregate("count").unstack()
tit.groupby(["pclass", "sex"])[["survived"]].aggregate("sum").unstack()
tit.groupby(["pclass", "sex"])[["survived"]].aggregate("mean").unstack()

tit.groupby(["pclass", "sex"])[["survived"]].aggregate(["sum", "count", "mean"])

tit.groupby(["pclass", "sex"]).agg({"survived" : ["sum", "count", "mean"]})
#Görev16 30 yasin altinda olanlar 1, 30'a esit ve büyük olanlara 0 verecek
#bir fonk. yazin. Yazdiginiz fonk. kullanarak titanik veri setinde age_flag adinda
# bir degisken olusturun. (apply ve lambda'yi kullanin)

def yas(age):
    if age < 30:
        return 1
    else:
        return 0
tit["age_flag"] = tit["age"].apply(lambda x: yas(x))
tit["age_flag"].info

#Görev17 Seaborn kütüphanesi icerisinden tips veri setini tanimlayin
tip = sns.load_dataset("tips")
tip.head()

#Görev18 Time degiskeninin kategorilerine (Dinner, Lunch) göre total_bill
#degerinin toplamini, min, max, ortalamasini bulunuz

tip.groupby("time")[["total_bill"]].aggregate(["sum", "min", "max","mean"])

#yeni sürümümde hata veriyormus o nedenle observed=false ifadesi eklenince vermiyormus??
#tip.groupby("time" ,observed=False)[["total_bill"]].aggregate(["sum", "min", "max","mean"])

#Görev19 Günlere ve time göre total_bill degerinin toplamini, min, max, ortalamasini bulunuz

tip.groupby(["day", "time"])[["total_bill"]].aggregate(["sum", "min", "max","mean"])


#Görev20 Lunch zamanina ve kadin müsterilere ait total_bill ve tip degerlerinin
# day a göre toplamini, min, max, ortalamasini bulunuz

###!!!!!ßß

tip[(tip["sex"]=="Female")&(tip["time"]=="Lunch")].groupby("day")[["total_bill","tip"]].agg(["sum","min","max","mean"])



#Görev21 size'i 3ten kücük, total_bill'i 10'dan büyük olan
# siparislerin ortalamasi nedir (loc kullanin)

tip.loc[(tip.size < 3) & (tip.total_bill > 10),["size", "total_bill"]].mean()

#Görev22 total_bill_tip_sum adinda yeni bir degisken olusturun.
#her bir müsterinin ödedigi total bil ve tipin toplamini versin

tip["total_bill_tip_sum"] = tip["total_bill"] + tip["tip"]
tip.head()

#Görev23 total_bill_tip_sum degiskenini büyükten kücüge siralayin ve
# ilk  30 kisiyi yeni bir date frame atayin

tip["total_bill_tip_sum"].sort_values()
df_new= tip["total_bill_tip_sum"].sort_values()[0:30]
df_new.head()