import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from datetime import datetime, timedelta


###############################################
# Parameters
###############################################
spark_conn = os.environ.get("spark_conn", "spark_conn")
spark_master = "spark://spark:7077"
spark_app_name = "Spark Hello World"

###############################################
# DAG Definition
###############################################
now = datetime.now()

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(now.year, now.month, now.day),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1)
}

dag = DAG(
    dag_id="spark-test",
    description="This DAG runs a simple Pyspark app.",
    default_args=default_args,
    schedule_interval=timedelta(1)
)

start = DummyOperator(task_id="start", dag=dag)

spark_job = SparkSubmitOperator(
    task_id="spark_job",
    # Spark application path created in airflow and spark cluster
    application="/usr/local/spark/applications/hello-world.py",
    name=spark_app_name,
    conn_id=spark_conn,
    verbose=1,
    conf={"spark.master": spark_master},
    # application_args=[file_path],
    dag=dag)

end = DummyOperator(task_id="end", dag=dag)

start >> spark_job >> end
