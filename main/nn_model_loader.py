import sqlalchemy as sa
import pickle
import pandas as pd
from keras.models import model_from_json


def find_model_binary(engine):
    result = engine.execute("SELECT `model` FROM `model_table` WHERE `model_name` = 'neural_net'")
    model_binary = result.fetchone()
    return model_binary['model']

def find_model_json(engine):
    result = engine.execute("SELECT `model` FROM `nn_model` WHERE `model_name` = 'neural_net'")
    model_json = result.fetchone()
    return model_json['model']

def load_test_data():
    test_data = pd.read_csv('/Users/a13659/git/ca-reward/car-bosatsu-ai/ai-core/resources/sample/nn_train_sample.csv')
    del test_data['aff_id']
    del test_data['label']
    return test_data

if __name__ == '__main__':
    host = 'mysql+pymysql://root:rootpasswd@localhost/pickle_test?charset=utf8'
    engine = sa.create_engine(host, echo=True)

    model_binary = find_model_binary(engine)
    model_json = find_model_json(engine)

    nn_model = model_from_json(model_json)
    weights = pickle.loads(model_binary)

    nn_model.set_weights(weights)

    print(weights)

    nn_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    test_data = load_test_data()

    result = nn_model.predict_proba(test_data.values)

    print(result)
