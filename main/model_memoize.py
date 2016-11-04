import sqlalchemy as sa
import pickle
import pandas as pd
import functools
from memoize import Memoizer
from keras.models import model_from_json


store = {}
memo = Memoizer(store)

host = 'mysql+pymysql://root:rootpasswd@localhost/pickle_test?charset=utf8'
engine = sa.create_engine(host, echo=True)


def load_test_data():
    test_data = pd.read_csv('../data/test_data.csv')
    return test_data

@memo(max_age=10)
def memoize_xgb_model():
    result = engine.execute("SELECT `model` FROM `model_table` WHERE `model_name` = 'xgboost'")
    print('------------------------model is loaded---------------------------')
    model_binary = result.fetchone()
    xgb = pickle.loads(model_binary['model'])
    return xgb

def memoize_nn_model():
    weight = engine.execute("SELECT `model` FROM `model_table` WHERE `model_name` = 'neural_net'")
    model = engine.execute("SELECT `model` FROM `nn_model` WHERE `model_name` = 'neural_net'")
    print('------------------------model is loaded---------------------------')
    weight_binary = weight.fetchone()
    model_json = model.fetchone()

    model = model_from_json(model_json)
    model.load_weights(weight_binary)


if __name__ == '__main__':

    test_data = load_test_data()

    while True:
        xgb = memoize_xgb_model()
        predict_proba = xgb.predict_proba(test_data)

        for p in predict_proba:
            print(p)
