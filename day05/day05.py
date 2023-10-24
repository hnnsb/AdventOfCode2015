import re
from collections import Counter
from aocd.models import Puzzle
from os.path import basename
from dotenv import DotEnv
config = DotEnv()

fileName = basename(__file__)
day = int(fileName.strip(r"day|.py"))
# -----------------------------------------------------
data = ""
with open(f"day05/input.txt", "r") as f:
    data = f.read()
data = data.splitlines()

vowels = set("aeiou")
not_allowed = ["ab", "cd", "pq", "xy"]


def niceString(string):
    for substring in not_allowed:
        if substring in string:
            return False
    return len(re.findall(r"[aeiou]", string)) >= 3 and len(
        re.findall(r"([a-z])\1", string)) >= 1


nice_strings = list(map(niceString, data))
print(sum(nice_strings))


def niceString2(string):
    return len(re.findall(r"([a-z]{2}).*\1", string)) > 0 and len(re.findall(r"(.).\1", string)) > 0


nice_strings2 = list(map(niceString2, data))
print(sum(nice_strings2))
