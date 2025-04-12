# Uporabimo uradno Python sliko
FROM python:3.10-slim

# Nastavimo delovno mapo znotraj kontejnerja
WORKDIR /app

# Kopiramo datoteko z zahtevami in namestimo odvisnosti
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Install OpenGL libraries
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Kopiramo vso vsebino projekta v kontejner
COPY . .

# Nastavimo zagonski ukaz
CMD ["python", "nal1.py"]
#CMD ["pytest"]
