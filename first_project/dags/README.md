`bash_operators_dag.py` - выполняет bash операции

`dataset_dag.py` - скачивает датасет в файл df.csv и выводит группировку по Pclass, Survived в файл output.csv (файлы df.csv и output.csv будут в контейнере)

`shortest_path_graph_dag.py` - ищет кратчайший путь в графе (получает данные из input.csv, записывает кратчайший путь в output.csv)

P.S. установить переменную var (Admin -> Variables) (для `dataset_dag.py`)

![Scheme1](https://github.com/romantitovmephi/airflow_in_docker/blob/main/first_project/dags.png?raw=true)

