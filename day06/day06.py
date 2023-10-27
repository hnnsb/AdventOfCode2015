from collections import Counter
from os.path import basename
import re

fileName = basename(__file__)
day = int(fileName.strip(r"day|.py"))
# -----------------------------------------------------
data = ""
with open(f"day06/input.txt", "r") as f:
            data = f.read()
data = data.splitlines()

lights = [[False for _ in range(1000)] for __ in range(1000)]

for instruction in data:
    x1,y1,x2,y2 = tuple(map(int, re.findall(r"\d+", instruction)))
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if "on" in instruction:
                lights[y][x] = True
            elif "off" in instruction:
                lights[y][x] = False
            elif "toggle" in instruction:
                lights[y][x] = not lights[y][x]

res = sum(map(sum, lights))
print(res)

lights2 = [[0 for _ in range(1000)] for __ in range(1000)]

for instruction in data:
    x1,y1,x2,y2 = tuple(map(int, re.findall(r"\d+", instruction)))
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if "on" in instruction:
                lights2[y][x] += 1
            elif "off" in instruction:
                if lights2[y][x] > 0:
                    lights2[y][x] -= 1
            elif "toggle" in instruction:
                lights2[y][x] += 2

res2 = sum(map(sum, lights2))
print(res2)