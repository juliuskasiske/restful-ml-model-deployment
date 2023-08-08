# restful ml model deployment

## 1. Background
During the first wave of COVID-19, three friends and I co-founded a delivery service, called Best Bite, for restaurants that were forced to close due to lockdowns. From that endeavour, we gathered data for each day on delivery frequency and resulting revenues and the gross profit we could expect. I joined that order data for each day with local weather data in order to understand how weather conditions influence customer order patterns. 

In order to demonstrate pythonic and RESTful machine learning model deployment, I trained a Decision Tree Regressor on that data. With the final model parameters, in theory, we could predict how much gross profit we could expect for the coming day, given weather forecasts and a few other attributes. These predicitions could have been used to perform vehicle capacity planning and save on delivery costs.

## 2. Disclaimers
### 2.1 Model accuracy
The focus of this project was to demonstrate containerized model deployment, not optimized model training. As such, I performed minimal preprocessing. Also, in order to save work, I chose to omit feature scaling and opted for a model that is insensitive to value ranges. The R2-score of the regressor on validation data will range between 0.1 and 0.3. Hence, please refrain from considering model predictions as reliable.

### 2.2 Data quality
While all weather data is accurate, I mocked any order data from Best Bite in order to not publicly disclose internal financial information. As such, please do not consider data to be accurate.

## 3. Running the server on your own
Feel free to test the system! To do so, all you have to do is to run the repositories ```build.bat``` file, if you are on Windows, and the ```build.sh``` file if you are on macOS or Linux. Then, call your localhost on port 5000.

## 4. Project architecture
For importing and transforming data, I used ```Pandas```, I instantiated and trained the Decision Tree Regressor using ```sklearn```. After defining the class and methods that will preprocess the data, train the model and make the predictions, the model will be instantiated and trained whenever the container is started. 

All modeling functionality is wrapped by a Flask app. In Flask, I defined the requests the server handles and how the client-side passes values for which to predict. Flask exposes the app on the container port 5000, which is forwarded to host port 5000 in the docker-run command. 

Docker then containerizes the application and enables deployment. Note that the service will run on your local machine. I refrained from deploying it on external cloud instances.

<img src="./example.jpg" alt="Architecture">




