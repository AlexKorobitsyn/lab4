import math


def f(x):
    return math.sqrt(1+x**4)

def method_trapezoids(h:int, b:int, a:int, f):
    step = a
    res = 0
    res += f(a)/2
    while abs(step - b) > 1e-9:
        step += h
        res += f(step)
    res += f(b)/2
    res *= h
    return  res
print("Метод Трапеций")
print("h = 0.1 ;\tI[f] =", method_trapezoids(0.1, 2, 1, f))
print("h = 0.05 ;\tI[f] =",method_trapezoids(0.05, 2, 1, f))
print("h = 0.025 ;\tI[f] =",method_trapezoids(0.025, 2, 1, f))


def method_cubic_parabolas(h:int, b:int, a:int, f):
    res = 0
    res += f(a)
    step = a
    counter = 0
    while abs(step - b) > 1e-9:
        step += h
        counter += 1
        counter %= 3
        if counter == 2:
            res += 2 * f(step)
        else:
            res += 3 * f(step)
    res += f(b)
    return 3*h/8*res
print("Метод 3/8")
print("h = 0.1 ;\tI[f] =", method_cubic_parabolas(0.1, 2, 1, f))
print("h = 0.05 ;\tI[f] =",method_cubic_parabolas(0.05, 2, 1, f))
print("h = 0.025 ;\tI[f] =",method_cubic_parabolas(0.025, 2, 1, f))
