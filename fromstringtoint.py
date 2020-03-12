import re

def myAtoi(str):
    str = str.strip()
    numbers = re.findall('^[-+]?\d+\.?\d?', str)
    if numbers:
        desired = int(float(numbers[0]))
        if desired < -2 **31:
            return -2 ** 31
        return desired
    return 0
print(myAtoi('192.12'))