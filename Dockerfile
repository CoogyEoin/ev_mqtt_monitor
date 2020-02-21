FROM arm32v7/python:3.7-buster

WORKDIR /usr/src/app

RUN apt-get install libffi-dev libssl-dev

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
