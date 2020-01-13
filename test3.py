""" 
测试if else
"""
user_name = str(input("输入用户名："))
pass_word = str(input("输入密码:"))
if user_name == 'admin' and pass_word == '123':
    print(True)
else:
    print(False)


"""
分段函数求值

        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
"""

x = float(input("请输入参数："))
if x > 1 :
    y = 3 * x - 5
elif x <= 1 and x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print("f(%.2f)=%.2f" % (x, y))  

from random import randint

face = randint(1,2)
if face == 1 :
    print("这是1")
else :
    print("这是2")

sum = 0
for x in range(10):
    sum += x
print(sum)

"""
猜数游戏
"""
import random
answer = random.randint(1,100)
counter = 0
while True:
    counter += 1
    number = int(input("输入你猜的数:"))
    if number > answer:
        print("猜大了")
    elif number < answer:
        print("猜小了")
    else:
        print("猜对了")
        break
print("你用了%d次" % counter)

""" 
九九乘法表
"""
for i in range(1,10):
    for j in range(1, i+1):
        print("%d*%d=%d" % (i , j , i * j) , end = "\t")
    print()
