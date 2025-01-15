# استفاده از پایتون 3.9
FROM python:3.9-slim

# پوشه کاری داخل کانتینر
WORKDIR /app

# نصب وابستگی‌ها
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# کپی کردن پروژه به کانتینر
COPY . /app/

# پورت 8000 رو باز می‌کنیم
EXPOSE 8000

# اجرای سرور Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
