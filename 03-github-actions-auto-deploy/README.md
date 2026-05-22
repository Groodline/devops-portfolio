# 03 — GitHub Actions Auto Deploy


* GitHub Actions может запускать команды после push.
* Для безопасного подключения к серверу используются GitHub Secrets.
* SSH-ключи нельзя хранить в коде.
* Docker Compose удобно использовать для обновления приложения.
* Nginx может работать как reverse proxy перед приложением.



\## Локальная проверка



Проект был успешно запущен локально через Docker Compose.



Работают 2 контейнера:



\- auto\_deploy\_web — Flask web application

\- auto\_deploy\_nginx — Nginx reverse proxy



Приложение доступно по адресу:



http://localhost



Health check:



http://localhost/health



Результат локального запуска:



<img src="./screenshots/auto-deploy-local-result.png" alt="Auto deploy local result" width="700">

