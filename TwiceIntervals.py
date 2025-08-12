
from NesterovTwin import *


if __name__ == '__main__':
    ai = Interval(9.80, 9.86, sortQ=False)
    ai1 = Interval(9.78, 9.88, sortQ=False)
    ti = TwinNesterov(ai, ai1)
    ai2 = Interval(11.16, 11.22, sortQ=False)
    ai21 = Interval(11.14, 11.24, sortQ=False)
    ti2 = TwinNesterov(ai2, ai21)
    print("ti=", ti)
    print("ti2=", ti2)
    print("\n")
    #print("Nest ti+ti2=", ti+ti2)
    
    t=ti*ti2
    print("Nest t = ti*ti2=", t)
    ai3 = Interval(37.42, 37.48, sortQ=False)
    ai23 = Interval(37.40, 37.50, sortQ=False)
    ti3 = TwinNesterov(ai3, ai23)

    print("ti3=", ti3, "\n")
    print("Nest t*ti3=", t*ti3)
    #print("\n")
    #print("Nest ti+ti=", ti + ti)
    #print("Nest ti*ti=", ti * ti)