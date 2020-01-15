
def main():
    _file = None
    try:
        _file = open('/Users/chenliang/chenliang/python/part2/text.txt', 'r', encoding = 'utf-8')
        print(_file.read())
    except FileNotFoundError:
        print('未找到')
    except FileExistsError:
        print('存在失败')
    except Exception:
        print('统一异常处理')
    finally:
        if _file:
            _file.close()
def main():
    try:
        #使用with标志上下文，上下文结束资源释放
        with open('/Users/chenliang/chenliang/python/part2/text.txt', 'r', encoding = 'utf-8') as f:
            print(f.read())
    except Exception:
        print('出错了')

import time


def main():
    # 一次性读取整个文件内容
    with open('/Users/chenliang/chenliang/python/part2/text.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('/Users/chenliang/chenliang/python/part2/text.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('/Users/chenliang/chenliang/python/part2/text.txt') as f:
        lines = f.readlines()
    print(lines)

from math import sqrt

def is_prime(n):
    """判断是否为素数"""
    for factor in range(2, int(sqrt(n))+1):
        if n % factor == 0:
            return False
        return True if n != 1 else False

def main():
    file_names = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for file_name in file_names:
            fs_list.append(open(file_name, 'w', encoding= 'utf-8'))
        for num in range(1,10000):
            if num < 100:
                fs_list[0].write(str(num) + '\n')
            if num < 1000:
                fs_list[1].write(str(num) + '\n')
            else:
                fs_list[2].write(str(num) + '\n')
    except Exception as e:
        print('错误信息', e)
    finally:
        for fs in fs_list:
            fs.close()
    print('ending')

"""
读写二进制(图片)
"""
def main():
    try:
        with open('guido.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # <class 'bytes'>
        with open('吉多.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开.')
    except IOError as e:
        print('读写文件时出现错误.')
    print('程序执行结束.')

if __name__ == '__main__':
    main()