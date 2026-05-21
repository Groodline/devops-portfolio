# 01 — Nginx Static Site Deploy

## Цель проекта

Задеплоить простой HTML-сайт на Linux/VPS через Nginx.

Этот проект показывает базовые навыки:

- работа через SSH;
- работа с Linux-директориями;
- настройка Nginx server block;
- проверка конфигурации через `nginx -t`;
- перезапуск сервиса через `systemctl`;
- просмотр логов Nginx.

## Стек

- Linux / Debian / Ubuntu
- Nginx
- SSH
- Bash

## Структура

```text
01-nginx-static-site-deploy/
├── index.html
├── nginx/
│   └── devops-static-site.conf
└── scripts/
    └── deploy_static_site.sh
```

## Ручной деплой

Подключиться к серверу:

```bash
ssh user@SERVER_IP
```

Установить Nginx:

```bash
sudo apt update
sudo apt install nginx -y
```

Создать папку сайта:

```bash
sudo mkdir -p /var/www/devops-static-site
```

Скопировать `index.html`:

```bash
sudo cp index.html /var/www/devops-static-site/index.html
```

Скопировать конфиг Nginx:

```bash
sudo cp nginx/devops-static-site.conf /etc/nginx/sites-available/devops-static-site
sudo ln -s /etc/nginx/sites-available/devops-static-site /etc/nginx/sites-enabled/devops-static-site
```

Проверить конфиг и перезагрузить Nginx:

```bash
sudo nginx -t
sudo systemctl reload nginx
```

Проверить в браузере:

```text
http://SERVER_IP
```

## Автоматический деплой скриптом

```bash
chmod +x scripts/deploy_static_site.sh
./scripts/deploy_static_site.sh
```

## Что я понял в процессе

- Nginx может раздавать статические файлы.
- Конфиги сайтов обычно лежат в `/etc/nginx/sites-available`.
- Активные сайты подключаются через symlink в `/etc/nginx/sites-enabled`.
- Перед перезапуском Nginx нужно проверять конфиг командой `sudo nginx -t`.
- Логи помогают искать ошибки в работе сайта.
