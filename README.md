## [Сборка Airflow в Docker](https://github.com/romantitovmephi/airflow_in_docker/blob/main/first_project/README.md)

1) из текущей папки first_project собрать Dockerfile (при этом Docker должен быть запущен): ```docker build -t first_docker .```
2) вывести порт из контейнера и запустить Docker: ```docker run -p 8080:8080 first_docker```
3) в Airflow: http://localhost:8080
4) увидеть запущенные контейнеры: ```docker ps```
5) перейти во внутрь контейнера с его ID: ```docker exec -it {CONTAINER ID} /bin/bash```
6) перейти в Airflow: ```cd $HOME/airflow```
7) связать локальную папку dags с такой же папкой внутри контейнера (запуск из first_project): ```docker run -p 8080:8080 --mount type=bind,source="$(pwd)"/dags,target=/root/airflow/dags first_docker```
При этом все изменения в локальной папке dags будут сразу происходить и в контейнере в папке dags
8) можно создать Docker образ: ```docker save first_docker > first_docker.tar```

![Scheme1](https://github.com/romantitovmephi/airflow_in_docker/blob/main/first_project/dags.png?raw=true)

## [Создание Docker-Compose](https://github.com/romantitovmephi/airflow_in_docker/blob/main/second_project/README.md)
Можно поднять Postgres внутри Docker'а и получать к ней доступ через pgAdmin

В docker-compose.yml собраны вместе images: first_docker, postgres, pgadmin4
1) запустить из текущей папки с yml: ```docker-compose up```
2) перейти в pgAdmin: http://localhost:5050 (login: admin@admin.com, password: root)
3) настроить соединение c Postgres (login: root, password: root)
4) привязать pgAdmin к базе, настроить соединение - добавить сервер postgres: а) в текущей папке - найти ID нужного контейнера: ```docker ps```; б) найти IP контейнера: ```docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' {ID CONTAINER}```
5) настроить соединение - добавить IP в pgAdmin
6) можно создавать таблицы, останавливать контейнер, при этом все таблицы будут сохраняться в контейнере

![Scheme1](https://github.com/romantitovmephi/airflow_in_docker/blob/main/second_project/docker_compose.png?raw=true)

![Scheme1](https://github.com/romantitovmephi/airflow_in_docker/blob/main/second_project/docker_compose.png?raw=true)

![Scheme1](https://github.com/romantitovmephi/airflow_in_docker/blob/main/second_project/pgAdmin.png?raw=true)



