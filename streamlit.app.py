import streamlit as st
from PIL import Image
import pandas as pd

# Session state untuk menyimpan preferensi
if 'font_size' not in st.session_state:
    st.session_state.font_size = 15
if 'language' not in st.session_state:
    st.session_state.language = "Indonesia"
if 'theme' not in st.session_state:
    st.session_state.theme = "Terang"  # Default tema

# Fungsi untuk mengubah tema
def toggle_theme():
    if st.session_state.theme == "Terang":
        st.session_state.theme = "Gelap"
    else:
        st.session_state.theme = "Terang"

# Konfigurasi tema berdasarkan session state
if st.session_state.theme == "Terang":
    primaryColor = "#ff0000"
    backgroundColor = "#FFFFFF"
    secondaryBackgroundColor = "#F0F2F6"
    textColor = "#000000"
else:
    primaryColor = "#ff0000"
    backgroundColor = "#000000"
    secondaryBackgroundColor = "#000000"
    textColor = "#ffffff"

# Konfigurasi tampilan dinamis
st.markdown(
    f"""
    <style>
        /* Mengatur ukuran font global */
        html, body, .stApp, .stMarkdown, .stButton>button, .stTextInput>input, .stSelectbox>select, .stSlider>div, .stExpander>div, .stHeader, .stTitle, .stSubheader, .stAlert, .stTable, .stDataFrame, .stWrite {{
            font-size: {st.session_state.font_size}px !important;
        }}
        body {{
            background-color: {backgroundColor};
            color: {textColor};
        }}
        .stApp {{
            background-color: {backgroundColor};
            color: {textColor};
        }}
        .stSidebar {{
            background-color: {secondaryBackgroundColor};
        }}
        .stButton>button {{
            background-color: {primaryColor};
            color: white;
        }}
        .stExpander > div {{
            background-color: {secondaryBackgroundColor};
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar untuk navigasi dan toggle tema
with st.sidebar:
    st.header("Navigasi")
    nav_options = ["Beranda", "Kontak", "Pengaturan"]
    selected_nav = st.radio("Pilih Halaman:", nav_options)

    # Toggle tema di sidebar
    st.markdown("---")  # Garis pemisah
    st.write("*Tema Aplikasi*")
    if st.button("🌙 Gelap" if st.session_state.theme == "Terang" else "☀ Terang"):
        toggle_theme()
        st.rerun()  # Memuat ulang aplikasi untuk menerapkan tema baru

# Konten berdasarkan navigasi yang dipilih
if selected_nav == "Beranda":
    # Judul dengan format HTML
    judul = "<b><i>ramaaisyah.corp</i></b>" if st.session_state.language == "Indonesia" else "<b><i>ramaaisyah Corp</i></b>"
    st.markdown(f"<h1 style='text-align: center; color: {primaryColor};'>{judul}</h1>", unsafe_allow_html=True)

    # Deskripsi perusahaan
    deskripsi = "Pengembangan Aplikasi dan Layanan Digital" if st.session_state.language == "Indonesia" else "Digital Application and Services Development"
    st.markdown(f"<h3 style='text-align: center;'>{deskripsi}</h3>", unsafe_allow_html=True)

    # Tab layout untuk konten utama
    tab_titles = ["Tentang Perusahaan", "Layanan"] if st.session_state.language == "Indonesia" else ["About Company", "Services"]
    tabs = st.tabs(tab_titles)

    # Tab 1: Tentang Perusahaan
    with tabs[0]:
        header_text = "Tentang Perusahaan" if st.session_state.language == "Indonesia" else "About Company"
        st.header(header_text)
        
        # Gambar perusahaan
        try:
            image = Image.open("C:\\Users\\ramaprayoga\\Downloads\\corp.jpg")
            st.image(image, caption="Foto Perusahaan")
        except FileNotFoundError:
            st.error("Gambar perusahaan tidak ditemukan" if st.session_state.language == "Indonesia" else "Company image not found")
        
        # Grafik pertumbuhan perusahaan
        st.subheader("📈 Pertumbuhan Perusahaan" if st.session_state.language == "Indonesia" else "📈 Company Growth")
        growth_data = {
            'Tahun': [2023, 2024, 2025],
            'Pengguna': [100, 1500, 4500],
            'Pendapatan (Juta)': [50, 750, 2500]
        }
        df = pd.DataFrame(growth_data)
        st.area_chart(df.set_index('Tahun'))
        
        company_desc = """
        Perusahaan ini berdiri pada tahun 2024 dan saat ini sedang dalam tahap 
        pengembangan aplikasi dan layanan digital
        """ if st.session_state.language == "Indonesia" else """
        The company was established in 2024 and is currently in the stage of 
        developing applications and digital services
        """
        st.write(company_desc)

        history_title = "📜 Sejarah Perusahaan" if st.session_state.language == "Indonesia" else "📜 Company History"
        with st.expander(history_title):
            history_text = """
            ramaaisyah.corp didirikan pada 8 Juni 2024 oleh Rama Prayoga dan Aisyah Rahma. 
            Perusahaan ini bermula dari visi untuk memberikan solusi teknologi inovatif yang dapat 
            meningkatkan kualitas hidup masyarakat.
            """ if st.session_state.language == "Indonesia" else """
            ramaaisyah.corp was founded in 8 June 2024 by Rama Prayoga and Aisyah Rahma. 
            The company started with the vision to provide innovative technology solutions 
            that can improve people's quality of life.
            """
            st.write(history_text)

        event_header = "📅 Event Perusahaan (2024-2025)" if st.session_state.language == "Indonesia" else "📅 Company Events (2024-2025)"
        st.header(event_header)
        
        tahun_event = st.slider(
            "Pilih Tahun Event:" if st.session_state.language == "Indonesia" else "Select Year:", 
            2024, 2025, 2024
        )

        if tahun_event == 2024:
            event_text = "Seminar Nasional (Juni 2024)" if st.session_state.language == "Indonesia" else "National Seminar (June 2024)"
            seminar_nasional = st.checkbox(event_text)
            if seminar_nasional:
                desc = "Acara ini akan membahas tren terbaru dalam pengembangan aplikasi dan AI." if st.session_state.language == "Indonesia" else "This event will discuss the latest trends in application and AI development."
                st.write(f"- {event_text}: {desc}")

        elif tahun_event == 2025:
            event_text = "Pelatihan (Agustus 2025)" if st.session_state.language == "Indonesia" else "Training (August 2025)"
            pelatihan = st.checkbox(event_text)
            if pelatihan:
                desc = "Program pelatihan intensif untuk pengembangan aplikasi mobile dan web." if st.session_state.language == "Indonesia" else "Intensive training program for mobile and web application development."
                st.write(f"- {event_text}: {desc}")

    # Tab 2: Layanan
    with tabs[1]:
        services_header = "Layanan" if st.session_state.language == "Indonesia" else "Services"
        st.header(services_header)
        
        layanan_data = {
            "Layanan": ["Pengembangan Aplikasi Mobile", "Pengembangan Aplikasi Web", "Data Analysis", "AI Development"],
            "Deskripsi": [
                "Membangun aplikasi mobile" if st.session_state.language == "Indonesia" else "Mobile app development",
                "Membangun aplikasi web" if st.session_state.language == "Indonesia" else "Web app development",
                "Analisis data" if st.session_state.language == "Indonesia" else "Data analysis",
                "Pengembangan AI" if st.session_state.language == "Indonesia" else "AI development"
            ]
        }
        st.table(layanan_data)

# Halaman Kontak
elif selected_nav == "Kontak":
    contact_header = "Kontak" if st.session_state.language == "Indonesia" else "Contact"
    st.header(contact_header)
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("Rama Prayoga"):
            try:
                image = Image.open("C:\\Users\\ramaprayoga\\Downloads\\rama.jpg")
                st.image(image, width=200)
            except FileNotFoundError:
                st.error("Gambar tidak ditemukan" if st.session_state.language == "Indonesia" else "Image not found")
            
            st.markdown("<h3 style='text-align: center;'>Rama Prayoga</h3>", unsafe_allow_html=True)
            
            # Hobi dan Pendidikan
            st.write("*Hobi:" if st.session_state.language == "Indonesia" else "Hobbies:*")
            st.write("- Programming\n- Musik\n- Olahraga")
            
            st.write("*Pendidikan:" if st.session_state.language == "Indonesia" else "Education:*")
            pendidikan = [
                "MI Muhammadiyah 04 Paciran",
                "SMP Muhammadiyah 15 Brondong",
                "SMA Muhammadiyah 09 Brondong",
                "Universitas Muhammadiyah Surabaya"
            ]
            for sekolah in pendidikan:
                st.write(f"- {sekolah}")
            
            st.markdown(f"""
                <p style='text-align: center;'>
                    <a href='https://www.instagram.com/ramaprayog/' target='_blank'>
                        <img src='https://img.icons8.com/ios/30/{textColor[1:]}/instagram-new.png' alt='Instagram'/>
                    </a>&emsp;
                    <a href='https://open.spotify.com/user/a4un84ncm7grjbjoertrnumq0' target='_blank'>
                        <img src='https://img.icons8.com/ios/30/{textColor[1:]}/spotify.png' alt='Spotify'/>
                    </a>&emsp;
                    <a href='https://t.me/ramaprayoga' target='_blank'>
                        <img src='https://img.icons8.com/ios/30/{textColor[1:]}/telegram-app.png' alt='Telegram'/>
                    </a>
                </p>
            """, unsafe_allow_html=True)
    
    with col2:
        with st.expander("Aisyah Rahma"):
            try:
                image = Image.open("C:\\Users\\ramaprayoga\\Downloads\\aisyah.jpg")
                st.image(image, width=200)
            except FileNotFoundError:
                st.error("Gambar tidak ditemukan" if st.session_state.language == "Indonesia" else "Image not found")
            
            st.markdown("<h3 style='text-align: center;'>Aisyah Rahma</h3>", unsafe_allow_html=True)
            
            # Hobi dan Pendidikan
            st.write("*Hobi:" if st.session_state.language == "Indonesia" else "Hobbies:*")
            st.write("- Membaca\n- Shopping\n- Traveling")
            
            st.write("*Pendidikan:" if st.session_state.language == "Indonesia" else "Education:*")
            pendidikan = [
                "SD Muhammadiyah 22 Surabaya",
                "SMP Negeri 16 Surabaya",
                "SMK Negeri 05 Surabaya",
                "Universitas Muhammadiyah Surabaya"
            ]
            for sekolah in pendidikan:
                st.write(f"- {sekolah}")
            
            st.markdown(f"""
                <p style='text-align: center;'>
                    <a href='https://www.instagram.com/aisyamhr_/' target='_blank'>
                        <img src='https://img.icons8.com/ios/30/{textColor[1:]}/instagram-new.png' alt='Instagram'/>
                    </a>&emsp;
                    <a href='https://open.spotify.com/user/0anlon1ls7al9z39qdaf3cd09' target='_blank'>
                        <img src='https://img.icons8.com/ios/30/{textColor[1:]}/spotify.png' alt='Spotify'/>
                    </a>&emsp;
                    <a href='https://t.me/aisyamhr' target='_blank'>
                        <img src='https://img.icons8.com/ios/30/{textColor[1:]}/telegram-app.png' alt='Telegram'/>
                    </a>
                </p>
            """, unsafe_allow_html=True)

# Halaman Pengaturan
elif selected_nav == "Pengaturan":
    settings_header = "Pengaturan" if st.session_state.language == "Indonesia" else "Settings"
    st.header(settings_header)
    
    bahasa = st.selectbox(
        "Pilih Bahasa" if st.session_state.language == "Indonesia" else "Select Language",
        ["Indonesia", "English"]
    )
    
    ukuran_font = st.slider(
        "Ukuran Font" if st.session_state.language == "Indonesia" else "Font Size",
        10, 30, st.session_state.font_size
    )
    
    if st.button("Simpan Preferensi" if st.session_state.language == "Indonesia" else "Save Preferences"):
        st.session_state.language = bahasa
        st.session_state.font_size = ukuran_font
        st.success("Preferensi disimpan!" if st.session_state.language == "Indonesia" else "Preferences saved!")
