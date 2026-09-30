# ---------------------------------------------------
# المرحلة 1: بيئة بايثون المؤقتة لتنزيل الصور
# ---------------------------------------------------
FROM python:3.11-slim AS builder

WORKDIR /build

# نسخ سكريبت التنزيل وتشغيله داخل الحاوية
COPY download_images.py .
RUN python download_images.py

# ---------------------------------------------------
# المرحلة 2: خادم Nginx النهائي للإنتاج
# ---------------------------------------------------
FROM nginx:latest

# مجلد العمل الافتراضي لمواقع Nginx
WORKDIR /usr/share/nginx/html

# نسخ ملف الموقع index.html من مجلد المشروع
COPY ./html/index.html .

# نسخ الصور التي تم تنزيلها في المرحلة الأولى (builder)
COPY --from=builder /build/images ./images

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]