import sys

def hour_glass_score(array, x, y):
    sum = 0
    sum += array[y][x]
    sum += array[y][x+1]
    sum += array[y][x+2]
    sum += array[y+1][x+1]
    sum += array[y+2][x]
    sum += array[y+2][x+1]
    sum += array[y+2][x+2]
    return sum

array_data = [ [int(item) for item in x.strip().split(' ')] for x in sys.stdin.readlines()]

max = 0
for x in range(0, 4):
    for y in range(0, 4):
        score = hour_glass_score(array_data, x, y)
        if score > max:
            max = score

print(max)


