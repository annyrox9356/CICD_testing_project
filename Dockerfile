FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Naya Step: Train karne se pehle fresh data generate karo
RUN python src/generate_data.py

# Data ban gaya, ab model train karo
RUN python src/train.py

EXPOSE 8000
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]