#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#汉诺塔的移动可以用递归函数非常简单地实现。
#请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：

#在递归的思想里，把问题简单化。
#n 个盘子，从 a 经过 b 移动到 c
#那分三步，

#把最上面 (n-1) 个盘子从a， 经过c 移动到b
#把1个盘子，从a 直接移动到 c
#把b 上的 n-1 个盘子从 b 经过 a 移动到c 至于怎么把 n-1个盘子移过去，那是另一层move干的事，我不管。
def move(n,a,b,c):
    if n==1:
        print(a, '-->',c)
    else:
        move(n-1, a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)


move(3,'A','B','C')