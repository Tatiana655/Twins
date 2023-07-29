from intvalpy import *
import math as m


def galka(x: RealInterval.ArrayInterval, y: RealInterval.ArrayInterval):
    return Interval(min(x.a, y.a), max(x.b, y.b), sortQ=False)


def dual_domik(x: RealInterval.ArrayInterval, y: RealInterval.ArrayInterval):
    return Interval(min(x.b, y.b), max(x.a, y.a), sortQ=False)


class TwinSainz(object):
    # добавить перевод из одного типа в другой! + дока
    def __init__(self, X_in: RealInterval.ArrayInterval, X_ex: RealInterval.ArrayInterval):
        if hasattr(X_in, 'len') or hasattr(X_ex, 'len'):
            print("I1 or I2 is not single intervals. Check your data.")
            exit()

            # print(X_in.a, X_ex.b)
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
        # print("X_in=", self.X_in, "; x_ex=", other.X_ex.dual)
        # in1 = self.X_in + other.X_in.dual
        # in2 = other.X_in + self.X_in.dual
        return TwinSainz(galka(galka(self.X_in.a + other.X_in, self.X_in.b + other.X_in),
                               galka(other.X_in.a + self.X_in, other.X_in.b + self.X_in)),
                         self.X_ex + other.X_ex)

    def __rmul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return TwinSainz(other * self.X_in, other * self.X_ex)

    def __mul__(self, other):
        # in1 = self.X_in * other.X_ex.dual
        # in2 = other.X_in * self.X_ex.dual
        # print(self.X_in * other.X_in)
        # print("my *", TwinNesterov(galka(in1, in2), self.X_ex * other.X_ex))
        if isinstance(other, float) or isinstance(other, int):
            return TwinSainz(other * self.X_in, other * self.X_ex)
        return TwinSainz(galka(galka(self.X_in.a * other.X_in, self.X_in.b * other.X_in),
                               galka(other.X_in.a * self.X_in, other.X_in.b * self.X_in)), self.X_ex * other.X_ex)

    def __neg__(self):
        return TwinSainz(-self.X_in, -self.X_ex)

    def __invert__(self):
        if 0 in self.X_in or 0 in self.X_ex:
            print("ERROR:Cannot be divided into intervals containing 0.")
            exit()

        return TwinSainz(1 / self.X_in, 1 / self.X_ex)

    def __eq__(self, other):
        if self.X_in.a == other.X_in.a and self.X_in.b == other.X_in.b and self.X_ex.a == other.X_ex.a and self.X_ex.b == other.X_ex.b:
            return True
        else:
            return False
