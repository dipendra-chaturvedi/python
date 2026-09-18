import numpy as np
import statistics

data = np.array([10, 20, 20, 30, 40])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))
print("Sum:", np.sum(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))

print(type(statistics.mean([10, 20, 30])))
# float

print(type(np.mean(np.array([10, 20, 30]))))
# numpy.float64

