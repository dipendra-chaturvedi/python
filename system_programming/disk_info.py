import psutil

disk = psutil.disk_usage("C:\\")

print("Total:", round(disk.total / (1024 ** 3), 2), "GB")
print("Used:", round(disk.used / (1024 ** 3), 2), "GB")
print("Free:", round(disk.free / (1024 ** 3), 2), "GB")
print("Usage:", disk.percent, "%")