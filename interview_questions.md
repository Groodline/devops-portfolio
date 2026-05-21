# Junior DevOps — вопросы для собеседования

## Linux

### Что такое SSH?
SSH — это протокол для безопасного подключения к удалённому серверу через терминал.

Пример:

```bash
ssh user@server_ip
```

### Как посмотреть текущую директорию?

```bash
pwd
```

### Как посмотреть файлы?

```bash
ls
ls -la
```

### Как изменить права файла?

```bash
chmod +x script.sh
```

### Как посмотреть процессы?

```bash
ps aux
top
htop
```

### Как посмотреть логи systemd-сервиса?

```bash
journalctl -u nginx
journalctl -u nginx -f
```

## Docker

### Что такое Docker image?
Image — это шаблон, из которого создаются контейнеры.

### Что такое Docker container?
Container — это запущенный экземпляр image.

### Чем Dockerfile отличается от docker-compose.yml?
Dockerfile описывает сборку одного image.  
docker-compose.yml описывает запуск нескольких сервисов и их связи.

### Как посмотреть контейнеры?

```bash
docker ps
docker ps -a
```

### Как посмотреть логи контейнера?

```bash
docker logs container_name
docker compose logs -f
```

## Nginx

### Для чего нужен Nginx?
Nginx может раздавать статические файлы, работать как reverse proxy и принимать HTTP-запросы.

### Что такое reverse proxy?
Reverse proxy принимает запрос от пользователя и передаёт его внутреннему приложению.

## Git

### Что делает git pull?
Загружает изменения из удалённого репозитория и обновляет локальную копию.

### Что делает git push?
Отправляет локальные коммиты в удалённый репозиторий.

## CI/CD

### Что такое CI/CD?
CI/CD — это автоматизация проверки, сборки и деплоя проекта.

### Как работает GitHub Actions в портфолио?
После push в main GitHub Actions подключается к VPS по SSH и выполняет команды обновления проекта.
