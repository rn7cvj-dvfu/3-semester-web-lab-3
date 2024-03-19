FROM python:3.12.2-slim-bookworm

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN python init.py

EXPOSE 5000

CMD ["python" , "run.py" ]