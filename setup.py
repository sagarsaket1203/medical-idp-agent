from setuptools import setup, find_packages

setup(
    name='medical-idp-agent',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'langgraph',
        'llama-index',
        'crewai',
        'mlflow',
        'databricks-sql-connector',
        'lancedb',
        'faiss-cpu',
        'folium',
        'pandas',
        'numpy',
        'openai',
        'pydantic'
    ],
)