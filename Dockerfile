FROM python:3.12-slim
WORKDIR /app
COPY ./ Lab2/database.py /app/database.py/ 
COPY ./ Lab2/main.py /app/main.py/
COPY ./ Lab2/models.py /app/models.py/
COPY requirements.txt /app/requirements.txt/
RUN pip install --no-cache-dir -r requirements.txt
COPY . . 
CMD ["uvicorn", "main:app", "--host",   "0.0.0.0", "--port", "8000"]
