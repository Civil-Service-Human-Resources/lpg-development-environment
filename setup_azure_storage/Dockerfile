FROM python:3.9

WORKDIR /app

COPY ./script.py .

RUN pip install azure-storage-blob

ENTRYPOINT [ "python", "script.py" ]