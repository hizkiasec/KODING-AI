<!-- 🎓 README.md | Project by Hizkia Agellvin Girsang -->

<h1 align="center">🌟📊 ANALISIS NILAI SISWA 📊🌟</h1>

<h3 align="center">👨‍💻 Hizkia Agellvin Girsang | XI RPL 3 👨‍💻</h3>

<p align="center">
  <img src="https://media.giphy.com/media/L8K62iTDkzGX6/giphy.gif" width="280" alt="coding animation"/>
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=yellow">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-green?style=for-the-badge&logo=pandas">
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-orange?style=for-the-badge&logo=plotly">
  <img src="https://img.shields.io/badge/Developer-Hizkia%20Agellvin%20Girsang-blueviolet?style=for-the-badge">
</p>

---

## 🧠 Tentang Proyek
**Analisis Nilai Siswa** adalah program Python interaktif yang menganalisis data nilai siswa menggunakan **Pandas** dan **Matplotlib**.  
Program ini membantu menemukan wawasan dari data siswa seperti:
- 📊 Statistik deskriptif (mean, median, modus, maksimum, minimum)
- 🧩 Nilai tertinggi & terendah per mata pelajaran
- 🎨 Visualisasi data interaktif dalam bentuk grafik

💡 Tujuannya adalah melatih pemahaman tentang **data science dasar**, serta menerapkan analisis data di dunia pendidikan.

<p align="center">
  <img src="https://media.giphy.com/media/ZVik7pBtu9dNS/giphy.gif" width="420" alt="Data Animation"/>
</p>

---

## ⚙️ Teknologi yang Digunakan
| Teknologi | Keterangan |
|------------|------------|
| 🐍 **Python 3.x** | Bahasa pemrograman utama |
| 📘 **Pandas** | Analisis dan manipulasi data |
| 📊 **Matplotlib** | Visualisasi data dalam bentuk grafik |
| 📄 **CSV File** | Format penyimpanan dataset nilai siswa |

---

## 📂 Struktur Dataset
| Kolom | Deskripsi |
|--------|------------|
| 🧑 `Nama` | Nama lengkap siswa |
| 📚 `Matpel` | Nama mata pelajaran |
| 🧾 `Nilai` | Nilai siswa dalam angka (0–100) |

📊 Jumlah data yang dianalisis: **22 baris**

---

## 🔍 Proses Analisis
1. Membaca dataset menggunakan `pandas.read_csv()`
2. Menampilkan struktur dan info kolom dataset
3. Menghitung **statistik deskriptif**: rata-rata, median, modus, nilai tertinggi & terendah
4. Mengelompokkan nilai berdasarkan **mata pelajaran**
5. Membuat **grafik batang & distribusi nilai** menggunakan `matplotlib.pyplot`

---

## 📈 Hasil Analisis
| Statistik | Nilai |
|------------|--------|
| **Rata-rata** | 86.32 |
| **Median** | 86.5 |
| **Modus** | 85 |
| **Nilai Maksimum** | 98 |
| **Nilai Minimum** | 75 |

---

## 🏫 Nilai Tertinggi & Terendah per Mapel
| Mata Pelajaran | 🔝 Tertinggi | 🔻 Terendah |
|----------------|--------------|-------------|
| Bahasa Indonesia | 88 | 75 |
| Bahasa Inggris | 90 | 78 |
| Fisika | 95 | 75 |
| Matematika | 98 | 85 |
| Produktif | 90 | 80 |

---

## 🎨 Visualisasi
<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTlmNjVjOTQ0ZjdiMmZmYWQ2MzkxMTI2MTZhNjM4ZWY3MTY4ZDA5ZCZjdD1n/PjeG2bHiBkqQ0/giphy.gif" width="250" alt="Chart Animation"/>
</p>

**Visualisasi yang dihasilkan:**
- Grafik distribusi nilai siswa  
- Grafik perbandingan rata-rata nilai antar mata pelajaran  
- Diagram batang untuk melihat variasi nilai  

---

## 💡 Insight & Kesimpulan
✨ Rata-rata nilai siswa **86.32**, menunjukkan performa belajar yang baik.  
📘 **Matematika** memiliki nilai tertinggi (**98**) dan konsistensi bagus.  
⚛️ **Fisika** menunjukkan variasi besar antara nilai tertinggi dan terendah, menandakan kesulitan relatif tinggi.  
📊 Sebagian besar nilai berada pada kisaran **85–90**, menunjukkan distribusi yang normal.  

---

## 🚀 Rencana Pengembangan
🔹 Menambahkan **fitur analisis tren nilai per siswa**  
🔹 Integrasi dengan **dashboard interaktif (Streamlit / Dash)**  
🔹 Export hasil analisis ke **PDF otomatis**  
🔹 Menambahkan **prediksi nilai** menggunakan *machine learning sederhana*  

---


