# Tugas Praktikum 7: REST API WebGIS dengan FastAPI & PostGIS

Proyek ini adalah implementasi REST API untuk mengakses data spasial dari database PostGIS menggunakan FastAPI. Proyek ini telah disusun dengan struktur yang rapi dan memenuhi semua syarat tugas.

## 📁 Struktur Proyek
- `main.py`: Titik masuk aplikasi dan konfigurasi FastAPI.
- `database.py`: Konfigurasi koneksi database menggunakan `asyncpg`.
- `models.py`: Skema validasi data menggunakan Pydantic.
- `routers/fasilitas.py`: Implementasi semua endpoint (CRUD & Spasial).
- `.env`: File konfigurasi environment (untuk URL Database).
- `requirements.txt`: Daftar library yang dibutuhkan.

## 🚀 Cara Menjalankan
1. **Instalasi Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Konfigurasi Database**:
   Buka file `.env` dan sesuaikan `DATABASE_URL` dengan username, password, dan nama database PostGIS Anda.
3. **Persiapan Database (SQL)**:
   Pastikan extension PostGIS sudah aktif dan tabel sudah dibuat (lihat bagian [Persiapan Database](#persiapan-database) di bawah).
4. **Jalankan Aplikasi**:
   ```bash
   uvicorn main:app --reload
   ```
5. **Akses Dokumentasi**:
   Buka [http://localhost:8000/docs](http://localhost:8000/docs) di browser Anda untuk melihat Swagger UI. Silakan ambil screenshot dari sini untuk laporan.

## 🛠️ Persiapan Database
Jalankan perintah SQL berikut di tool database Anda (seperti pgAdmin atau DBeaver):

```sql
-- 1. Aktifkan Extension PostGIS
CREATE EXTENSION IF NOT EXISTS postgis;

-- 2. Buat Tabel Fasilitas Publik
CREATE TABLE IF NOT EXISTS fasilitas_publik (
    id SERIAL PRIMARY KEY,
    nama VARCHAR(255) NOT NULL,
    jenis VARCHAR(100),
    alamat TEXT,
    geom GEOMETRY(Point, 4326)
);

-- 3. Tambahkan Data Sampel (Opsional)
INSERT INTO fasilitas_publik (nama, jenis, alamat, geom) 
VALUES 
('Kampus Itera', 'Pendidikan', 'Jati Agung', ST_SetSRID(ST_Point(105.3121, -5.3575), 4326)),
('RS Airan Raya', 'Kesehatan', 'Jl. Airan Raya', ST_SetSRID(ST_Point(105.3050, -5.3700), 4326));
```

## ✅ Fitur yang Diimplementasikan
1. **GET `/fasilitas`**: Mengambil semua data fasilitas.
2. **GET `/fasilitas/{id}`**: Mengambil data fasilitas berdasarkan ID.
3. **READ `/geojson`**: Mengembalikan data dalam format standar GeoJSON (FeatureCollection).
4. **POST `/fasilitas`**: Menambah data baru dengan validasi Pydantic (wajib koordinat longitude & latitude).
5. **GET `/fasilitas/nearby`**: Query spasial untuk mencari fasilitas dalam radius tertentu (meter) berdasarkan titik pusat (lat, lon).
