# 1. Resmi ve hafif bir Python imajı kullanıyoruz
FROM python:3.11-slim

# 2. Sistem güncellemelerini yapıp FFmpeg'i kuruyoruz (yt-dlp'nin ses dönüştürmesi için şart)
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# 3. Konteyner içinde çalışma klasörü oluşturuyoruz
WORKDIR /app

# 4. Gerekli Python kütüphanelerini yüklüyoruz
RUN pip install --no-cache-dir flask yt-dlp

# 5. Proje dosyalarımızı konteynerin içine kopyalıyoruz
COPY . .

# 6. İndirilen müziklerin kaydedileceği klasörü oluşturuyoruz
RUN mkdir -p indirilenler

# 7. Flask uygulamasının çalışacağı portu dışarı açıyoruz
EXPOSE 5000

# 8. Uygulamayı başlatıyoruz
CMD ["python", "muzikindir.py"]