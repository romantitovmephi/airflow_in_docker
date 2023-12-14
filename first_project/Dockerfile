FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev zsh curl git locales
RUN pip3 install pandas virtualenv pytrends networkx
RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV TZ=Europe/Moscow

COPY requirements.txt /root/requirements.txt
RUN python3 -m pip install -r /root/requirements.txt

RUN airflow db init
RUN airflow users create --username admin --role Admin --email rt@rt.org --firstname Roman  --lastname Titov --password admin

COPY airflow.cfg /root/airflow/airflow.cfg
COPY dags /root/airflow/dags
CMD (airflow scheduler &) && airflow webserver


