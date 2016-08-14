import sys
import re
from functools import cmp_to_key


def len_sort(a, b):
    return len(a) - len(b)

n = int(input().strip())
n = bin(n)[2::]


test = re.split("0+", n)


result = sorted(test, key=cmp_to_key(len_sort))
print(len(result.pop()))