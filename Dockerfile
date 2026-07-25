FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ۱. اول کپی تمام فایل‌ها به داخل امیج
COPY . .

# ۲. سپس ساخت کاربر و دادن مالکیت فایل‌های کپی‌شده به appuser
RUN adduser --disabled-password --gecos "" appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
