import numpy as np
import warnings

try:
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        data = np.loadtxt('data.csv', delimiter=',', skiprows= 1)
except (OSError, IOError):
    print("Error: data.csv is empty of has invalid format.")
    exit(1)
except (StopIteration, ValueError, UserWarning):
	print("Error: data.csv is empty or has invalid format.")
	exit(1)

if data.size == 0:
    print("Error: data.csv contains no data")
    
if np.any(data < 0) or np.any(data > 1000000):
    print("Error: All values must be between 0 and 1,000,000.")
    exit(1)
    
print(data)