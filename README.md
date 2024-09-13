# Use files Yandex Disk
Стк веб-приложения: TailwindCSS + npm + gulp + Django + Postgres + Gunicorn + Nginx + Docker.
Use files Yandex Disk - это адаптивное веб-приложение которое позволяет пользователям просматривать и загружать
файлы из Яндекс.Диска по публичной ссылке. Приложение использует API Яндекс.Диска для получения списка файлов.
## Запуск
### Запуск с помощью Docker
1. `git clone https://github.com/HANM4/django_useFilesFromYandexDisk.git`
2. `cd .\django_useFilesFromYandexDisk\`
3. Удаляем папку ./data/postgres
4. `docker-compose up -d --build`
5. `docker ps`
6. `docker exec -it {CONTAINER ID} bash` {CONTAINER ID} заменить на id django из docker ps (пример рабочей команды: docker exec -it ec3b6766197f bash)
7. `bash docker_first_up.sh`
8. `exit` или ctrl +z выход из терминала контейнера
9. После завершения всех вышеуказанных шагов, приложение будет доступно по адресу http://localhost:8080/.

## Функционал
- Просмотр списка файлов на Яндекс.Диске по публичной ссылке.
- Фильтрация файлов по типу (архивы, документы, изображения, исполняемые файлы, медиа файлы).
- Загрузка файлов на локальный компьютер.
- Реализовано кеширование запросов чтобы не отправлять запросы к API Яндекс.Диску слишком часто.
- Адаптивный пользовательский интерфейс.