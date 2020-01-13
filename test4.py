"""
判断素数
"""
from math import sqrt

number = int(input("输入素数："))
end = int(sqrt(number))
is_prime = True
for x in range(2, end + 1):
    if number % x == 0:
        is_prime = False
        break
if is_prime and number != 1:
    print("%d是素数" % number)
else:
    print("%d不是素数" % number)

"""
最大公约数和最小公倍数
"""
x = int(input('x = '))
y = int(input('y = '))
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break

"""
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
"""

row = 4
for x in range(row):
    for y in range(x + 1):
        print('*', end='')
    print()

for x in range(row):
    for y in range(row):
        if y < row - x - 1:
            print(' ', end = '')
        else:
            print('*', end = '')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()

