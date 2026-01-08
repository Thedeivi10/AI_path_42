import numpy
import matplotlib.pyplot as plot
import warnings
import sys

if len(sys.argv) != 2:
    print("Error: Usage: python describe.py <dataset.csv>")
    sys.exit(1)

filename = sys.argv[1]
if filename != 'datasets/dataset_train.csv':
    print("The dataset for training must be called dataset_train.csv and saved in the directory \'datasets\'. Your path must be datasets/dataset_train.csv")
    exit(1)
try:
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        raw_data = numpy.genfromtxt('datasets/dataset_train.csv', delimiter= ',',
            skip_header=1,
            dtype=None,
            encoding='utf-8')
except:
    print("Error loading dataset_train.csv")

data = numpy.array(
	[row[6:] for row in raw_data],
	dtype = float
)
  
for i,l in enumerate(data):
    print(l);
    if i > 4: break;