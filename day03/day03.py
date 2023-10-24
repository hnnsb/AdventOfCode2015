from collections import Counter, defaultdict
from aocd.models import Puzzle
from os.path import basename
from dotenv import DotEnv
config = DotEnv()

fileName = basename(__file__)
day = int(fileName.strip(r"day|.py"))
TEST = False
# -----------------------------------------------------
data = ""
with open(f"day03/input.txt", "r") as f:
    data = f.read()

x, y = 0, 0
r, s = 0, 0
presents = defaultdict(int)
presents[(x, y)] = 2
for c in range(0, len(data), 2):
    match data[c]:
        case ">":
            x += 1
        case "v":
            y += 1
        case "<":
            x -= 1
        case "^":
            y -= 1
    match data[c+1]:
        case ">":
            r += 1
        case "v":
            s += 1
        case "<":
            r -= 1
        case "^":
            s -= 1
    presents[(x, y)] += 1
    presents[(r, s)] += 1

print(len(presents.keys()))
