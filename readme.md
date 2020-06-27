## TF Serving app

It classifies the input room image as 'clean' or 'messy'.

Dataset:
https://www.kaggle.com/cdawn1/messy-vs-clean-room

To start
```
docker-compose up -d --build
```

To use
```
curl -F image=@./image.jpg localhost:8000/predict
```