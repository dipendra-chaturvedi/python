# Real-Life Example: GST Calculator
def calculate_gst(price):
    gst = price * 0.18
    return price + gst

total = calculate_gst(1000)

print(total)