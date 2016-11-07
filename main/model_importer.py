import sqlalchemy as sa


host = 'mysql+pymysql://root:rootpasswd@localhost/pickle_test?charset=utf8'
engine = sa.create_engine(host, echo=True)


def load_binary_file():
    with open('../data/nn_sample_weight', 'rb') as file:
        binary = file.readlines()
    return binary

def insert_binary_model(binary):
    ins = "INSERT INTO `model_table` VALUES ('neural_net', load_file(%s))"
    engine.execute(ins, '/Users/a13659/ca-reward/nn_model/nn-weights-20161104.pickle')

if __name__ == '__main__':
    binary_data = load_binary_file()
    insert_binary_model(binary_data)
