import random
import time
import copy

# 冒泡
def fun1(lis):
    for j in range(len(lis)):
        for i in range(len(lis) - 1):
            if lis[i] > lis[i + 1]:
                lis[i], lis[i + 1] = lis[i + 1], lis[i]

    return lis


# 选择
def fun2(lis):
    num = len(lis)
    for i in range(num):
        min = lis[i]
        a = i
        for j in range(i + 1, num):
            if lis[j] < min:
                min = lis[j]
                a = j
        lis[i], lis[a] = min, lis[i]

    return lis


# 快排
def fun3(lis):
    if len(lis) <= 1:
        return lis
    else:
        a = lis[0]
        lis_r = [i for i in lis[1:] if i > a]
        lis_l = [i for i in lis[1:] if i <= a]
    return fun3(lis_l) + [a] + fun3(lis_r)


# 插入
def fun4(lis):
    lis_out = []
    lis_out.append(lis[0])
    for i in range(1, len(lis)):
        for j in range(len(lis_out)):
            if lis[i] < lis_out[j]:
                lis_out.insert(j, lis[i])
                break
            if j == len(lis_out) - 1:
                lis_out.append(lis[i])
    return lis_out


# 归并 lis = [23, 5, 34, 2, 35, 6, 15, 12, 24, 1]
def fun_split(lis):
    if len(lis) <= 1:
        return lis
    mid = len(lis) // 2
    left = fun_split(lis[:mid])
    right = fun_split(lis[mid:])
    return merge(left, right)


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


#计数排序
def fun5(lis):
    min = lis[0]
    max = 0
    for li in lis:
        if li > max:
            max = li
        if li < min:
            min = li

    count = [0] * (max - min + 1)
    for li in lis:
        count[li - min] += 1
    lis = []
    for i in range(len(count)):

        if count[i] == 0:
            continue
        for j in range(count[i]):
            lis.append(i + min)

    return lis


# 斐波那契数列
def fun(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    s = fun(x - 1) + fun(x - 2)
    return s


def fun_print(x):
    for i in range(x):
        print(fun(i), end=' ')

# print(fun(6))
# fun_print(11)
# lis = [2, 5, 34, 66, 52, 1, 2, 3, 4, 13, 22, 14, 5, 5]
lis = [random.randint(1, 1000) for i in range(50)]
# print(lis)
# list1 = copy.deepcopy(lis)
# list2 = copy.deepcopy(lis)
# list3 = copy.deepcopy(lis)
# list4 = copy.deepcopy(lis)
# list5 = copy.deepcopy(lis)
list6 = copy.deepcopy(lis)
# list7 = copy.deepcopy(lis)


def fun_sort(lis):
    lis.sort()


def count_time(fun, list, num):
    start_time = time.time()
    for i in range(num):
        fun(list)
    end_time = time.time()
    return end_time - start_time


# print('冒泡排序执行结果：', fun1(list1))
# print('选择排序执行结果：', fun2(list2))
# print('快速排序执行结果：', fun3(list3))
# print('插入排序执行结果：', fun4(list4))
# print('计数排序执行结果：', fun5(list5))
# print('归并排序执行结果：', fun_split(list6))
# print('sort排序执行结果：', fun_split(list6))

# time_out = count_time(fun1, list1, 1)
# print('冒泡排序执行时间：{}'.format(time_out))
# time_out = count_time(fun2, list2, 1)
# print('选择排序执行时间：{}'.format(time_out))
# time_out = count_time(fun3, list3, 1)
# print('快速排序执行时间：{}'.format(time_out))
# time_out = count_time(fun4, list4, 1)
# print('插入排序执行时间：{}'.format(time_out))
# time_out = count_time(fun5, list5, 1)
# print('计数排序执行时间：{}'.format(time_out))
# time_out = count_time(fun_split, list6, 1)
# print('归并排序执行时间：{}'.format(time_out))
# time_out = count_time(fun_sort, list6, 1)
# print('sort排序执行时间：{}'.format(time_out))


def split(lis):
    if len(lis) == 1:
        return lis
    mid = len(lis) // 2

    left = split(lis[:mid])
    right = split(lis[mid:])
    return merges(left, right)


def merges(left, right):
    lis = []
    while left and right:
        if left[0] < right[0]:
            lis.append(left.pop(0))
        else:
            lis.append(right.pop(0))
    while left:
        lis.append(left.pop(0))
    while right:
        lis.append(right.pop(0))
    return lis

print(lis)




def fun(lis):
    if len(lis) <= 1:
        return lis
    r = lis[0]
    left = [i for i in lis[1:] if i<=r]
    right = [i for i in lis[1:] if i>r]
    return fun(left) + [r] + fun(right)


print(fun(lis))
