# filter1.py

def positive(x):
    return x > 0

print(list(filter(lambda x: x > 0,[1, -3, 2, 0, -5, 6])))