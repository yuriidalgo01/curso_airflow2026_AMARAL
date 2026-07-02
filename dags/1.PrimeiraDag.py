import pendulum # Esta biblioteca é importante para lidar com datas e horários de forma eficiente.
from airflow import DAG

# Adicione a nova importação atualizada:
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id = "primera_dag",
    description = "Minha primeira DAG",
    schedule = None,  # A DAG não será executada automaticamente; será disparada manualmente.
    start_date = pendulum.datetime(2025, 1, 1, tz = "America/Sao_Paulo"),  # Data de início da DAG.
    catchup = False,  # Não executar execuções passadas que foram perdidas.
    tags = ["curso", "exemplo"],  # Tags para categorizar a DAG.
) as dag:
    task1 = BashOperator(task_id = "tsk1", bash_command = "sleep 5")
    task2 = BashOperator(task_id = "tsk2", bash_command = "sleep 5")
    #task2 = BashOperator(task_id = "tsk2", bash_command = "exit 1") # Teste de erros.
    task3 = BashOperator(task_id = "tsk3", bash_command = "sleep 5")

    task1 >> task2 >> task3  # Define a ordem de execução das tarefas: task1 -> task2 -> task3  