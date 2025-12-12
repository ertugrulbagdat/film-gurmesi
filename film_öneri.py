import pandas as pd 
import os 
TUR_CEVIRI = {
    "aksiyon": "Action",
    "macera": "Adventure",
    "animasyon": "Animation",
    "biyografi": "Biography",
    "komedi": "Comedy",
    "suç": "Crime",
    "dram": "Drama",
    "aile": "Family",
    "fantastik": "Fantasy",
    "tarih": "History",
    "korku": "Horror",
    "müzik": "Music",
    "gizem": "Mystery",
    "romantik": "Romance",
    "bilim kurgu": "Sci-Fi",
    "spor": "Sport",
    "gerilim": "Thriller",
    "savas": "War",
    "western": "Western"
}
def veri_getir():
    print("\n Yerel Dosya Bulunuyor...")
    dosya = "imdb_top_1000.csv"
    try:
        df=pd.read_csv(dosya)
        df = df.rename(columns={
            "Series_Title": "Film_Adi",
            "Released_Year": "Yil",
            "IMDB_Rating": "Puan",
            "Genre": "Tur"
        })
        df = df[df["Yil"].astype(str).str.isnumeric()]
        df["Yil"]=df["Yil"].astype(int)
        print("\n Veriler yüklendi")
        return df
    except Exception as e:
        print(f" Hata: Dosya bulunamadı.Hata Mesajı: {e}")
        return None
def genel_analiz(df):
    print("\n VERİ TABLOSU ANALİZİ")
    print("-"*40)
    print(f"Toplam Film Sayısı:{len(df)}")
    print("\nEn Yüksek Puanlı 5 Film:")
    print(df.nlargest(5, 'Puan')[['Film_Adi', 'Yil', 'Puan']].to_string(index=False))
def film_oner(df):
    print("="*40)
    print("\n FİLM ÖNERİ ASİSTANI")
    print("-"*40)
    print("Seçebileceğiniz Türler:")
    print(" | ".join(sorted(TUR_CEVIRI.keys())))
    istenen =input("\n Hangi tür istersiniz?\n :").lower().strip()
    if istenen in TUR_CEVIRI:
        ingilizce_tur=TUR_CEVIRI[istenen]
        filtre=df[df["Tur"].str.contains(ingilizce_tur,case=False,na=False)]
        if len(filtre)>0:
            kaliteli=filtre[filtre["Puan"]>7.0]
            if len(kaliteli)==0:
                kaliteli=filtre
            secim=kaliteli.sample(n=1).iloc[0]
            print("\n ÖNERİM:")
            print(f" {secim['Film_Adi']} ({secim['Yil']})")
            print(f" IMDb: {secim['Puan']}")
            print(f" Tür: {secim['Tur']}")
        else:
            print("Bu türde film bulunamadı.")
    else:
        print("Listede olmayan bir tür yazdınız.")

pd.set_option("display.max_columns",None)
pd.set_option("display.width",1000)
df=veri_getir()
if df is not None:
    while True:
        print("\n"+ "-"*40)
        print("1. En Yüksek IMDB 1-5")
        print("2. Film Öner")
        print("3. Çıkış" )
        karar = input("Seçim: ")
        if karar=="1":
            genel_analiz(df)
        elif karar=="2":
            film_oner(df)
        elif karar=="3":
            print("Görüşmek üzereee...")
            break
        else:
            print("Hatalı Tuşlama. Tekrar seçim yapınız.")