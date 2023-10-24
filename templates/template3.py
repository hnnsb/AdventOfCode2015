from collections import Counter
from aocd.models import Puzzle
from os.path import basename
from dotenv import DotEnv
config = DotEnv()

fileName = basename(__file__)
day = int(fileName.strip(r"day|.py"))
puzzle = Puzzle(day=day, year=config.get("YEAR"))
TEST = False
# -----------------------------------------------------
data = puzzle.input_data
if TEST:
    with open(f"day{day}/test.txt", "r") as f:
            data = f.read()
data = data.splitlines()

print(data)

# puzzle.answer_a =
# puzzle.answer_b =
