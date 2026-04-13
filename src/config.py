import os

# Environment Variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
DATABRICKS_HOST = os.getenv('DATABRICKS_HOST')
DATABRICKS_TOKEN = os.getenv('DATABRICKS_TOKEN')
MLFLOW_TRACKING_URI = os.getenv('MLFLOW_TRACKING_URI')
MLFLOW_EXPERIMENT_NAME = os.getenv('MLFLOW_EXPERIMENT_NAME')

# Directories
DATA_DIR = 'data/'
MODELS_DIR = 'models/'
OUTPUT_DIR = 'output/'
