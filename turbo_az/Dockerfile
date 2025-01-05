FROM python:3.12
# FROM - İmage-i alır

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*
# RUN - Container qurularkən icra olunacaq komandaları göstərir və işə salır

WORKDIR /app
# WORKDIR - Komandaların işləyəcəyi folderi bildirir

COPY requirements.txt ./
# COPY - Verilmiş olan məlumatı container-də göstərdiyimiz yerə kopyalayır

RUN pip install --no-cache -r requirements.txt

COPY . .

EXPOSE 8000
# EXPOSE - Göstərilmiş portu xaricdən əlçatan edir

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD - App-i işə salmaq üçün komanda burada təyin edilir


# docker-compose build ---> Container-i quraşdırır
# docker-compose up ---> Containerləri işə salır
# docker-compose down ---> Layihənin işlək olan container-lərini dayandırır
# docker ps - up olmuş bütün containerləri göstərir
# docker exec -it `container_name or container_id` bash
