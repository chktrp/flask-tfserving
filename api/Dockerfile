FROM tensorflow/tensorflow:2.1.1

WORKDIR /usr/src/app/
COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["python", "app.py"]
