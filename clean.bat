@REM stop container
call docker stop

@REM remove image
call docker image rm "ml-deployment-1"
