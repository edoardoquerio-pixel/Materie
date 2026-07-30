# Build stage
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Runtime stage
FROM python:3.11-slim

WORKDIR /app

# Copia le dipendenze installate dalla build stage
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copia l'applicazione
COPY app.py .

# Variabile d'ambiente per la versione (iniettata in build)
ENV APP_VERSION=dev

EXPOSE 8000

CMD ["python", "app.py"]