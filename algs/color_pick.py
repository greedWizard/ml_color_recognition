import numpy as np
import warnings
import math
import pandas as pd
from collections import Counter
import random


def kns_class(data : dict, predict, k=3):
    if k < len(data):
        warnings.warn('K is set to a value less than total voting groups!')

    distances = []

    for group in data:
        for features in data[group]:
            p = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append((p, group))

    votes = [i[1] for i in sorted(distances)[:k]]
    vote_result = Counter(votes).most_common(1)[0][0]

    return vote_result


df = pd.read_csv('colors.data')
full_data = df.astype(float).values.tolist()
train_data = full_data[:]


random.shuffle(full_data)

test_size = 0.2

train_data = full_data[int(test_size*len(full_data)):]
test_data = full_data[:int(test_size*len(full_data))]

colors_q = len(open('colors.val').readlines())

k = math.floor(colors_q/2)*2 + 1

train_set = {}
test_set = {}

for i in range(colors_q):
    train_set[i] = []
    test_set[i] = []

for i in train_data:
    train_set[i[-1]].append(i[:-1])

for i in test_data:
    test_set[i[-1]].append(i[:-1])

colors_dict = {}
strings = []


with open('colors.val', 'rt') as f:
    strings = [l.strip() for l in f]

for string in strings:
    string = string.split('--')
    color = string[0]
    number = int(string[1])

    colors_dict[number] = color


if __name__ == "__main__":
    correct = 0
    total = 0

    accuracies = []

    accuracy = 0

    for group in test_set:
        for data in test_set[group]:
            vote = kns_class(train_set, data, k=9)

            if vote == group:
                correct += 1

            total += 1
        
    accuracy = correct / total