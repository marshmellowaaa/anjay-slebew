import streamlit as st
import folium
import random
import networkx as nx
from streamlit_folium import folium_static

# ---- MENU ----
menu = st.sidebar.radio("Pilih Menu", ["Home", "Graph Visualization", "Peta Koneksi Jawa Barat", "Isi Foto"])

# ---- MENU 1: HOME ----
if menu == "Home":
    st.title("Home - Profil")
    st.subheader("Selamat datang di aplikasi Streamlit!")

    # Data statis pengguna
    nama = "Falah"
    student_id = "12345"
    # URL gambar dari GitHub
    foto_profil_url = "https://raw.githubusercontent.com/username/repository-name/branch-name/foto_profil.jpg"

    # Tampilkan profil
    st.write(f"**Nama:** {nama}")
    st.write(f"**Student ID:** {student_id}")

    # Tampilkan foto menggunakan URL
    st.image(foto_profil_url, caption="Foto Profil", use_column_width=True)

# ---- MENU 2: GRAPH VISUALIZATION ----
elif menu == "Graph Visualization":
    st.title("Graph Visualization")
    st.subheader("Visualisasi Graph dengan Random Edges")

    # Input jumlah node dan edge
    num_nodes = st.number_input("Masukkan jumlah node", min_value=2, max_value=100, value=5)
    num_edges = st.number_input("Masukkan jumlah edge", min_value=1, max_value=100, value=5)

    # Generate graph
    G = nx.Graph()
    G.add_nodes_from(range(num_nodes))

    for _ in range(num_edges):
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)
        if u != v:
            G.add_edge(u, v)

    # Visualisasi graph
    st.write("**Graph yang dihasilkan:**")
    pos = nx.spring_layout(G)
    st.pyplot(nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=500, edge_color="gray"))

# ---- MENU 3: PETA KONEKSI JAWA BARAT ----
elif menu == "Peta Koneksi Jawa Barat":
    st.title("Peta Koneksi Provinsi Jawa Barat")
    st.subheader("Peta ini menampilkan koneksi antar kota besar di Jawa Barat.")

    # Data kota di Jawa Barat
    kota = {
        "Bandung": (-6.914744, 107.609810),
        "Bekasi": (-6.238270, 107.007310),
        "Bogor": (-6.595038, 106.816635),
        "Depok": (-6.402484, 106.794243),
        "Cirebon": (-6.706924, 108.555994),
        "Tasikmalaya": (-7.327383, 108.220688),
        "Sukabumi": (-6.921950, 106.927390),
        "Garut": (-7.204750, 107.882610),
    }

    # Koneksi antar kota
    koneksi = [
        ("Bandung", "Bekasi"),
        ("Bandung", "Bogor"),
        ("Bandung", "Garut"),
        ("Bogor", "Depok"),
        ("Depok", "Bekasi"),
        ("Tasikmalaya", "Garut"),
        ("Cirebon", "Tasikmalaya"),
        ("Cirebon", "Sukabumi"),
    ]

    # Buat peta
    peta = folium.Map(location=[-6.9, 107.6], zoom_start=8)

    # Tambahkan marker untuk kota
    for nama, (lat, lon) in kota.items():
        folium.Marker(location=[lat, lon], popup=nama, tooltip=nama).add_to(peta)

    # Tambahkan garis koneksi
    for (kota1, kota2) in koneksi:
        lokasi1 = kota[kota1]
        lokasi2 = kota[kota2]
        folium.PolyLine([lokasi1, lokasi2], color="blue", weight=2.5, tooltip=f"{kota1} - {kota2}").add_to(peta)

    # Tampilkan peta
    folium_static(peta)

# ---- MENU 4: ISI FOTO ----
elif menu == "Isi Foto":
    st.title("Isi Foto")
    st.subheader("Unggah dan tampilkan foto Anda.")

    # Upload foto
    uploaded_file = st.file_uploader("Pilih file gambar Anda", type=["jpg", "jpeg", "png"])

    # Tampilkan foto jika ada
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Gambar yang diunggah", use_column_width=True)
    else:
        st.write("Belum ada gambar yang diunggah.")
