import streamlit as st
import pandas as pd

st.set_page_config(page_title="Enerji Şok Simülatörü", layout="centered")

df = pd.read_excel("DATA.xls")

st.title("Enerji Şok Simülatörü")

st.write(
    "Bu araç, seçilen enerji ürünündeki fiyat değişiminin "
    "seçilen sektörün maliyetine yaklaşık etkisini hesaplar."
)

sektor = st.selectbox("Sektör seç", df["Sektör"].unique())

enerji = st.selectbox(
    "Enerji ürünü seç",
    ["Kömür", "Petrol", "Doğalgaz", "Elektrik", "Isı"]
)

degisim = st.number_input("Fiyat değişimi (%)", value=20.0)

satir = df[df["Sektör"] == sektor].iloc[0]
katsayi = satir[enerji]

sonuc = katsayi * degisim

st.metric("Tahmini nihai maliyet değişimi", f"%{sonuc:.2f}")

st.caption(f"Kullanılan katsayı: {katsayi:.4f}")
