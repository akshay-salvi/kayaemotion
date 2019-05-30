FROM python:3.6.6

WORKDIR /app
COPY . /app
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install Pillow
RUN pip install setuptools


CMD ["python", "main.py"]
