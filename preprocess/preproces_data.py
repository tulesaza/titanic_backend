import numpy as np


def split_train_data(dataset, ratio=0.2):
    # makes random generator to generate the same values for each execution
    np.random.seed(33)
    # random sequence of dataFrame indexes
    shuffled_indexes = np.random.permutation(len(dataset))
    # size of test data according to ratio
    test_size = int(len(dataset)*ratio)
    # array with indexes of test_set
    test_set_indexes = shuffled_indexes[:test_size]
    train_set_indexes = shuffled_indexes[test_size:]
    return dataset.iloc[train_set_indexes], dataset.iloc[test_set_indexes]


def prepare_x_and_y(dataset, split_column="Survived", drop_columns=None):
    if drop_columns is None:
        drop_columns = ["PassengerId", "Id"]
    temp = dataset.drop(drop_columns, axis=1)
    X = temp.drop(split_column, axis=1)
    y = temp[split_column].copy()
    return X.to_numpy(), y.to_numpy()
