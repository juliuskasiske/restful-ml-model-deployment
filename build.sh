docker build -t "ml-deployment-1" .
docker run -p 5000:5000 "ml-deployment-1"