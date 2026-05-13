import streamlit as st

# 🔒 YETKİ KONTROL KİLİDİ
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("⚠️ Lütfen önce ana sayfadan giriş yapın kanka!")
    st.stop()

if st.session_state.get("role") != "club":
    st.error("🔒 Yetki Hatası: Bu sayfa sadece Kulüp Yöneticileri ve Öğrenciler içindir!")
    st.stop()

# --- Sayfanın kalan orijinal rezervasyon kodları aşağıda aynen devam ediyor ---
st.title("📅 Yeni Sınıf Rezervasyon Talebi")
st.write(f"Aktif Hesap: **{st.session_state['email']}**")
# (Geri kalan form elemanları...)
    
    import streamlit as st

st.title("📅 Yeni Sınıf Rezervasyon Talebi")
st.write("Etkinliğiniz için rezervasyon formunu eksiksiz doldurun.")

# Takım B'nin Reservation tablosundaki resmi alan adları
event_title = st.text_input("Etkinlik Adı (event_title)")
event_description = st.text_area("Etkinlik Açıklaması (event_description)")
event_date = st.date_input("Etkinlik Tarihi (event_date)")
start_time = st.time_input("Başlangıç Saati (start_time)")
end_time = st.time_input("Bitiş Saati (end_time)")
expected_attendees = st.number_input("Tahmini Katılımcı Sayısı (expected_attendees)", min_value=1, value=10)

if st.button("Talebi Gönder"):
    if event_title:
        st.success(f"'{event_title}' talebiniz başarıyla oluşturuldu! Durumu: pending (Onay Bekliyor)")
        st.info("Süreç Başladı: Danışman Onayı -> Koordinatör Onayı -> Bina Sorumlusu Onayı")
    else:
        st.error("Lütfen etkinlik adını boş bırakmayın!")
