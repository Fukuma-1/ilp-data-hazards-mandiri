# Implementasi Data Hazards ILP — Tugas Mandiri

## Isi proyek
- `ilp_hazards.py`: simulator Python sederhana untuk RAW, WAR, dan WAW.
- `ILP_Data_Hazards_Mandiri.ipynb`: notebook untuk Google Colab.
- `Laporan_ILP_Data_Hazards.pdf`: laporan berisi dependency graph dan analisis.
- `sample_output.txt`: contoh hasil eksekusi program.

## Menjalankan
Jalankan `python ilp_hazards.py` dengan Python 3, atau unggah notebook ke Google Colab dan pilih Runtime → Run all.

## Contoh
- RAW: I1 menulis R1, lalu I2 membaca R1.
- WAR: I1 membaca R2, lalu I2 menulis R2.
- WAW: I1 dan I2 menulis R1.

WAR dan WAW pada contoh ini adalah name dependence yang dapat diatasi dengan register renaming. RAW merupakan true data dependence.

## GitHub
Buat repository bernama `ilp-data-hazards-mandiri`, lalu unggah file proyek. Tambahkan URL repository asli pada laporan setelah repository berhasil dibuat.
