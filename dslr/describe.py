import numpy
import matplotlib.pyplot as plot
import warnings
import sys
import pandas as pd

if len(sys.argv) != 2:
    print("Error: Usage: python describe.py <dataset.csv>")
    exit(1)

filename = sys.argv[1]
if filename != 'datasets/dataset_train.csv':
    print("The dataset for training must be called dataset_train.csv and saved in the directory \'datasets\'. Your path must be datasets/dataset_train.csv")
    exit(1)
try:
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        raw_data = pd.read_csv(filename)
except:
    print("Error loading dataset_train.csv")
    exit(1)

titles = raw_data.columns[6:].tolist()
data = raw_data.iloc[:, 6:].to_numpy()

def metric(function, colum):
    for i,v in enumerate(titles):
        if i < len(titles) - 1: print(f'{titles[i]}\t', end='')
        else: print(titles[i])


count = lambda lst: len(lst)


print('\t\t',end='')
for i,v in enumerate(titles):
    if i < len(titles) - 1: print(f'{titles[i]}\t', end='') 
    else: print(titles[i])

""" Count """
print('Count\t',end='')
