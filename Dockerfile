FROM arm32v7/python:3.7-buster

WORKDIR /usr/src/grianity
RUN export PKG_CONFIG_PATH="${PKG_CONFIG_PATH}:/usr/local/opt/libffi/lib/pkgconfig"
RUN apt-get install libffi-dev libssl-dev
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
