import sys

previous = None
cnt = 0
input_file = sys.stdin 
for line in input_file:
    line = line.strip()
    if previous:
        if previous == line:
            cnt += 1
        else:
            print(f'{previous} - {cnt} раз')
            previous = line
            cnt = 1
    else:
        previous = line
        cnt = 1
print(f'{previous} - {cnt} раз') 
