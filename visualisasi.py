import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
import warnings
warnings.filterwarnings('ignore')
                           

sns.set(style="whitegrid")

np.random.seed(18) #NIM 241524018

n_mhs = 150
data_informatika = {
    'Nama' : [f'Mahasiswa_{i}' for i in range(n_mhs)],
    'Nilai_Algoritma': np.random.normal(80, 8, n_mhs),
    'Nilai_Pemrograman' : np.random.normal(78, 10, n_mhs),
    'Jumlah_proyek' : np.random.randint(1, 10, n_mhs),
    'Semester' : np.random.randint(1, 8, n_mhs),
    'IPK' : np.random.uniform(2.8, 4.0, n_mhs),
    'Gender': np.random.choice(['Laki-laki','Perempuan'], n_mhs),
    'Umur' : np.random.randint(18, 25, n_mhs),
    'Kekayaan': np.random.uniform(10, 100, n_mhs),
    'Kebahagiaan': np.random.uniform(0, 100, n_mhs),
    'Kategori': np.random.choice(["Web Dev", "data Science", "AI", "Cybersecuri"], n_mhs)
}

df_informatika = pd.DataFrame(data_informatika)

n_pasien = 200
data_penyakit = {
    'ID_Pasien ': [f'Pasien_ {i}' for i in range ( n_pasien )],
    'Usia': np. random . randint (20 , 80, n_pasien ),
    'Tekanan_Darah': np. random . normal (120 , 15,n_pasien ),
    'Kadar_Gula': np. random . normal (100 , 20, n_pasien ),
    'Durasi_Rawat': np. random . randint (1, 15,n_pasien ),
    'Diagnosa': np. random . choice ([ 'Diabetes','Hipertensi', 'Jantungan', 'Normal'],n_pasien ),
    'Biaya': np. random . uniform (1000 , 10000 , n_pasien ),
    'Gender': np. random . choice ([ 'Laki - laki' ,'Perempuan'], n_pasien ),
    'IPK': np. random . uniform (2.0 , 4.0 , n_pasien ),
    'Kekayaan': np. random . uniform (50 , 500 , n_pasien ),
    'Kebahagiaan': np. random . uniform (0, 100 , n_pasien )
}
df_penyakit = pd. DataFrame(data_penyakit)

# 1. Seaborn Scatter Plot

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_informatika, x= 'IPK', y= 'Kebahagiaan', hue='Gender', size = 'Kekayaan', sizes =(20,200))
plt.title("Hubungan IPK dan Kebahagian Mahasiswa Informatika")
plt.savefig("scatter_informatika_ipk_kebahagiaan.png")
plt.close()


# 2. Seaborn box Plot

plt.figure(figsize=(10, 6))
sns.boxplot(data=df_informatika, x='Kategori', y = 'Kebahagiaan', hue = 'Gender' , palette='Set2')
plt.title("Distribusi Kebahagiaan Mahasiswa Informatika per Kategori")
plt.savefig('box_informatika_kebahagiaan.png')
plt.close()

# 3. Seaborn Heatmap (Penyakit)
plt.figure(figsize=(10, 8))
corr_penyakit = df_penyakit[['Usia', 'Tekanan_Darah', 'Kadar_Gula',
                             'Durasi_Rawat', 'Biaya', 'IPK',
                             'Kekayaan', 'Kebahagiaan']].corr()
sns.heatmap(corr_penyakit, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Korelasi Antar Variabel Pasien')
plt.savefig('heatmap_penyakit_korelasi.png')
plt.close()

# 4. Seaborn Bar Plot (Penyakit)
plt.figure(figsize=(10, 6))
sns.barplot(data=df_penyakit, x='Diagnosa', y='Kekayaan', hue='Gender', palette='muted')
plt.title('Rata-rata Kekayaan Pasien Berdasarkan Diagnosa dan Gender')
plt.savefig('bar_penyakit_kekayaan.png')
plt.close()

# 5. Bokeh Scatter Plot (Penyakit)
output_file('bokeh_scatter_penyakit_usia_kebahagiaan.html')
source_penyakit = ColumnDataSource(df_penyakit)

p1 = figure(title="Usia vs Kebahagiaan Pasien (Interaktif)",
            x_axis_label='Usia',
            y_axis_label='Kebahagiaan',
            tools="pan,box_zoom,reset,save")

p1.scatter('Usia', 'Kebahagiaan', source=source_penyakit,
           size=8, color=Spectral6[2],
           legend_label='Pasien', fill_alpha=0.6)

p1.legend.click_policy = "hide"
show(p1)


# 6. Bokeh Bar Plot (Informatika)
output_file('bokeh_bar_informatika_ipk.html')

ipk_kategori_gender = df_informatika.groupby(['Kategori', 'Gender'])['IPK'].mean().reset_index()
source_informatika = ColumnDataSource(ipk_kategori_gender)

p2 = figure(x_range=ipk_kategori_gender['Kategori'].unique(),
            title="Rata-rata IPK per Kategori dan Gender",
            x_axis_label='Kategori', y_axis_label='IPK',
            tools="pan,reset,save")

p2.vbar(x='Kategori', top='IPK', width=0.4,
        source=source_informatika, color=Spectral6[3],
        legend_label='IPK')

p2.legend.click_policy = "hide"
show(p2)

# 7. violinplot sebagai modifikasi tampilan
plt.figure(figsize=(8, 5))
sns.violinplot(data=df_penyakit, x='Diagnosa', y='Kadar_Gula',
               order=['Diabetes','Hipertensi', 'Jantungan', 'Normal'])
plt.title("Sebaran diagnosa penyakit Berdasarkan Kadar gula")
plt.savefig("violin_diagnosa_kadargula.png")
plt.close()

# =============================================
# ============== DATA SET CUSTOM ============== 
# =============================================

n_siswa_k12 = 200
data_siswa_k12 = {
    'ID_siswa ': [f'siswa_ {i}' for i in range ( n_siswa_k12 )],
    'Usia': np. random . randint (5 , 18, n_siswa_k12 ),
    'Nilai_Rapor': np. random . uniform (0 , 100 , n_siswa_k12 ),
    'Gender': np. random . choice (['Laki - laki' ,'Perempuan'], n_siswa_k12 ),
    'Prestasi': np. random . choice (['Sangat Baik','Baik', 'Cukup', 'Kurang', 'Buruk'],n_siswa_k12 ),
    'Dukungan_Orang_Tua': np. random . choice (['Sangat Baik','Baik', 'Cukup', 'Kurang', 'Buruk'],n_siswa_k12 ),
    'Durasi_Penggunaan_Gawai': np. random . uniform (0, 360 , n_siswa_k12 ),
    'Kebahagiaan': np. random . uniform (0, 100 , n_siswa_k12 )
}
df_siswa_k12 = pd. DataFrame(data_siswa_k12)
peta_dukungan_orang_tua = {'Sangat Baik' : 5,'Baik': 4, 'Cukup' : 3, 'Kurang' : 2, 'Buruk':1 }
peta_prestasi = {'Sangat Baik' : 5,'Baik': 4, 'Cukup' : 3, 'Kurang' : 2, 'Buruk':1 }
df_siswa_k12['Prestasi_Numerik'] = df_siswa_k12['Prestasi'].map(peta_prestasi)
df_siswa_k12['Dukungan_Orang_Tua_Numerik'] = df_siswa_k12['Dukungan_Orang_Tua'].map(peta_dukungan_orang_tua)

# 1. Visualisasi Scatter plot untuk menunjukan korelasi antara durasi gawai vs Nilai
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_siswa_k12, x='Durasi_Penggunaan_Gawai', y = 'Nilai_Rapor', hue = 'Gender' , size = 'Dukungan_Orang_Tua_Numerik', sizes =(10,100))
plt.title("Korelasi antara Durasi Penggunaan Gawai dengan Nilai Rapor")
plt.savefig("scatter_siswaK12_Rapor_DurasiGawai.png")
plt.close()

# 2. Seaborn Bar Plot untuk membandingkan nilai rata rata nilai Rapor berdasarkan dukungan orang tua dan gender
plt.figure(figsize=(10, 6))
sns.barplot(data=df_siswa_k12, x='Dukungan_Orang_Tua', y='Nilai_Rapor', hue='Gender', palette='muted')
plt.title('Rata-rata Nilai Rapor siswa K-12 Berdasarkan Dukungan Orang Tua dan Gender')
plt.savefig('bar_dukunganOrtu_Gender.png')
plt.close()

# 3. Seaborn Heatmap untuk korelasi antar variabel siswa K-12
plt.figure(figsize=(10, 8))
corr_siswa = df_siswa_k12[['Usia', 'Nilai_Rapor', 'Dukungan_Orang_Tua_Numerik',
                             'Prestasi_Numerik', 'Durasi_Penggunaan_Gawai', 'Kebahagiaan']].corr()
sns.heatmap(corr_siswa, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Korelasi Antar Variabel Siswa K-12')
plt.savefig('heatmap_Siswa_korelasi.png')
plt.close()

# 4. Custom Visualisasi durasi vs nilai
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_siswa_k12, x='Durasi_Penggunaan_Gawai', y = 'Nilai_Rapor', hue = 'Gender' , size = 'Prestasi_Numerik', sizes =(10,100), palette='Set2')
plt.title("Korelasi antara Durasi Penggunaan Gawai dengan Nilai Rapor")
plt.savefig("scatter_siswaK12_Rapor_Durasi_Gawai_Custom.png")
plt.close()

