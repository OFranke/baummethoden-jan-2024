import pandas as pd
import pickle


def test_prediction():
    # load trained model
    file_to_open = open("models/baummethoden.pickle", "rb")
    trained_model = pickle.load(file_to_open)
    file_to_open.close()

    # load data that we want predictions for
    prediction_data = pd.read_csv("data/prediction_input_mpg.csv", sep=";")

    prediction_result = trained_model.predict(prediction_data)
    # assert prediction_result == [16.0]
