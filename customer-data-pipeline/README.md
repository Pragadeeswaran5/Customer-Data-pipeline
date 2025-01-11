# Customer Data Pipeline

This project demonstrates a simple data engineering pipeline that:

1. Ingests raw customer purchase data into Google Cloud Storage (GCS).
2. Processes and transforms the data using Apache Spark.
3. Loads the transformed data into BigQuery for analytics.
4. Automates the pipeline using Apache Airflow.

## Technologies Used

- **Google Cloud Storage (GCS):** For storing raw and processed data.
- **Apache Spark:** For processing and transforming the data.
- **BigQuery:** For data warehousing and analytics.
- **Apache Airflow:** For pipeline orchestration.

## Repository Structure

```
customer-data-pipeline/
├── dags/
│   └── customer_data_pipeline.py      # Airflow DAG script
├── scripts/
│   └── etl_spark_script.py            # Spark ETL script
├── data/
│   └── raw/                           # Raw CSV data (local before upload)
├── README.md                          # Project documentation
```

## Setup and Execution

1. **Setup GCS:**
   - Create a bucket in GCS (e.g., `customer-data-bucket`).
   - Upload the raw data (e.g., `customer_purchases.csv`) to `gs://customer-data-bucket/raw/`.
   - Upload the Spark script to `gs://customer-data-bucket/scripts/etl_spark_script.py`.

2. **Spark ETL:**
   - Run the Spark ETL script on a Spark cluster or Dataproc.

3. **BigQuery Table:**
   - Create the dataset and table in BigQuery (e.g., `my_project.customer_dataset.customer_purchases`).

4. **Airflow Configuration:**
   - Add the DAG to your Airflow instance.
   - Ensure the `spark_default` and GCP connections are configured in Airflow.

5. **Run the Pipeline:**
   - Trigger the Airflow DAG to execute the pipeline.

## License

MIT License
