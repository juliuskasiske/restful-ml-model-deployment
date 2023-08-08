from flask import Flask
import model
import datetime

app = Flask(__name__)

def fill_values():
    weekday = datetime.date.today().weekday()
    day = 20200505
    month = 5
    return weekday, day, month

@app.route("/<avgTemp>-<highTemp>-<lowTemp>-<precipitation>-<windSpeed>-<sunMinutes>")
def homepage(avgTemp, highTemp, lowTemp, precipitation, windSpeed, sunMinutes):
    weekday, day, month = fill_values()
    prediction = model.predict_single(weekday, day, avgTemp, lowTemp, highTemp, precipitation, windSpeed, sunMinutes)
    return_day = day[:4] + "." + day[4:6] + "." + day[6:]
    return f"Expected gross profit for Best Bite on {return_day} will be: {prediction}"

if (__name__) == "__main__":
    # prepare model to make preds
    model = model.BestBiteModel()
    model.preprocess()
    model.train(show_score=True)
    app.run(host="0.0.0.0")