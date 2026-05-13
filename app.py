import streamlit as st

# 🔑 SOL MENÜYÜ GİRİŞ YAPANA KADAR GİZLEME AYARI
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.set_page_config(initial_sidebar_state="collapsed")
    st.markdown(
        """<style>[data-testid="stSidebarNav"] {display: none !important;}</style>""",
        unsafe_allow_html=True
    )

st.title("🔑 ClubSpace İTÜ Giriş Paneli")
st.write("Lütfen İTÜ test hesap bilgilerinizle giriş yapın.")

# Giriş Formu Elemanları
email = st.text_input("E-posta Adresi")
password = st.text_input("Şifre", type="password")

if st.button("Giriş Yap"):
    if password == "1234":
        # Kulüp ve Öğrenci Rolü Tanımlaması
        if email in ["kulup@itu.edu.tr", "ogrenci@itu.edu.tr"]:
            st.session_state["logged_in"] = True
            st.session_state["role"] = "club"
            st.session_state["email"] = email
            st.success(f"Başarıyla Giriş Yapıldı! Rol: Kulüp Yöneticisi / Öğrenci ({email})")
            st.rerun()
            
        # Onay Yetkilileri (Admin/Yönetici) Rolü Tanımlaması
        elif email in ["danisman@itu.edu.tr", "koordinator@itu.edu.tr", "bina@itu.edu.tr"]:
            st.session_state["logged_in"] = True
            st.session_state["role"] = "admin"
            st.session_state["email"] = email
            st.success(f"Başarıyla Giriş Yapıldı! Rol: Onay Yetkilisi ({email})")
            st.rerun()
            
        else:
            st.error("Bu e-posta adresi sistemde tanımlı değil kanka!")
    else:
        st.error("Hatalı şifre! Lütfen tekrar deneyin.")

# Giriş yapıldıktan sonra dinamik menü gizleme/gösterme CSS şovları
if "logged_in" in st.session_state and st.session_state["logged_in"]:
    rol = st.session_state.get("role", "club")
    st.sidebar.write(f"📋 Aktif Kullanıcı: {st.session_state['email']}")
    
    if rol == "club":
        # Kulüp başkanına Onay Paneli'ni (4. sayfayı) gizliyoruz
        st.markdown(
            """<style>[data-testid="stSidebarNav"] li:nth-child(4) {display: none !important;}</style>""", 
            unsafe_allow_html=True
        )
    elif rol == "admin":
        # Yöneticiye de Rezervasyon Yap (3. sayfayı) gizliyoruz
        st.markdown(
            """<style>[data-testid="stSidebarNav"] li:nth-child(3) {display: none !important;}</style>""", 
            unsafe_allow_html=True
        )
        
import streamlit as st

# 🔑 SOL MENÜYÜ GİRİŞ YAPANA KADAR GİZLEME AYARI
if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.set_page_config(initial_sidebar_state="collapsed") # Sol menüyü tamamen kapatır
    
    # Sol menünün içindeki butonları kodla da gizliyoruz (Kullanıcı yandan açamasın diye)
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {display: none !important;}
        </style>
        """,
        unsafe_allow_html=True
    )

    
    
    
    import streamlit as st

st.set_page_config(
    page_title="ClubSpace ITU",
    page_icon="🏫",
    layout="wide"
)

# Basit mock auth - session state ile giris durumu tutuyoruz
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_role = None
    st.session_state.user_name = None
    st.session_state.user_club = None

def login(email, password):
    """Mock authentication - gercek projede veritabanindan kontrol edilir"""
    mock_users = {
        "kulup@itu.edu.tr": {"password": "1234", "name": "Ahmet Yilmaz", "role": "club_admin", "club": "ITU Robotik Kulubu"},
        "danisman@itu.edu.tr": {"password": "1234", "name": "Prof. Dr. Ayse Demir", "role": "advisor", "club": None},
        "koordinator@itu.edu.tr": {"password": "1234", "name": "Mehmet Kaya", "role": "coordinator", "club": None},
        "bina@itu.edu.tr": {"password": "1234", "name": "Fatma Celik", "role": "building_mgr", "club": None},
        "ogrenci@itu.edu.tr": {"password": "1234", "name": "Can Ozturk", "role": "student", "club": None},
    }
    if email in mock_users and mock_users[email]["password"] == password:
        user = mock_users[email]
        st.session_state.logged_in = True
        st.session_state.user_name = user["name"]
        st.session_state.user_role = user["role"]
        st.session_state.user_club = user["club"]
        return True
    return False

def logout():
    st.session_state.logged_in = False
    st.session_state.user_role = None
    st.session_state.user_name = None
    st.session_state.user_club = None

# ---- ANA SAYFA ----
if not st.session_state.logged_in:
    st.title("🏫 ClubSpace ITU")
    st.subheader("Ogrenci Kulubu Derslik Rezervasyon Platformu")
    st.write("ITU ogrenci kuluplerinin derslik rezervasyon surecini dijitallestiren platform.")
    
    st.divider()
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("### Giris Yap")
        email = st.text_input("ITU E-posta", placeholder="ornek@itu.edu.tr")
        password = st.text_input("Sifre", type="password")
        
        if st.button("Giris Yap", type="primary", use_container_width=True):
            if not email.endswith("@itu.edu.tr"):
                st.error("Lutfen ITU e-posta adresinizi kullanin (@itu.edu.tr)")
            elif login(email, password):
                st.success(f"Hos geldiniz, {st.session_state.user_name}!")
                st.rerun()
            else:
                st.error("E-posta veya sifre hatali!")
    
    with col2:
        st.markdown("### Test Hesaplari")
        st.info("""
        **Kulup Yoneticisi:** kulup@itu.edu.tr  
        **Danisman:** danisman@itu.edu.tr  
        **Koordinator:** koordinator@itu.edu.tr  
        **Bina Sorumlusu:** bina@itu.edu.tr  
        **Ogrenci:** ogrenci@itu.edu.tr  
        
        Tum sifreler: **1234**
        """)

else:
    # Sidebar - kullanici bilgisi ve cikis
    with st.sidebar:
        st.markdown(f"### 👤 {st.session_state.user_name}")
        role_labels = {
            "club_admin": "Kulup Yoneticisi",
            "advisor": "Danisman",
            "coordinator": "Koordinator",
            "building_mgr": "Bina Sorumlusu",
            "student": "Ogrenci"
        }
        st.caption(role_labels.get(st.session_state.user_role, ""))
        if st.session_state.user_club:
            st.caption(f"🏢 {st.session_state.user_club}")
        st.divider()
        if st.button("Cikis Yap", use_container_width=True):
            logout()
            st.rerun()
    
    st.title("🏫 ClubSpace ITU")
    st.success(f"Hos geldiniz, {st.session_state.user_name}! Sol menuden sayfalara erisebilirsiniz.")
    
    # Basit istatistikler
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Toplam Etkinlik", "24")
    col2.metric("Onay Bekleyen", "3")
    col3.metric("Bu Ayki Etkinlik", "8")
    col4.metric("Aktif Kulup", "12")
