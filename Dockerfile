
FROM python:3.10

ADD main.py .

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["python","./main.py"]