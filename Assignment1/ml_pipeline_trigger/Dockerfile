FROM python:3.10.7-slim
ADD ml_pipeline_executor.py /home/ml_pipeline_executor.py
ADD requirements.txt ./
RUN pip install -r requirements.txt
# Expose the port that our app runs in
EXPOSE 5000
ENTRYPOINT ["python","/home/ml_pipeline_executor.py"]
