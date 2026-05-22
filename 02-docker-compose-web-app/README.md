\# 02 — Docker Compose Web App



\## Цель проекта



Запустить веб-приложение, базу данных PostgreSQL и Nginx через Docker Compose.



Проект показывает навыки:



\- написание Dockerfile

\- сборка Docker image

\- запуск нескольких сервисов через Docker Compose

\- использование .env

\- работа с volume для базы данных

\- reverse proxy через Nginx

\- проверка логов контейнеров



\## Стек



\- Python Flask

\- PostgreSQL

\- Docker

\- Docker Compose

\- Nginx



\## Структура проекта



02-docker-compose-web-app/



\- app/app.py

\- app/Dockerfile

\- app/requirements.txt

\- nginx/default.conf

\- docker-compose.yml

\- .env.example

\- README.md

\- screenshots/docker-compose-result.png



\## Запуск локально



Создать .env файл:



cp .env.example .env



Запустить контейнеры:



docker compose up -d --build



Проверить статус контейнеров:



docker compose ps



Открыть приложение:



http://localhost:8080



Проверить health endpoint:



curl http://localhost:8080/health



Посмотреть логи:



docker compose logs -f



Остановить проект:



docker compose down



Остановить проект и удалить volume базы данных:



docker compose down -v



\## Проверка работы



Проект был успешно запущен локально через Docker Compose.



Работают 3 контейнера:



\- devops\_nginx — Nginx reverse proxy

\- devops\_web\_app — Flask web application

\- devops\_postgres — PostgreSQL database



Приложение доступно по адресу:



http://localhost:8080



Health check:



http://localhost:8080/health



Результат работы приложения:



<img src="./screenshots/docker-compose-result.png" alt="Docker Compose result" width="700">


\## Что я понял в процессе



\- Dockerfile описывает, как собрать image для приложения.

\- Docker Compose позволяет запускать несколько связанных сервисов.

\- PostgreSQL хранит данные в Docker volume.

\- Nginx принимает HTTP-запросы и проксирует их в web-контейнер.

\- .env нужен, чтобы не хранить пароли прямо в docker-compose.yml.

