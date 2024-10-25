FROM python:3.10.7-slim
WORKDIR /usr/src/heartdiseaseapp-ml
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT ["python","ml_pipeline_executor.py"]
