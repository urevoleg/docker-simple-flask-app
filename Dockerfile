FROM python:3.8

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN ifconfig eth0 mtu 1450
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]