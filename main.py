from intvalpy import *
import math as m

def galka(x:RealInterval.ArrayInterval,y:RealInterval.ArrayInterval):
    return Interval(min(x.a, y.a), max(x.b, y.b), sortQ=False)

def dual_domik(x:RealInterval.ArrayInterval, y:RealInterval.ArrayInterval):
    return Interval(min(x.b, y.b), max(x.a, y.a), sortQ=False)

class TwinNesterov(object):
    def __init__(self, X_in : RealInterval.ArrayInterval, X_ex : RealInterval.ArrayInterval):
        #добавить чекалку на вложенность

        #if not (X_in in X_ex):
        #    print("check the insertion")
        #    exit()

        if hasattr(X_in, 'len') or hasattr(X_ex, 'len'):
            print("I1 or I2 is not single intervals. Check your data.")
            exit()

        #print(X_in.a, X_ex.b)
        if m.isnan(float(X_in.a)) or m.isnan(float(X_ex.b)):
            print("The outer interval cannot be empty.")
            exit()

        self.X_in = X_in

        if (m.isnan(X_in.a) or m.isnan(X_in.b)) and X_ex.a == X_ex.b:
            self.X_in = X_ex

        self.X_ex = X_ex

    def __str__(self):
        return "[" + str(self.X_in) + ", " + str(self.X_ex) + "]"

    def __add__(self, other):
        #print("X_in=", self.X_in, "; x_ex=", other.X_ex.dual)
        in1 = self.X_in + other.X_ex.dual
        in2 = other.X_in + self.X_ex.dual
        print("my +", TwinNesterov(galka(in1, in2), self.X_ex + other.X_ex))
        return TwinNesterov(galka(dual_domik(self.X_in.a + other.X_ex, self.X_in.b + other.X_ex), dual_domik(other.X_in.a + self.X_ex, other.X_in.b + self.X_ex)), self.X_ex + other.X_ex)


    def __mul__(self, other):
        in1 = self.X_in * other.X_ex.dual
        in2 = other.X_in * self.X_ex.dual
        print("my *", TwinNesterov(galka(in1, in2), self.X_ex * other.X_ex))
        return TwinNesterov(galka(dual_domik(self.X_in.a * other.X_ex, self.X_in.b * other.X_ex), dual_domik(other.X_in.a * self.X_ex, other.X_in.b * self.X_ex)), self.X_ex * other.X_ex)

    def __neg__(self):
        return TwinNesterov(-self.X_in, -self.X_ex)

    def __invert__(self):
        if 0 in self.X_in or 0 in self.X_ex:
            print("ERROR:Cannot be divided into intervals containing 0.")
            exit()

        return TwinNesterov(1 / self.X_in, 1 / self.X_ex)

    def __eq__(self, other):
        if self.X_in.a == other.X_in.a and self.X_in.b == other.X_in.b and self.X_ex.a == other.X_ex.a and self.X_ex.b == other.X_ex.b:
            return True
        else:
            return False

if __name__ == '__main__':
    ai = Interval(3, 5, sortQ=False)
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
    print("Nest ti*ti=", ti * ti)





