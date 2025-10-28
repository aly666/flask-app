# Gunakan base image ringan
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh source code
COPY app.py .

# Expose port Flask
EXPOSE 8080

# Jalankan aplikasi
CMD ["python", "app.py"]

