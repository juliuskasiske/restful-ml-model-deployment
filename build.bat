@REM build image
call docker build -t "ml-deployment-1" .

@REM run container
call docker run -p 5000:5000 "ml-deployment-1"

