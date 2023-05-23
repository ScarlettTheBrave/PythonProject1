import sys

for p in sys.path:
print(p)

from sys import path

path.append('...\\module’)

import module

print(module.counter)


from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))