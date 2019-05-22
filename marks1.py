# mark1.py
marks = [90, 25, 67,45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d student persuades pass point" % number)
    else:
        print("%d student don't persuade pass point" % number)