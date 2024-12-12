import folium

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
    "Probolinggo": (-7.717508, 113.204239)
}

def buat_peta(kota, koneksi):
    # Create map centered on East Java
    peta = folium.Map(location=[-7.8, 112.6], zoom_start=8)
    
    # Add markers for each city
    for nama, (lat, lon) in kota.items():
        folium.Marker(
            location=[lat, lon], 
            popup=nama, 
            tooltip=nama
        ).add_to(peta)
    
    # Add connections between cities
    for (kota1, kota2) in koneksi:
        lokasi1 = kota[kota1]
        lokasi2 = kota[kota2]
        folium.PolyLine(
            [lokasi1, lokasi2], 
            color="blue", 
            weight=2.5, 
            tooltip=f"{kota1} - {kota2}"
        ).add_to(peta)
    
    return peta

def input_koneksi(kota):
    # Predefined connections for all cities
    koneksi = [
        # Create a network connecting all cities
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
        ("Probolinggo", "Jember")
    ]
    
    return koneksi

if __name__ == "__main__":
    print("Kota yang tersedia:", ", ".join(kota.keys()))
    
    # Get connections
    koneksi = input_koneksi(kota)
    
    # Create and save the map
    peta = buat_peta(kota, koneksi)
    peta.save("peta_koneksi_jawa_timur.html")
    
    print("Peta telah disimpan sebagai 'peta_koneksi_jawa_timur3.html'. Buka file tersebut di browser Anda.")