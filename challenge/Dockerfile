# Usa la imagen oficial de Python
FROM python:3.13-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requirements
COPY requirements.txt .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Expone el puerto donde correrá Gunicorn
EXPOSE 8000

# Comando para correr Gunicorn con 3 workers
CMD ["gunicorn", "challenge.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
