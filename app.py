import streamlit as st

st.set_page_config(page_title="Aplikasi Multi-Page", layout="wide")
st.title("Selamat Datang di Aplikasi Multi-Page Streamlit")
st.write("Silakan pilih menu di sidebar untuk berpindah halaman.")
import streamlit as st
import numpy as np
import pandas as pd

#Menambahkan Judul
st.title("Welcome to my Sreamlit!!!")

import streamlit as st

st.title('Selamat Datang di Aplikasi Streamlit saya!')
st.header('Bagian 1: Pendahuluan')
st.subheader('Subbagian 1: Data')
st.caption('Ini adalah data.')
st.code('import pandas as pd')
st.text('Dan ini adalah teks biasa tanpa format atau penekanan.')
st.latex(r' y = mx + b ')
st.markdown('**Teks Tebal** dan _Teks Miring_ serta [Tautan](https://streamlit.io)')
st.divider()

#Menambahkan Paragraf
st.write("Berikut adalah data singkat beberapa teman saya")

data = {
    'Nama': ['Hikma', 'zalfa', 'Nia', 'Hilma', 'Berli'],
    'Usia': ['19', '19', '20', '19', '18' ],
    'Kota/Kab.':['Gowa', 'Makassar', 'Kalimantan', 'Makassar', 'Makassar']
} 
df = pd.DataFrame(data)
st.write(df)


import streamlit as st
import requests
import pandas as pd

st.title('Data dari API')

url = 'https://jsonplaceholder.typicode.com/users'  # API contoh
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.dataframe(df)
    print(data)
else:
    st.error('Gagal mengambil data dari API')

uploaded_file = st.file_uploader("Pilih file CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
else:
    st.write("")

import streamlit as st
import pandas as pd

# Data sederhana
data = {
    'Nama': ['Hikma', 'Husna', 'Natasya'],
    'Umur': [19, 19, 19],
    'Kota/Kab.': ['Gowa', 'Enrekang', 'Manado']
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menampilkan DataFrame
st.write("Tabel Data:")
st.write(df)

import streamlit as st
import pandas as pd
import numpy as np

# Membuat DataFrame random dengan 10 baris dan 5 kolom
df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

# Menampilkan DataFrame di Streamlit
st.dataframe(df)

import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Omset", value="Rp 500 Juta", delta="+5%")
with col2:
    st.metric(label="User Aktif", value="1.200", delta="+2%")
with col3:
    st.metric(label="Refund", value="15", delta="-1%")

col1, col2 = st.columns(2)

import streamlit as st
import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.randn(300, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(data)

st.bar_chart(data)

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)
chart = alt.Chart(data.reset_index()).mark_line().encode(
    x='index',
    y='a'
)

st.altair_chart(chart, use_container_width=True)

import streamlit as st
import pandas as pd
import numpy as np

# Membuat DataFrame dengan 100 titik koordinat acak di sekitar Jakarta
data = pd.DataFrame({
    'lat': -6.2 + np.random.rand(100) * 0.1,   # Latitude sekitar Jakarta
    'lon': 106.8 + np.random.rand(100) * 0.1   # Longitude sekitar Jakarta
})

st.map(data)

import streamlit as st
import plotly.express as px
import pandas as pd
import streamlit as st
st.title("📊 Dashboard Penjualan 5 Tahun")

data = pd.DataFrame({
    'Tahun': [2018, 2019, 2020, 2021, 2022],
    'Penjualan': [100, 120, 90, 140, 180],
    'Laba': [20, 30, 15, 35, 50]
})

fig_penjualan = px.line(
    data,
    x='Tahun',
    y='Penjualan',
    markers=True,
    text='Penjualan',
    title="📈 Tren Penjualan Tiap Tahun",
    labels={'Penjualan': 'Jumlah Penjualan', 'Tahun': 'Tahun'},
    template='plotly_white'  # tampilan lebih bersih
)
fig_penjualan.update_traces(textposition="top center")
fig_penjualan.update_layout(title_x=0.5)

fig_laba = px.bar(
    data,
    x='Tahun',
    y='Laba',
    color='Tahun',
    title="💰 Laba Tahunan",
    labels={'Laba': 'Jumlah Laba'},
    template='plotly_dark'  # tema gelap
)
fig_laba.update_layout(title_x=0.5)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig_penjualan, use_container_width=True)

with col2:
    st.plotly_chart(fig_laba, use_container_width=True)

st.divider()
st.caption('Dibuat dengan ❤️ menggunakan Streamlit dan Plotly')


import streamlit as st

with st.form("form_input"):
    nama = st.text_input("Nama")
    alamat = st.text_area("Alamat")
    usia = st.number_input("Usia", min_value=0)
    tanggal_lahir = st.date_input("Tanggal Lahir")
    waktu_janji = st.time_input("Waktu Janjian")
    jenis_kelamin = st.radio("Jenis Kelamin", ("Pria", "Wanita"))
    hobi = st.multiselect("Hobi", ["Membaca", "Olahraga", "Musik", "Traveling"])
    warna_favorit = st.color_picker("Pilih warna favorit")
    file_foto = st.file_uploader("Upload Foto")
    foto_kamera = st.camera_input("Ambil foto dari Kamera")
    rating = st.slider("Rating Kepuasan", 1, 10)
    submitted = st.form_submit_button("Kirim Data")

if submitted:
    st.success(f"Data {nama} berhasil dikirim!")

import streamlit as st
from PIL import Image

import streamlit as st

st.image(
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=600&q=80",
    caption="Ilustrasi Artificial Intelligence",
    use_container_width=True
)

import streamlit as st
# Menampilkan video dari URL (contoh: YouTube)
st.video('https://www.youtube.com/watch?v=2Ji-clqUYnA')

import streamlit as st
# Menampilkan audio dari URL
st.audio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3')

import streamlit as st

# Upload file
uploaded_file = st.file_uploader("Pilih file PDF atau CSV", type=['pdf', 'csv'])

if uploaded_file is not None:
    st.write("File berhasil di-upload:")
    st.write(uploaded_file.name)
    st.download_button("Unduh file", uploaded_file)

import streamlit as st
from PyPDF2 import PdfReader

# Menampilkan PDF
uploaded_pdf = st.file_uploader("Pilih file PDF", type=["pdf"])

if uploaded_pdf is not None:
    reader = PdfReader(uploaded_pdf)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    st.write(text)

import streamlit as st

# Menampilkan HTML langsung
html_code = """
<h1>Selamat datang di Aplikasi Streamlit!</h1>
<p>Ini adalah <strong>paragraf</strong> HTML yang dapat diproses oleh Streamlit.</p>
"""
st.markdown(html_code, unsafe_allow_html=True)


import streamlit as st
from PIL import Image

import streamlit as st

import streamlit as st

# Membuat dua kolom
col1, col2 = st.columns(2)

# Menampilkan konten di kolom pertama
with col1:
    st.header("Kolom Pertama")
    st.write("konten di kolom pertama.")
    st.button("Pertama")

# Menampilkan konten di kolom kedua
with col2:
    st.header("Kolom Kedua")
    st.write("konten di kolom kedua.")
    st.button("Kedua")

import streamlit as st

with st.expander("Klik untuk melihat lebih banyak"):
    st.write("konten tersembunyi yang bisa dilihat saat pengguna klik expander.")
    st.image("https://via.placeholder.com/150", caption="Gambar")

import streamlit as st

# Membuat container
container = st.container()

# Menambahkan elemen ke dalam container
with container:
    st.header("Konten di dalam Container")
    st.write("elemen-elemen yang ada dalam container.")
    st.button("Container")

import streamlit as st

# Menambahkan elemen ke Sidebar
st.sidebar.header("Konten")
st.sidebar.radio("Pilih Opsi", ["Opsi 1", "Opsi 2", "Opsi 3"])

# Konten utama
st.title("Konten Utama")
st.write("konten utama yang ditampilkan di layar.")


import streamlit as st

# Menambahkan elemen navigasi di Sidebar
st.sidebar.header("Navigasi")
selection = st.sidebar.radio("Pilih Halaman", ["Beranda", "Tentang", "Kontak"])

# Konten berdasarkan pilihan
if selection == "Beranda":
    st.title("Beranda")
    st.write("halaman beranda.")
elif selection == "Tentang":
    st.title("Tentang")
    st.write("halaman tentang.")
else:
    st.title("Kontak")
    st.write("halaman kontak.")

# Menambahkan elemen navigasi dengan dropdown di Sidebar
st.sidebar.header("Navigasi")
selection = st.sidebar.selectbox("Pilih Halaman", ["Beranda", "Tentang", "Galeri", "Kontak"])

# Konten berdasarkan pilihan
if selection == "Beranda":
    st.title("Beranda")
    st.write("halaman beranda.")
elif selection == "Tentang":
    st.title("Tentang")
    st.write("halaman tentang.")
elif selection == "Galeri":
    st.title("Galeri")
    st.write("Ihalaman galeri.")
else:
    st.title("Kontak")
    st.write("halaman kontak.")

# Menambahkan tombol untuk navigasi di Sidebar
st.sidebar.header("Navigasi")
if st.sidebar.button("Beranda"):
    st.title("Beranda")
    st.write("halaman beranda.")
elif st.sidebar.button("Tentang"):
    st.title("Tentang")
    st.write("halaman tentang.")
elif st.sidebar.button("Kontak"):
    st.title("Kontak")
    st.write("halaman kontak.")

# Menambahkan tautan navigasi di Sidebar
st.sidebar.header("Navigasi")
st.sidebar.markdown("[Beranda](#beranda)")
st.sidebar.markdown("[Tentang](#tentang)")
st.sidebar.markdown("[Kontak](#kontak)")

# Konten halaman berdasarkan tautan
st.title("Beranda")
st.write("halaman beranda.")

st.title("Tentang")
st.write("halaman tentang.")

st.title("Kontak")
st.write("halaman kontak.")


