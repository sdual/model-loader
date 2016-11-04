import sqlalchemy as sa
import pickle
import pandas as pd
import time


def load_model(cls, model_path):
    with open(model_path, 'rb') as model_file:
        xgb = pickle.load(model_file)
        return xgb

def find_model_binary(engine):
    result = engine.execute("SELECT `model` FROM `model_table` WHERE `model_name` = 'xgboost'")
    model_binary = result.fetchone()
    return model_binary['model']

def load_model_file():
    with open('/Users/tenoritama/xgb-20161101.pickle', 'rb') as model_file:
        xgb = pickle.load(model_file)
    return xgb

def load_test_data():
    test_data = pd.read_csv('/Users/tenoritama/tmp-data/test-data.csv')
    return test_data

if __name__ == '__main__':
    host = 'mysql+pymysql://root:rootpasswd@localhost/pickle_test?charset=utf8'
    engine = sa.create_engine(host, echo=True)

    start_time_loading_db = time.time()
    model_db_binary = find_model_binary(engine)
    elapsed_time_db = time.time() - start_time_loading_db
    print(elapsed_time_db)


    start_time_loading_file = time.time()
    model_file_binary = load_model_file()
    elapsed_time_file = time.time() - start_time_loading_file
    print(elapsed_time_file)
