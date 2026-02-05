import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Baca file CSV (karena pakai koma, tidak perlu sep=';')
data = pd.read_csv('nilai_siswa.csv')

print("\n=== Nama Kolom dalam Dataset ===")
print(data.columns)

print("\n=== Info Dataset ===")
print(data.info())

print("\n=== 5 Data Pertama ===")
print(data.head())

print("\n=== Statistik Deskriptif ===")
print(data.describe())

print("\n=== Statistik Nilai ===")
print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])
print("Nilai maksimum:", data['Nilai'].max())
print("Nilai minimum:", data['Nilai'].min())

# 2. Nilai per mata pelajaran
print("\n=== Nilai per Mata Pelajaran ===")
for mapel in data['Matpel'].unique():
    print(f"\n{mapel}:")
    print(data[data['Matpel'] == mapel])

# 3. Nilai maksimum dan minimum per mapel
print("\n=== Nilai Maksimum & Minimum per Mapel ===")
print(data.groupby('Matpel')['Nilai'].agg(['max', 'min']))

# 4. Grafik batang rata-rata nilai per mapel
rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar', color='skyblue')
plt.title('Rata-Rata Nilai per Mapel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

# 5. Boxplot sebaran nilai per mapel
sns.boxplot(x='Matpel', y='Nilai', data=data)
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.show()
