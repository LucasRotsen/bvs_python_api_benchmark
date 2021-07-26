FROM python:3.8.1

WORKDIR /bvs_python_api_benchmark/

COPY requirements.txt /bvs_python_api_benchmark/

RUN pip install -r requirements.txt

COPY api /bvs_python_api_benchmark/api/
COPY database /bvs_python_api_benchmark/database/
COPY service /bvs_python_api_benchmark/service/

EXPOSE 8000

CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]


