from collections import Counter
from aocd.models import Puzzle
from os.path import basename
from dotenv import DotEnv
config = DotEnv()

fileName = basename(__file__)
day = int(fileName.strip(r"day|.py"))
TEST = False
# -----------------------------------------------------
data = ""
with open(f"day01/input.txt", "r") as f:
    data = f.read()

if TEST:
    with open(f"day01/test.txt", "r") as f:
        data = f.read()

counter = Counter(data)
print(counter["("] - counter[")"])

level = 0
for i, c in enumerate(data, start=1):
    if c == "(":
        level += 1
    if c == ")":
        level -= 1
    if level < 0:
        print(i)
        break
