import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Simulasi pengumpulan data dari backend IoT
# Fitur: Suhu saat ini, Kelembapan, Intensitas Cahaya (LDR)
# Target: Prediksi suhu 1 jam ke depan
data = {
    'temp_current': np.random.uniform(25.0, 35.0, 1000),
    'humidity': np.random.uniform(40.0, 90.0, 1000),
    'light_intensity': np.random.uniform(100, 4000, 1000)
}
df = pd.DataFrame(data)
# Simulasi suhu masa depan memiliki korelasi dengan kondisi saat ini
df['temp_future'] = df['temp_current'] * 0.9 + (df['light_intensity'] / 2000) + np.random.normal(0, 0.5, 1000)

# Pembagian data: 80% pelatihan, 20% pengujian (seperti di Resume Sesi 4)
X = df[['temp_current', 'humidity', 'light_intensity']]
y = df['temp_future']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Menggunakan Supervised Learning - Regression
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluasi Model
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Evaluasi Model Machine Learning:")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"R-squared: {r2:.4f}")
