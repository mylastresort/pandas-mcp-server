FROM python:3.11-slim

RUN pip install --no-cache-dir uv

WORKDIR /app
COPY requirements.txt .
RUN uv pip install --system --no-cache-dir -r requirements.txt

COPY . .
COPY run_sse.py .

EXPOSE 8000
ENTRYPOINT ["python", "run_sse.py"]