import sys
from pymystem3 import Mystem
m = Mystem()

input_file = sys.stdin
next(input_file)
for line in input_file:
    i = line.split(',')[0]
    i = m.lemmatize(i)[:-1]
    for word in i:
        if word.isalpha():
            print(f'{word}')
