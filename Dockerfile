FROM python:3.7
WORKDIR /home/app

COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "editimage.py"]
