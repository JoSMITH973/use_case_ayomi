FROM python:3.10.2

WORKDIR /home/user

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py npi.py ./

EXPOSE 8000
ENTRYPOINT ["python", "main.py"]