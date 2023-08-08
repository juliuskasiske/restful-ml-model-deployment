import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

class BestBiteModel:
    __data = None
    
    def __init__(self) -> None:
        # model self-initializes best bite data
        self.__data = pd.read_csv("alldata.csv", index_col=0)
    
    def preprocess(self):
        try:
            data_raw = self.__data
            data_raw["weekday"] = LabelEncoder().fit_transform(data_raw["weekday"])
            data_raw["day"] = data_raw["day"].apply(lambda row: int(row[-4:] + row[3:5] + row[0:2]))
            self.__data = data_raw
            return True

        except Exception:
            return False
        
    def train(self, show_score: bool):
        try:
            data_raw = self.__data
            # split raw data
            X_train, X_val, y_train, y_val = train_test_split(data_raw.drop(["revenue", "expGrossProfit", "ID"], axis = 1), 
                                                    data_raw["revenue"], 
                                                    random_state=3,
                                                    test_size=0.1, 
                                                    shuffle=True)
            # define regressor and train on training data
            model = DecisionTreeRegressor(max_leaf_nodes=10, max_depth=3)
            model.fit(X_train, y_train)

            if show_score:
                train_predictions = model.predict(X_train)
                val_predictions = model.predict(X_val)

                r2_train = r2_score(y_train, train_predictions)
                r2_val = r2_score(y_val, val_predictions)

                print(f"training score: {round(r2_train, 2)}")
                print(f"validation score: {round(r2_val, 2)}")
            
            self.__model = model
            return True
            
        except Exception:
            return False
        
    def predict_single(self, weekday, day, avgTemp, lowTemp, highTemp, 
                       precipitation, windSpeed, sunMinutes, month):
        values = [weekday, day, avgTemp, lowTemp, highTemp, precipitation, windSpeed, sunMinutes, month]
        data_raw = self.__data
        # define data frame
        single_data = pd.DataFrame(columns=["weekday", "day"] + list(data_raw.columns[-7:]))
        # fill data frame
        for index, col in enumerate(single_data.columns):
            single_data.loc[0, col] = values[index]
        
        #return predictions 
        return self.__model.predict(single_data)[0]
