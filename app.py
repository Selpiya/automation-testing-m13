import os
from pathlib import Path
from dotenv import load_dotenv

from flask import Flask, request, redirect, url_for


# =====================================
# KONFIGURASI ENVIRONMENT
# =====================================

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

TEST_USER = os.getenv("TEST_USER")
TEST_PASS = os.getenv("TEST_PASS")

HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", "8000"))

if not TEST_USER or not TEST_PASS:
    raise ValueError(
        "TEST_USER dan TEST_PASS belum diatur!"
    )


# =====================================
# INISIALISASI FLASK
# =====================================

app = Flask(__name__)


# =====================================
# HALAMAN LOGIN
# =====================================

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


# =====================================
# HALAMAN DASHBOARD
# =====================================

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


# =====================================
# ROUTE HALAMAN LOGIN
# =====================================

@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if username == TEST_USER and password == TEST_PASS:

            return redirect(
                url_for("dashboard"),
                code=303
            )

        return (
            """
            <h2>Login Gagal!</h2>
            <p>Username atau password salah.</p>
            <a href="/login">Kembali ke Login</a>
            """,
            401
        )

    return LOGIN_HTML


# =====================================
# ROUTE HALAMAN DASHBOARD
# =====================================

@app.route("/dashboard")
def dashboard():

    return DASHBOARD_HTML


# =====================================
# MENJALANKAN APLIKASI LOKAL
# =====================================

if __name__ == "__main__":

    print("Aplikasi Flask berhasil dijalankan!")
    print(f"URL: http://{HOST}:{PORT}/login")

    app.run(
        host=HOST,
        port=PORT,
        debug=False
    )