import os
from pathlib import Path
from dotenv import load_dotenv

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs


# ==========================================
# KONFIGURASI ENVIRONMENT
# ==========================================

BASE_DIR = Path(__file__).resolve().parent

# Membaca file .env untuk pengujian lokal
load_dotenv(BASE_DIR / ".env")

# Mengambil kredensial dari environment
TEST_USER = os.getenv("TEST_USER")
TEST_PASS = os.getenv("TEST_PASS")

# Konfigurasi server untuk deployment
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))

# Memastikan kredensial tersedia
if not TEST_USER or not TEST_PASS:
    raise ValueError(
        "TEST_USER dan TEST_PASS harus diatur "
        "melalui environment variable."
    )


# ==========================================
# HALAMAN LOGIN
# ==========================================

LOGIN_HTML = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Login - Latihan Selenium</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f1f5f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .login-box {
            background: white;
            padding: 35px;
            width: 320px;
            border-radius: 12px;
            box-shadow: 0 4px 15px #0002;
        }

        input, button {
            width: 100%;
            padding: 12px;
            margin-top: 12px;
            box-sizing: border-box;
        }

        button {
            background: #2563eb;
            color: white;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>Login Sistem</h2>
        <p>Latihan Automation Testing</p>

        <form action="/login" method="POST">
            <input
                type="text"
                id="username"
                name="username"
                placeholder="Username"
                required
            >

            <input
                type="password"
                id="password"
                name="password"
                placeholder="Password"
                required
            >

            <button type="submit" id="login-button">
                Login
            </button>
        </form>
    </div>
</body>
</html>
"""


# ==========================================
# HALAMAN DASHBOARD
# ==========================================

DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Dashboard</title>
</head>
<body>
    <h1>Login Berhasil!</h1>
    <p>Selamat datang di halaman Dashboard.</p>
    <p>Pengujian Selenium dapat dilakukan pada halaman ini.</p>
</body>
</html>
"""


# ==========================================
# SERVER APLIKASI
# ==========================================

class LoginHandler(BaseHTTPRequestHandler):

    def send_html(self, html, status=200):
        self.send_response(status)
        self.send_header(
            "Content-Type",
            "text/html; charset=utf-8"
        )
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    # Menangani permintaan GET
    def do_GET(self):

        if self.path in ["/", "/login"]:
            self.send_html(LOGIN_HTML)

        elif self.path == "/dashboard":
            self.send_html(DASHBOARD_HTML)

        else:
            self.send_error(
                404,
                "Halaman tidak ditemukan"
            )

    # Menangani proses login
    def do_POST(self):

        if self.path == "/login":

            length = int(
                self.headers.get("Content-Length", 0)
            )

            data = self.rfile.read(length).decode("utf-8")
            form = parse_qs(data)

            username = form.get("username", [""])[0]
            password = form.get("password", [""])[0]

            # Memeriksa kredensial dari environment
            if (
                username == TEST_USER
                and password == TEST_PASS
            ):

                self.send_response(303)
                self.send_header(
                    "Location",
                    "/dashboard"
                )
                self.end_headers()

            else:

                self.send_html(
                    "<h2>Login Gagal!</h2>"
                    "<p>Username atau password salah.</p>"
                    '<a href="/login">Kembali ke Login</a>',
                    status=401
                )

        else:
            self.send_error(
                404,
                "Halaman tidak ditemukan"
            )


# ==========================================
# MENJALANKAN SERVER
# ==========================================

if __name__ == "__main__":

    server = HTTPServer(
        (HOST, PORT),
        LoginHandler
    )

    print("Server berhasil dijalankan!")
    print(f"Host : {HOST}")
    print(f"Port : {PORT}")
    print(
        f"Login lokal: http://127.0.0.1:{PORT}/login"
    )

    server.serve_forever()