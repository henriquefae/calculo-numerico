from numpy import sin, cos, pi

erro = 0.0001


def f(x):
    return 9/sin((125+x)*pi/180) + 7/sin((x)*pi/180)


def Df(x):
    return -9*cos((125+x)*pi/180)/(sin((125+x)*pi/180))**2 - 7*cos(x*pi/180)/(sin((x)*pi/180))**2


def mtd_bissec(a=0.1, b=54.9):
    c = (a+b)/2
    if (abs(Df(c)) < erro):
        return c
    if (Df(a)*Df(c) < 0):
        return mtd_bissec(a, c)
    elif (Df(b)*Df(c) < 0):
        return mtd_bissec(c, b)
    else:
        return print("O metodo não convergiu")


L = f(mtd_bissec())

print(f"O comprimento máximo é {L:.6f}")
