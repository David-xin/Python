#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

#ax2 + bx + c = 0

#的两个解。

import math

def quadratic(a,b,c):
    D = pow(b, 2) - 4*a*c
    if a==0 or D < 0:
        pass
    elif D==0:
        x1 = x2 = -b/(a*2)
        return x1, x2
    elif D > 0:
        sqrt = math.sqrt(D)
        x1 = ((-b)+sqrt)/(2*a)
        x2 = ((-b)-sqrt)/(2*a)
        return x1, x2

a = int(input('Please input a value:'))
b = int(input('Please input b value:'))
c = int(input('Please input c value:'))
S = quadratic(a, b, c)
if S is None:
    print('Equation %sx2+%sx+%s=0 no real root' % (a,b,c))
elif b==0:
    if S[0] == S[1]:
        print('Equation %sx2+%s=0 real root is x1=x2=%s' %(a,c,S[0]))
    else:
        print('Equation %sx2+%s=0 real root is x1=%s x2=%s' %(a,c,S[0],S[1]))
else:
    if S[0]==S[1]:
        print('Equation %sx2+%sx+%s=0 real root is x1=%s' %(a,b,c,S[0]))
    else:
        print('Equation %sx2+%sx+%s=0 real root is x1=%s x2=%s' %(a,b,c,S[0],S[1]))