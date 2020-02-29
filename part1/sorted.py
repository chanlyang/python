# 选择排序
def selection(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print(arr)


# 冒泡排序
def bubble(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


# 插入排序
def insertion(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    print(arr)


# 希尔排序
def shell(arr):
    h = 1
    while h < (len(arr) // 3):
        h = h * 3 + 1
    while h > 0:
        for i in range(h, len(arr)):
            j = i
            while j >= h and arr[j] < arr[j - h]:
                arr[j], arr[j - h] = arr[j - h], arr[j]
                j -= h
        h = h // 3
    return arr


import math


# 归并排序
def mergeSort(arr):
    if (len(arr) < 2):
        return arr
    middle = math.floor(len(arr) / 2)
    left, right = arr[0:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


# 快速排序
def quick(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    if left < right:
        pivot = partition(arr, left, right)
        quick(arr, left, pivot - 1)
        quick(arr, pivot + 1, right)
    return arr


def partition(arr, left, right):
    povit = left
    index = povit + 1
    for i in range(index, right + 1):
        if arr[i] < arr[povit]:
            arr[i], arr[index] = arr[index], arr[i]
            index += 1
    arr[povit], arr[index - 1] = arr[index - 1], arr[povit]
    return index - 1


# 计数排序
def count(arr, max):
    bucketLen = max + 1
    bucket = [0] * bucketLen
    for i in range(len(arr)):
        if not bucket[arr[i]]:
            bucket[arr[i]] = 0
        bucket[arr[i]] += 1
    sortedIndex = 0
    for j in range(bucketLen):
        while bucket[j] > 0:
            arr[sortedIndex] = j
            sortedIndex += 1
            bucket[j] -= 1
    print('计数：', arr)


def main():
    arr = [2, 1, 3, 5, 3, 2, 1, 3, 5, 3, 1, 6, 7, 4, 9, 8, 5, 3, 7, 6]
    # selection(arr)
    # bubble(arr)
    # insertion(arr)
    # shell(arr)
    # result = mergeSort(arr)
    #result = quick(arr)
    #print(result)
    count(arr,max(arr))


if __name__ == '__main__':
    main()
