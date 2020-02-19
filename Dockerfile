FROM python:3
RUN mkdir -p /usr/src/grianity
WORKDIR /usr/src/grianity

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
