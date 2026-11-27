# Automation Testing M13

## 1. Project Overview

Proyek ini merupakan implementasi Automation Testing menggunakan Selenium WebDriver dan PyTest dengan pendekatan Page Object Model (POM).

Pengujian dilakukan pada fitur login aplikasi web. Proyek ini dikembangkan menggunakan Python dan Flask, kemudian di-deploy ke PythonAnywhere sebagai environment staging.

Pengujian otomatis dijalankan melalui GitHub Actions menggunakan browser Chrome dalam mode Headless.

### Tujuan Proyek
- Mengotomatisasi pengujian fitur login.
- Menerapkan Page Object Model (POM).
- Mengelola konfigurasi menggunakan environment variables.
- Melakukan deployment aplikasi ke staging.
- Menjalankan automation testing melalui CI/CD.

## 2. Technology Stack

Teknologi yang digunakan:

- Python 3.13
- Flask
- Selenium WebDriver
- PyTest
- Python-dotenv
- Google Chrome
- Git dan GitHub
- GitHub Actions
- PythonAnywhere

## 3. Project Structure

Struktur direktori proyek:

```text
automation-testing-m13/
│
├── .github/
│   └── workflows/
│       └── selenium-test.yml
│
├── pages/
│   ├── __init__.py
│   └── login_page.py
│
├── tests/
│   ├── __init__.py
│   └── test_login.py
│
├── screenshots/
│
├── app.py
├── check_env.py
├── config.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

Keterangan:
- `app.py`: Aplikasi web menggunakan Flask.
- `pages/`: Menyimpan komponen Page Object Model.
- `login_page.py`: Mengelola interaksi pada halaman login.
- `tests/`: Menyimpan skenario pengujian otomatis.
- `test_login.py`: Melakukan pengujian login valid.
- `config.py`: Mengelola konfigurasi environment.
- `check_env.py`: Memeriksa variabel environment.
- `.env`: Menyimpan konfigurasi lokal.
- `.env.example`: Template konfigurasi environment.
- `requirements.txt`: Daftar dependensi Python.
- `.github/workflows/`: Menyimpan konfigurasi GitHub Actions.
- `screenshots/`: Menyimpan hasil screenshot pengujian.

## 4. Prerequisites

Sebelum menjalankan proyek, pastikan perangkat telah memiliki:

1. Python versi 3.13.
2. Git.
3. Visual Studio Code atau editor Python lainnya.
4. Browser Google Chrome atau Microsoft Edge.
5. Koneksi internet.
6. Dependensi yang tercantum dalam requirements.txt.

## 5. Environment Configuration

Proyek menggunakan environment variables untuk menghindari penulisan URL dan kredensial secara langsung di dalam kode.

Variabel yang digunakan:

```env
BASE_URL=http://127.0.0.1:8000
TEST_USER=isi_username_pengujian
TEST_PASS=isi_password_pengujian
BROWSER=edge
HEADLESS=false
```

Keterangan:
- `BASE_URL`: Alamat aplikasi yang akan diuji.
- `TEST_USER`: Username pengujian.
- `TEST_PASS`: Password pengujian.
- `BROWSER`: Browser yang digunakan.
- `HEADLESS`: Mengatur mode browser tanpa tampilan GUI.

File `.env` tidak boleh diunggah ke repository GitHub karena berisi informasi sensitif.

Sebagai gantinya, proyek menyediakan `.env.example` sebagai template konfigurasi.

Untuk pengujian melalui GitHub Actions, konfigurasi rahasia disimpan menggunakan GitHub Repository Secrets dengan nama:
- BASE_URL
- TEST_USER
- TEST_PASS

## 6. Installation Steps

### A. Clone Repository

```bash
git clone <URL_REPOSITORY>
```

Masuk ke folder proyek:

```bash
cd automation-testing-m13
```

### B. Membuat Virtual Environment

Windows:

```bash
python -m venv .venv
```

Mengaktifkan virtual environment melalui Git Bash:

```bash
source .venv/Scripts/activate
```

Linux atau macOS:

```bash
source .venv/bin/activate
```

### C. Menginstal Dependencies

Jalankan perintah:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### D. Mengatur Environment

Salin file `.env.example` menjadi `.env`.

Git Bash:

```bash
cp .env.example .env
```

Kemudian sesuaikan nilai variabel environment dengan konfigurasi pengujian.

### E. Menjalankan Aplikasi

Jalankan aplikasi Flask:

```bash
python app.py
```

Aplikasi dapat diakses melalui alamat yang telah dikonfigurasi pada BASE_URL.

## 7. How to Run Automation Testing

Pastikan virtual environment sudah aktif dan aplikasi pengujian dapat diakses.

Jalankan pengujian:

```bash
python -m pytest -v -s tests/test_login.py
```

Skenario pengujian:

**Login Valid**

1. Membuka halaman login.
2. Mengisi username.
3. Mengisi password.
4. Menekan tombol Login.
5. Memverifikasi URL Dashboard.
6. Memverifikasi judul Dashboard.
7. Menyimpan screenshot hasil pengujian.

Pengujian dinyatakan berhasil apabila pengguna berhasil diarahkan ke halaman Dashboard dan seluruh assertion terpenuhi.

## 8. Deployment and CI/CD

Aplikasi web di-deploy menggunakan PythonAnywhere sebagai environment staging.

Automation testing dijalankan secara otomatis melalui GitHub Actions.

Workflow memiliki beberapa tahapan:

1. Checkout Repository.
2. Set Up Python.
3. Check Environment.
4. Install Dependencies.
5. Run Selenium Tests.
6. Upload Test Screenshot.

Pengujian menggunakan Google Chrome dalam mode Headless agar dapat berjalan pada GitHub Actions tanpa tampilan browser.

Hasil screenshot disimpan sebagai GitHub Actions Artifact dengan nama:

`selenium-test-screenshot`

Workflow dijalankan ketika terdapat push ke branch main atau melalui workflow_dispatch.

## 9. Troubleshooting

### A. ModuleNotFoundError

Penyebab:
Dependensi Python belum terinstal atau virtual environment belum aktif.

Solusi:

```bash
pip install -r requirements.txt
```

### B. Login Gagal

Penyebab:
Username atau password tidak sesuai dengan konfigurasi aplikasi.

Solusi:
- Periksa kembali variabel TEST_USER dan TEST_PASS.
- Pastikan GitHub Secrets sudah sesuai.
- Pastikan konfigurasi aplikasi staging sudah benar.

### C. TimeoutException

Penyebab:
Selenium tidak berhasil menemukan elemen atau menunggu proses halaman dalam batas waktu yang ditentukan.

Solusi:
- Periksa locator elemen.
- Pastikan aplikasi dapat diakses.
- Periksa URL pengujian.
- Sesuaikan waktu tunggu apabila diperlukan.

## 10. Testing Result

Pengujian automation testing berhasil dijalankan melalui GitHub Actions.

Hasil pengujian:
- Test Scenario: Login Valid
- Browser: Google Chrome
- Execution Mode: Headless
- Test Framework: PyTest
- Automation Library: Selenium WebDriver
- Pipeline Status: Success

Screenshot hasil pengujian tersedia melalui GitHub Actions Artifact.

---

**Project:** Automation Testing M13

**Course:** Implementasi dan Pengujian Perangkat Lunak

**Repository:** automation-testing-m13