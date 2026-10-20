# IoT Environmental Monitoring & ML Prediction System

Sistem ini mengintegrasikan perangkat Internet of Things (IoT) dengan model Machine Learning (ML) berdasarkan konsep dari Resume Sesi 4: Introduction to Machine Learning.

## Arsitektur Sistem
1. **IoT Device (ESP32)**: Membaca data lingkungan menggunakan sensor **SHT31** (Suhu & Kelembapan) dan **LDR** (Intensitas Cahaya). Data dikirim melalui protokol MQTT.
2. **Backend (Golang)**: Menerima data dari MQTT broker (seperti Mochi MQTT), memproses, dan menyimpannya untuk analisis lebih lanjut.
3. **Machine Learning Model (Python)**: Menerapkan **Supervised Learning (Regression)** untuk memprediksi tren suhu di masa depan berdasarkan data historis, serta mengevaluasi model menggunakan metrik seperti MAE (Mean Absolute Error) sesuai dengan materi resume.

## Struktur Direktori
- `iot_device/`: Kode C++/Arduino untuk mikrokontroler ESP32.
- `backend/`: Kode Golang untuk MQTT Subscriber dan pengolahan data backend.
- `ml_model/`: Skrip Python untuk melatih model regresi (Supervised Learning).

## Cara Menjalankan
1. Konfigurasi kredensial WiFi dan MQTT Broker pada file `iot_device/main.ino`.
2. Jalankan MQTT broker lokal (misalnya Mochi MQTT).
3. Jalankan backend Golang dengan perintah `go run main.go` di folder `backend/`.
4. Jalankan `python train_model.py` di folder `ml_model/` untuk melatih model prediksi.
