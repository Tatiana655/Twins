from NesterovTwin import *
from SainzTwin import *

if __name__ == '__main__':
    ai = Interval(3, 5, sortQ=False)
    ai1 = Interval(1, 5, sortQ=False)
    ti = TwinSainz(ai, ai1)
    ai2 = Interval(4, 4.25, sortQ=False)
    ai21 = Interval(3.5, 4.5, sortQ=False)
    ti2 = TwinSainz(ai2, ai21)
    print("ti=", ti)
    print("ti2=", ti2)
    print("\n")
    print("Nest ti+ti2=", ti + ti2)
    print("Nest ti*ti2=", ti * ti2)
    print("\n")
    print("Nest ti+ti=", ti + ti)
    print("Nest ti*ti=", ti * ti)

    '''ai = Interval(3, 5, sortQ=False)
    ai1 = Interval(1, 5, sortQ=False)
    ti = TwinNesterov(ai, ai1)
    ai2 = Interval(4, 4.25, sortQ=False)
    ai21 = Interval(3.5, 4.5, sortQ=False)
    ti2 = TwinNesterov(ai2, ai21)
    print("ti=", ti)
    print("ti2=", ti2)
    print("\n")
    print("Nest ti+ti2=", ti+ti2)
    print("Nest ti*ti2=", ti*ti2)
    print("\n")
    print("Nest ti+ti=", ti + ti)
    print("Nest ti*ti=", ti * ti)'''
