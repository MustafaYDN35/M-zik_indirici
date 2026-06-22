from flask import Flask, render_template, request, jsonify
import yt_dlp
import os

app = Flask(__name__,)

DOWNLOAD_FOLDER = "indirilenler"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',
        'noplaylist': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


@app.route("/")
def index():
    return render_template("muzik_indirici.html")


@app.route("/download", methods=["POST"])
def download():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"status": "error", "message": "URL boş olamaz"})

    try:
        download_audio(url)
        return jsonify({"status": "ok", "message": "İndirme tamamlandı"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
