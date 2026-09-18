import statistics

data = [10, 20, 20, 30, 40]

print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))
print("Median Low:", statistics.median_low(data))
print("Median High:", statistics.median_high(data))
print("Standard Deviation:", statistics.stdev(data))
print("Population Standard Deviation:", statistics.pstdev(data))
print("Variance:", statistics.variance(data))
print("Population Variance:", statistics.pvariance(data))
print("Geometric Mean:", statistics.geometric_mean(data))
print("Harmonic Mean:", statistics.harmonic_mean(data))
print("Quantiles:", statistics.quantiles(data))