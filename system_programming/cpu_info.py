import psutil

print("CPU Cores:", psutil.cpu_count(logical=False))
print("Logical CPUs:", psutil.cpu_count(logical=True))
print("CPU Usage:", psutil.cpu_percent(interval=1), "%")