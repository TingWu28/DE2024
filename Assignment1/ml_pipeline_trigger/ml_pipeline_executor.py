import google.cloud.aiplatform as aip
import logging
import os

def run_ml_pipeline():
    # Define the GCS path to your pipeline YAML and pipeline root
    pipeline_def = "gs://temp_de2024_2117913/heartdisease_predictor_training_pipeline.yaml"
    pipeline_root = "gs://temp_de2024_2117913"

    # Define the parameters that the pipeline requires
    parameter_values = {
        'project_id': 'de2024-435020',
        'data_bucket': 'data_de2024_2117913',
        'dataset_uri': 'gs://data_de2024_2117913/datasets/training_set.csv',
        'model_repo': 'models_de2024_2117913'
    }

    # Create the job
    job = aip.PipelineJob(
        display_name="retrain-model",
        template_path=pipeline_def,
        pipeline_root=pipeline_root,
        parameter_values=parameter_values
    )

    # Run the job
    job.run()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    run_ml_pipeline()
