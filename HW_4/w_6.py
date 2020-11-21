from itertools import count, cycle
from time import sleep

for i in count(27):
    if i > 31:
        break
    print(i)
    sleep(0.5)

sleep(1)

my_list = ['str', 'RTS', '1trs1']
x = 0
for i in cycle(my_list):
    if x > 8:
        break
    print(i)
    sleep(0.5)
    x += 1
