#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：

def product(*num):
    if len(num) <= 0:#检测输出参数的个数
        raise TypeError('Please input num!')
    sum=1
    for x in num:
        if not isinstance(x, (int, float)):#检测输入参数的类型
            raise TypeError("Error Type, Numbers only!")
        sum*=x
    return sum

print('product(5)=',product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')