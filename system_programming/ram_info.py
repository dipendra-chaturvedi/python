import psutil

memory = psutil.virtual_memory()

print("Total RAM:", round(memory.total / (1024 ** 3), 2), "GB")
print("Used RAM:", round(memory.used / (1024 ** 3), 2), "GB")
print("Available RAM:", round(memory.available / (1024 ** 3), 2), "GB")
print("RAM Usage:", memory.percent, "%")