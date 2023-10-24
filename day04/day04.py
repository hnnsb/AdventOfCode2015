import hashlib
from collections import Counter
from aocd.models import Puzzle
from os.path import basename
from dotenv import DotEnv
config = DotEnv()

fileName = basename(__file__)
day = int(fileName.strip(r"day|.py"))
TEST = False
# -----------------------------------------------------

data = "yzbqklnj"
number = 0
while con := True:
    result = hashlib.md5((data+str(number)).encode("UTF-8"))
    res_string = str(result.hexdigest())
    if res_string.startswith("000000"):
        print(res_string)
        print(number)
        break
    number += 1
