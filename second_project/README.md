Создание Docker-Compose

Можно поднять Postgres внутри Docker'а и получать к ней доступ через pgAdmin

В docker-compose.yml собраны вместе images: first_docker, postgres, pgadmin4

1) запустить из текущей папки с yml: docker-compose up
2) перейти в pgAdmin: http://localhost:5050 (login: admin@admin.com, password: root)
3) настроить соединение c Postgres (login: root, password: root)
4) привязать pgAdmin к базе, настроить соединение - добавить сервер postgres: а) в текущей папке - найти ID нужного контейнера: docker ps; б) найти IP контейнера: docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' {ID CONTAINER}
5) настроить соединение - добавить IP в pgAdmin
6) можно создавать таблицы, останавливать контейнер, при этом все таблицы будут сохраняться в контейнере