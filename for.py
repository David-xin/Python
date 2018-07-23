#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sum = 0
for x in range(101):
    sum = sum + x
print(sum)


sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

#请利用循环依次对list中的每个名字打印出Hello, xxx!：

L=['Bart', 'Lisa', 'Adam']

for name in L:
    print('Hello,%s' % name)
