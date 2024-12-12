import networkx as nx
import folium

# 1. Representasi graf untuk kota-kota di Jawa Timur
# Daftar kota dan koordinat geografisnya
kota_jawa_timur = {
    "Blitar": [-8.0954, 112.1603],
    "Kediri": [-7.848, 112.017],
    "Madiun": [-7.629, 111.523],
    "Malang": [-7.9839, 112.6214],
    "Batu": [-7.867, 112.523],
    "Mojokerto": [-7.472, 112.438],
    "Pasuruan": [-7.645, 112.907],
    "Probolinggo": [-7.75, 113.216]
}

# Koneksi antar kota
koneksi_kota = [
    ("Blitar", "Kediri"),
    ("Kediri", "Madiun"),
    ("Malang", "Blitar"),
    ("Malang", "Batu"),
    ("Batu", "Mojokerto"),
    ("Mojokerto", "Pasuruan"),
    ("Pasuruan", "Probolinggo")
]

# Membuat graf dengan NetworkX
G = nx.Graph()
G.add_nodes_from(kota_jawa_timur.keys())
G.add_edges_from(koneksi_kota)

# 2. Membuat peta menggunakan Folium
peta = folium.Map(location=[-7.8, 112.5], zoom_start=8)

# Menambahkan marker untuk setiap kota
for kota, koordinat in kota_jawa_timur.items():
    folium.Marker(location=koordinat, popup=kota, tooltip=kota).add_to(peta)

# Menambahkan garis untuk koneksi antar kota
for kota1, kota2 in koneksi_kota:
    koordinat1 = kota_jawa_timur[kota1]
    koordinat2 = kota_jawa_timur[kota2]
    folium.PolyLine([koordinat1, koordinat2], color="blue", weight=2.5, tooltip=f"{kota1} - {kota2}").add_to(peta)

# Menyimpan peta ke file HTML
peta.save("peta_koneksi_jawa_timur5.html")
print("Peta telah disimpan sebagai 'peta_koneksi_jawa_timur.html'. Buka file tersebut di browser Anda.")

# 3. Representasi Graf: Adjacency List, Adjacency Matrix, dan Edge List
print("Adjacency List:")
for node, neighbors in dict(G.adjacency()).items():
    print(f"{node}: {list(neighbors.keys())}")

print("\nAdjacency Matrix:")
print(nx.adjacency_matrix(G).toarray())

print("\nEdge List:")
print(list(G.edges))

# 4. Contoh Aplikasi Graph Theory
# Dijkstra's Algorithm untuk menemukan jalur terpendek
shortest_path = nx.dijkstra_path(G, source="Blitar", target="Probolinggo")
print("\nJalur Terpendek dari Blitar ke Probolinggo:", shortest_path)

# Algoritma Greedy untuk Graph Coloring
graph_coloring = nx.greedy_color(G)
print("\nGraph Coloring (Pewarnaan Graf):", graph_coloring)

# 5. Informasi tambahan tentang Streamlit dan penggunaan GitHub
print("\nStreamlit adalah library Python untuk membangun aplikasi web interaktif.")
print("Streamlit Community Cloud adalah platform untuk mendistribusikan aplikasi Streamlit.")
print("\nUntuk mengunggah file ke GitHub, buat repository dan gunakan perintah git untuk push file.")

# 6. Catatan untuk pengumpulan laporan
print("\nSimpan laporan dengan format berikut:")
print("- Nama file Word: groupname.docx")
print("- File Python: groupname-repor2no6.py dan groupname-repor2no7.py")
