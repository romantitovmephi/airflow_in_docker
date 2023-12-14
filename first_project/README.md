# Сборка Airflow в Docker

1) из текущей папки first_project собрать Dockerfile (при этом Docker должен быть запущен): ```docker build -t first_docker .```
2) вывести порт из контейнера и запустить Docker: ```docker run -p 8080:8080 first_docker```
3) в Airflow: http://localhost:8080
4) увидеть запущенные контейнеры: ```docker ps```
5) перейти во внутрь контейнера с его ID: ```docker exec -it {CONTAINER ID} /bin/bash```
6) перейти в Airflow: ```cd $HOME/airflow```
7) связать локальную папку dags с такой же папкой внутри контейнера (запуск из first_project): ```docker run -p 8080:8080 --mount type=bind,source="$(pwd)"/dags,target=/root/airflow/dags first_docker```
При этом все изменения в локальной папке dags будут сразу происходить и в контейнере в папке dags
8) можно создать Docker образ: ```docker save first_docker > first_docker.tar```

