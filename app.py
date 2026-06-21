import streamlit as st
import pandas as pd

st.set_page_config(page_title="Enerji Şok Simülatörü", layout="centered")

df = pd.read_excel("DATA.xls")

# Sütun adlarını temizle
df.columns = df.columns.str.replace("\n", "", regex=False).str.strip()

# Sektör isimlerini temizle
df["Sektor"] = df["Sektor"].astype(str).str.replace("\n", "", regex=False).str.strip()

st.title("Enerji Şok Simülatörü")

st.write(
    "Bu araç, seçilen enerji ürünündeki fiyat değişiminin "
    "seçilen sektörün maliyetine yaklaşık etkisini hesaplar."
)

sektor = st.selectbox("Sektör seç", df["Sektor"].unique())

enerji = st.selectbox(
    "Enerji ürünü seç",
    [
        "Komur_urunleri",
        "Petrol_urunleri",
        "Dogal_Gaz",
        "Elektrik",
        "Isı",
        "Diger_urunler"
    ]
)

degisim = st.number_input("Fiyat değişimi (%)", value=20.0)

satir = df[df["Sektor"] == sektor].iloc[0]
katsayi = satir[enerji]

# Eğer Excel'de değerler %16 gibi girildiyse pandas bunu 0.16 okuyabilir.
# Eğer 16 olarak okursa 100'e bölüyoruz.
if katsayi > 1:
    katsayi = katsayi / 100

sonuc = katsayi * degisim

st.metric("Tahmini nihai maliyet değişimi", f"%{sonuc:.2f}")

st.caption(f"Kullanılan katsayı: {katsayi:.4f}")
