FROM python:3.8-buster

WORKDIR /workdir

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

RUN mkdir /model && wget https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin -O /model/lid.176.bin

COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
