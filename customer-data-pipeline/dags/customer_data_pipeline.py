from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
}

with DAG(
    'customer_data_pipeline',
    default_args=default_args,
    description='Pipeline to process customer data',
    schedule_interval='@daily',
    start_date=datetime(2025, 1, 1),
    catchup=False,
) as dag:

    # Spark ETL task
    spark_etl_task = SparkSubmitOperator(
        task_id='run_spark_etl',
        application="gs://customer-data-bucket/scripts/etl_spark_script.py",
        conn_id="spark_default",
        verbose=True
    )

    # Loading to BigQuery
    load_to_bigquery = GCSToBigQueryOperator(
        task_id='load_to_bigquery',
        bucket='customer-data-bucket',
        source_objects=['processed/customer_purchases_transformed.parquet'],
        destination_project_dataset_table='my_project.customer_dataset.customer_purchases',
        source_format='PARQUET',
        write_disposition='WRITE_TRUNCATE'
    )

    # task dependencies
    spark_etl_task >> load_to_bigquery
