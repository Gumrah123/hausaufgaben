#Aufgabe_1 Beantworten Sie die folgenden Fragen:
#1-Lesen Sie die CSV-Datei ein und zeigen Sie beschreibende Informationen über den Datensatz an
import matplotlib.pyplot as plt
plt.ion()
import pandas as pd
import numpy as np

df= pd.read_csv(r"C:\Users\User Laptop\Desktop\phyton\phyton_ders\customers-odev4.csv")

#Fehler:Raw-String vor das C gesetzt, sonst konnte die Datei nicht geöffnet werden

df.head(10)
df.info()
df.dtypes
df.shape
df.describe().T
df.isnull().values.any()
df.isnull().sum()

#2-Wie viele einzigartige (unique) PLATFORM gibt es? Was sind ihre Frequenzen?

df["PLATFORM"].unique()
df["PLATFORM"].value_counts().count()
df["PLATFORM"].value_counts()

#3-Wie viele einzigartige (unique) PRICE gibt es?

df["PRICE"].value_counts()
df["PRICE"].value_counts().count()

#4-Wie viele Einheiten  von PRICE wurden verkauft?
df["PRICE"].value_counts()

#5-Wie viele Einheiten wurden aus welchem Land verkauft?
df["REGION"].value_counts()

#6-Wie viel wurde insgesamt durch Verkäufe nach Ländern verdient?
df.groupby("REGION")["PRICE"].sum()
#wenn wir sortieren wollen (vom K zum G)
l= (df.groupby("REGION")["PRICE"].sum()).tolist()
l.sort()
print(l)

#7-Wie hoch sind die Verkaufszahlen ("PRICE") nach Plattformtypen ("PLATFORM")?

df.groupby("PLATFORM")["PRICE"].count()

#8-Wie hoch ist der Preisdurchschnitte (PRICE-mean) je nach Land (REGION)?

df.groupby("REGION")["PRICE"].mean()

#9-Wie hoch ist der Preisdurchschnitte (PRICE-mean) je nach Land (PLATFORM)?

df.groupby("PLATFORM")["PRICE"].mean()

#10-Wie hoch sind die Durchschnittspreise (PRICE-mean) in der Aufschlüsselung "REGION" und "PLATFORM?

df.groupby(["REGION", "PLATFORM"])["PRICE"].mean()

#Aufgabe_2 Wie hoch sind die Durchschnittspreise (PRICE-mean)
# in der Aufschlüsselung "REGION", "PLATFORM", "GENDER", "AGE"?

df.groupby(["REGION", "PLATFORM", "GENDER", "AGE"])["PRICE"].mean()

#Aufgabe_3 Sortieren Sie die Ausgabe absteigend nach der Variable "PRICE"
# und speichern Sie die Ergebnisse als "agg_df".

agg_df= df.groupby(["REGION", "PLATFORM", "GENDER", "AGE"])["PRICE"].mean().sort_values(ascending= False)

agg_df.head(10)

#Aufgabe_4 Weisen Sie die im Index enthaltenen Namen als Variablen zu.
agg_df= agg_df.reset_index()

#Aufgabe_5 Konvertieren Sie die Variable AGE in eine kategoriale Variable
# und fügen Sie sie zum agg_df hinzu.
# Die Alterskategorien sollten wie folgt lauten (0-18, 19-23, 24-30, 31-40, 41-70)

agg_df["yas_kat"]= pd.cut(agg_df["AGE"], [0, 18, 23, 30, 40, 90], labels= ["0_18", "19_23", "24_30", "31_40", "41_70"])
agg_df.head()
plt.show()
agg_df.values
#Aufgabe_6 Yeni seviye tabanli müsteri gruplarini olusturun. yeni bir degisken ekleyin; costumer_profile
#(list comprehension ile olustur, sonra tekilleme yap)

agg_df["customer_profile"] = list(map(lambda row: row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5] ,agg_df.values))
print(agg_df["customer_profile"])

agg_df= agg_df.groupby(["customer_profile"])[["PRICE"]].aggregate({"PRICE": "mean"})
agg_df.head()


#Aufgabe_7 Yeni müsterileri PRICE göre 4 segmente ayir
#segmenteleri "SEGMENT" isimlendirmesi ile degisken olarak agg_df ekle
#Segmentleri betimleyiniz (segmentlere göre groupby yapip PRICE max, mean ve sumlarini aliniz)
#ipucu pd.qcut(agg_df["PRICE"],4,labels= ["D", "C", "B", "A"]
agg_df["SEGMENT"]= pd.qcut(agg_df["PRICE"],4,labels= ["D", "C", "B", "A"])
agg_df.groupby(["SEGMENT"])[["PRICE"]].agg(["mean", "max","sum"])


agg_df.sort_values("PRICE", ascending= False)

#Aufgabe_8 Yeni gelen müsterileri siniflandirip, ne kadar gelir getirebileceklerini tahmin ediniz.
#33yasinda ANDROID kullanan bir Türk kadini hangi segmente aittir ve
# ortalama ne kadar gelir kazanmasi beklenir
#35 yasinda IOS kullanan bir Fransiz kadini hangi segmente aittir ve
# ortalama ne kadar gelir kazanmasi beklenir
#ipucu new_user= "TUR_ANDROID_FEMALE_31_40" agg_df[agg_df["customer_profile"] == new_user]


agg_df["SEGMENT"]["TUR_ANDROID_FEMALE_31_40"]



new_user= "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customer_profile"] == new_user]

new_user= "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customer_profile"] == new_user]
