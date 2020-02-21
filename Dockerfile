FROM arm32v7/python:3.7-slim-buster

WORKDIR /usr/src/app
RUN chmod u=rwx,g=rx,o=rx requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
