import streamlit as st

# 🔒 YETKİ KONTROL KİLİDİ
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("⚠️ Lütfen önce ana sayfadan giriş yapın kanka!")
    st.stop()

if st.session_state.get("role") != "admin":
    st.error("🔒 Yetki Hatası: Bu sayfaya sadece Onay Yetkilileri (Danışman, Koordinatör, Bina Sorumlusu) erişebilir!")
    st.stop()

st.title("📋 Yönetici Onay Paneli")
current_email = st.session_state.get("email", "")
st.write(f"Giriş Yapan Yetkili: **{current_email}**")

st.info("**Talep Eden:** İTÜ Robotik Kulübü\n\n**Etkinlik:** Robot Günleri Hazırlığı\n\n**Sınıf:** EEB - 1101")

# Giriş yapan e-postaya göre rolü otomatik eşleştiriyoruz
if current_email == "danisman@itu.edu.tr":
    onay_rolu = "Danışman (advisor)"
elif current_email == "koordinator@itu.edu.tr":
    onay_rolu = "Koordinatör (coordinator)"
elif current_email == "bina@itu.edu.tr":
    onay_rolu = "Bina Sorumlusu (building_mgr)"
else:
    onay_rolu = "Genel Yönetici"

st.success(f"Şu an **{onay_rolu}** yetkisiyle işlem yapıyorsunuz.")

yorum = st.text_input("Onay/Ret Notu (Yorum ekleyin)")

col1, col2 = st.columns(2)
with col1:
    if st.button("👍 Onayla"):
        st.success(f"Talep, {onay_rolu} tarafından ONAYLANDI. Süreç ilerletiliyor.")
with col2:
    if st.button("👎 Reddet"):
        st.error(f"Talep, {onay_rolu} tarafından REDDEDİLDİ. Kulübe bilgi gönderildi.")
    import streamlit as st

st.title("📋 Yönetici Onay Paneli")
st.write("Sistemdeki onay bekleyen aktif rezervasyon talepleri.")

st.info("**Talep Eden:** İTÜ Robotik Kulübü\n\n**Etkinlik:** Robot Günleri Hazırlığı\n\n**Sınıf:** EEB - 1101")

# Takım B'nin dökümanındaki resmi ENUM onay seviyeleri
onay_rolu = st.selectbox("Onay Yetkili Rolünüzü Seçin", ["advisor", "coordinator", "building_mgr"])
yorum = st.text_input("Onay/Ret Notu (Yorum ekleyin)")

col1, col2 = st.columns(2)
with col1:
    if st.button("👍 Onayla"):
        st.success(f"Talep {onay_rolu} seviyesinde ONAYLANDI. Bir sonraki aşamaya aktarılıyor.")
with col2:
    if st.button("👎 Reddet"):
        st.error(f"Talep {onay_rolu} tarafından REDDEDİLDİ. Kulübe bildirim gönderildi.")
