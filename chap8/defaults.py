def f(ta=[]):
    ta.append("1")
    return ta

print(f())
print(f())


def g(ta=None):
    if ta is None:
        ta = []
    ta.append("1")
    return ta

#print(g())
#print(g())




def newf():
    def f(ta=[]):
        ta.append("1")
        return ta
    return f

#f1 = newf()
#f2 = newf()
#print(f1())
#print(f1())
#print(f2())
#print(f2())





def resetdefaults(f):
    from copy import deepcopy
    def wrap(*args, **kwargs):
        f.defaults0 = deepcopy(f.__defaults__)
        res = f(*args, **kwargs)
        f.__defaults__ = f.defaults0
        return res
    return wrap


@resetdefaults
def h(ta=[]):
    ta.append("1")
    return ta

#print(h())
#print(h())

