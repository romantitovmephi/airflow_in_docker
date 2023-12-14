from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import networkx as nx


shortest_path_graph_dag = DAG(
    "shortest_path_graph_dag",
    description='Python DAG',
    schedule_interval="* * * * *",
    start_date=days_ago(0, 0, 0, 0, 0),
    tags=['python']
)


def search_shortest_path():
    graph_list = []
    cntr = 0
    with open('/root/airflow/dags/input.csv') as in_file:
        for line in in_file:
            if cntr == 0:
                nodes = line.strip().split()[0]
                cntr_max = int(line.strip().split()[1])
            elif 1 <= cntr <= cntr_max:
                out_node = line.strip().split()[0]
                in_node = line.strip().split()[1]
                weight = int(line.strip().split()[2])
                graph_list.append((out_node, in_node, weight))
            elif cntr == cntr_max + 1:
                start_node = line.strip().split()[0]
                end_node = line.strip().split()[1]
            cntr += 1
        G = nx.DiGraph()
        G.add_weighted_edges_from(graph_list)
        try:
            print(nx.shortest_path_length(G, start_node, end_node, weight='weight'))
            shortest_path = str(nx.shortest_path_length(G, start_node, end_node, weight='weight'))
        except:
            print(-1)
            shortest_path = str(-1)

    out_file = open('/root/airflow/dags/output.csv', 'w')
    out_file.write(shortest_path)
    out_file.close()

search_path = PythonOperator(
    task_id='search_path',
    python_callable=search_shortest_path,
    dag=shortest_path_graph_dag
)

search_path