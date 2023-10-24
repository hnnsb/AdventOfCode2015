import re
from aocd.models import Puzzle
from os.path import basename

fileName = basename(__file__)
day = int(fileName.strip(r"day|.py"))
TEST = False
# -----------------------------------------------------
data = ""
with open(f"day02/input.txt", "r") as f:
    data = f.read()
data = data.splitlines()
data = list(map(lambda x: re.findall(r"\d+", x), data))
data = [list(map(int, l)) for l in data]

surface = list(map(lambda x: 2*x[0]*x[1] + 2*x[1]*x[2] + 2*x[2]
                   * x[0] + min(x[0]*x[1], x[1]*x[2], x[2]*x[0]), data))
print(sum(surface))

ribbons = list(map(lambda x: min(
    2*x[0]+2*x[1], 2*x[1]+2*x[2], 2*x[2]+2*x[0]) + x[0]*x[1]*x[2], data))
print(sum(ribbons))


# puzzle.answer_a =
# puzzle.answer_b =
