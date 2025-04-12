# Uporabimo uradno Python sliko
FROM python:3.10-slim

# Nastavimo delovno mapo znotraj kontejnerja
WORKDIR /app

# Kopiramo datoteko z zahtevami in namestimo odvisnosti
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiramo vso vsebino projekta v kontejner
COPY . .

# Nastavimo zagonski ukaz
CMD ["python", "nal1.py"]
CMD ["pytest"]
