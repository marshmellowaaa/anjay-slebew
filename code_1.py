import folium
import streamlit as st
from streamlit import components

# Data kota di Jawa Timur
kota = {
    "Surabaya": (-7.250445, 112.768845),
    "Malang": (-7.966620, 112.632629),
    "Blitar": (-8.095603, 112.160713),
    "Madiun": (-7.629081, 111.523098),
    "Jember": (-8.172040, 113.700361),
    "Kediri": (-7.820049, 112.010664),
    "Batu": (-7.870921, 112.530411),
    "Mojokerto": (-7.474373, 112.437528),
    "Pasuruan": (-7.642643, 112.900128),
    "Probolinggo": (-7.717508, 113.204239),
}

# Fungsi membuat peta
def buat_peta(kota, koneksi):
    peta = folium.Map(location=[-7.8, 112.6], zoom_start=8)
    for nama, (lat, lon) in kota.items():
        folium.Marker(location=[lat, lon], popup=nama, tooltip=nama).add_to(peta)
    for (kota1, kota2) in koneksi:
        lokasi1 = kota[kota1]
        lokasi2 = kota[kota2]
        folium.PolyLine([lokasi1, lokasi2], color="blue", weight=2.5, tooltip=f"{kota1} - {kota2}").add_to(peta)
    return peta

# Koneksi antar kota
def input_koneksi():
    koneksi = [
        ("Surabaya", "Malang"),
        ("Surabaya", "Mojokerto"),
        ("Surabaya", "Pasuruan"),
        ("Malang", "Batu"),
        ("Malang", "Blitar"),
        ("Blitar", "Kediri"),
        ("Kediri", "Madiun"),
        ("Madiun", "Mojokerto"),
        ("Mojokerto", "Pasuruan"),
        ("Pasuruan", "Probolinggo"),
        ("Probolinggo", "Jember"),
    ]
    return koneksi

# Streamlit Interface
st.title("Aplikasi Kota Jawa Timur")

# Sidebar untuk Menu
menu = st.sidebar.radio("Pilih Menu", ["Profile", "Grafik", "Peta"])

# Data Profile untuk 3 orang
profiles = {
    "Feriza Anggraeni": {
        "gambar": "feriza.jpg",  # Nama file gambar lokal
        "Nama": "Feriza",
        "Student ID" : "'021202400021'",
        "Hobi": "Menulis",
    },
    "Hana Arabella Liliana Sigalingging": {
        "gambar": "hanna.jpg",  # Nama file gambar lokal
        "Nama": "Hana",
        "Student ID" : "'021202400003'",
        "Hobi": "Menonton",
    },
    "Alexandra Mercy Christani": {
        "gambar": "mercy.jpg",  # Nama file gambar lokal
        "Nama": "Alexandra",
        "Student ID" : "'021202400008'",
        "Hobi": "Membaca",
    }
}

# Bagian Profile
if menu == "Profile":
    st.subheader("Profile")
    
    # Pilih salah satu profil
    profile_choice = st.selectbox("Pilih Profile", ["Feriza Anggraeni", "Hana Arabella Liliana Sigalingging", "Alexandra Mercy Christani"])

    # Tampilkan informasi profil yang dipilih
    profile = profiles[profile_choice]
    st.image(profile["gambar"], caption=profile["Nama"], width=150)
    st.write(f"Nama: {profile['Nama']}")
    st.write(f"Hobi: {profile['Hobi']}")
    st.write(f"Student ID: {profile['Student ID']}")

# Bagian Grafik (Untuk demo, menampilkan gambar grafik)
elif menu == "Grafik":
    st.subheader("Grafik")
    st.image("https://via.placeholder.com/600x300?text=Grafik+Di+Sini", caption="Grafik Contoh", use_column_width=True)

# Bagian Peta
elif menu == "Peta":
    st.subheader("Peta Koneksi Kota di Jawa Timur")
    st.write("Peta ini menampilkan koneksi antar kota besar di Jawa Timur.")

    # Ambil koneksi
    koneksi = input_koneksi()

    # Buat peta
    peta = buat_peta(kota, koneksi)

    # Simpan peta ke file HTML sementara
    peta.save("temp_peta.html")

    # Tampilkan peta di Streamlit
    with open("temp_peta.html", "r", encoding="utf-8") as file:
        peta_html = file.read()

    st.components.v1.html(peta_html, height=600)
