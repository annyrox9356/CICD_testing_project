FROM python:3.12-slim

WORKDIR /app

# Dependencies copy aur install karein
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pura code copy karein
COPY . .

# Training script run karein taaki model.pkl image ke andar generate ho jaye
RUN python train.py

EXPOSE 8000

# API server chalu karein (List format me)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]