from numpy import sin, cos, pi

erro = 0.0001


def f(x):
    return x*cos(x)


def Df(x):
    return cos(x) - x*sin(x)


def mtd_bissec(a=0, b=pi/2):
    c = (a+b)/2
    if (abs(Df(c)) < erro):
        return f(c)
    if (Df(a)*Df(c) < 0):
        return mtd_bissec(a, c)
    elif (Df(b)*Df(c) < 0):
        return mtd_bissec(b, c)
    else:
        return print("O metodo não convergiu")


print(f"A área máxima é: {mtd_bissec():.6f}")
