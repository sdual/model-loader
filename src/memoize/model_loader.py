import sqlalchemy as sa
import pickle
import pandas as pd


def load_model(cls, model_path):
    with open(model_path, 'rb') as model_file:
        xgb = pickle.load(model_file)
        return xgb

def find_model_binary(engine):
    result = engine.execute("SELECT `model` FROM `model_table` WHERE `model_name` = 'xgboost'")
    model_binary = result.fetchone()
    return model_binary['model']

def load_test_data():
    test_data = pd.read_csv('../data/test_data.csv')
    return test_data

if __name__ == '__main__':
    host = 'mysql+pymysql://root:rootpasswd@localhost/pickle_test?charset=utf8'
    engine = sa.create_engine(host, echo=True)

    model_binary = find_model_binary(engine)
    xgb = pickle.loads(model_binary)

    test_data = load_test_data()

    predict_proba = xgb.predict_proba(test_data)

    for p in predict_proba:
        print(p)
