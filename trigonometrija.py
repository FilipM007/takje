import math
import time
print("ako je vrijednost nepoznata unesi 0")
alfa=float(input("alfa: "))
beta=float(input("beta: "))
a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))
opseg=float(input("opseg: "))
povrsina=float(input("povrsina: "))
lista=["alfa", "beta", "a", "b", "c", "opseg", "površina"]
gotovo=False
brojac=0


if alfa!=0 and beta!=0 and a!=0 and b!=0 and c!=0 and opseg!=0 and povrsina!=0 or beta==0 and a==0 and b==0 and c==0 and opseg==0 and povrsina==0:
    gotovo=True
    print("NEMOŽE")


while not gotovo and brojac<7:
    for traženo in lista:
        if traženo=="alfa" and alfa==0:
            # zbroj kutova
            if beta != 0:
                alfa = 90 - beta
                brojac=0
            #sinus
            elif a!=0 and c!=0:
                sin_alfa = a / c
                kutalfa = math.asin(sin_alfa)
                alfa_stupnjevi = math.degrees(kutalfa)
                alfa = alfa_stupnjevi
                brojac = 0
            # cosinus
            elif b!=0 and c!=0:
                cos_alfa = b/c
                kutalfa = math.acos(cos_alfa)
                alfa_stupnjevi = math.degrees(kutalfa)
                alfa = alfa_stupnjevi
                brojac = 0
            #tanges
            elif a!=0 and b!=0:
                tan_alfa = a/b
                kutalfa = math.atan(tan_alfa)
                alfa_stupnjevi = math.degrees(kutalfa)
                alfa = alfa_stupnjevi
                brojac = 0
        elif traženo=="beta" and beta==0:
            # zbroj kutova
            if alfa!=0:
                beta=90-alfa
                brojac = 0
            # sinus
            elif b != 0 and c != 0:
                sin_beta = b / c
                kutbeta = math.asin(sin_beta)
                beta_stupnjevi = math.degrees(kutbeta)
                beta = beta_stupnjevi
                brojac = 0
            # cosinus
            elif a != 0 and c != 0:
                cos_beta = a / c
                kutbeta = math.acos(cos_beta)
                beta_stupnjevi = math.degrees(kutbeta)
                beta = beta_stupnjevi
                brojac = 0
            # tanges
            elif b != 0 and a != 0:
                tan_beta = b / a
                kutbeta = math.atan(tan_beta)
                beta_stupnjevi = math.degrees(kutbeta)
                beta = beta_stupnjevi
                brojac = 0
        elif traženo == "a" and a==0:
            #povrsina
            if povrsina!=0 and b!=0:
                a=(povrsina/b)*2
                brojac = 0
            #sinus
            elif alfa!=0 and c!=0:
                kut = math.radians(alfa)
                a=math.sin(kut)*c
                a=abs(a)
                brojac = 0
            #kosinus
            elif beta!=0 and c!=0:
                kut = math.radians(beta)
                a = math.cos(kut) * c
                a = abs(a)
                brojac = 0
            #tanges
            elif alfa!=0 and b!=0:
                kut = math.radians(alfa)
                a = math.tan(kut) * b
                a = abs(a)
                brojac = 0
            # pitagora
            elif b != 0 and c != 0:
                a = (c * c) - (b * b)
                a = math.sqrt(a)
                brojac = 0
        elif traženo == "b" and b==0:
            # povrsina
            if povrsina != 0 and a != 0:
                b = (povrsina / a) * 2
                brojac = 0
            # sinus
            elif beta != 0 and c != 0:
                kut = math.radians(beta)
                b = math.sin(kut) * c
                b = abs(b)
                brojac = 0
            # kosinus
            elif alfa != 0 and c != 0:
                kut = math.radians(alfa)
                b = math.cos(kut) * c
                b = abs(b)
                brojac = 0
            # tanges
            elif beta != 0 and a != 0:
                kut = math.radians(beta)
                b = math.tan(kut) * b
                b = abs(b)
                brojac = 0
            # pitagora
            elif a != 0 and c != 0:
                b = (c * c) - (a * a)
                b = math.sqrt(b)
                brojac = 0
        elif traženo == "c" and c==0:
            # sinus
            if alfa != 0 and a != 0:
                kut = math.radians(alfa)
                c = a / math.sin(kut)
                c = abs(c)
                brojac = 0
            # kosinus
            elif alfa != 0 and b != 0:
                kut = math.radians(alfa)
                c = b / math.cos(kut)
                c = abs(c)
                brojac = 0
                # pitagora
            elif a != 0 and b != 0:
                c = (a * a) + (b * b)
                c = math.sqrt(c)
                brojac = 0
        elif traženo=="opseg":
            if a!=0 and b!=0 and c!=0:
                opseg=a+b+c
                brojac = 0
        elif traženo=="površina":
            if a!=0 and b!=0:
                povrsina=(a*b)/2
                brojac = 0
        else:
            brojac+=1
        if alfa != 0 and beta != 0 and a != 0 and b != 0 and c != 0 and opseg!= 0 and povrsina!= 0:
            gotovo = True
if brojac>=7:
    print("NEMOŽE")
else:
    print("alfa: ", alfa)
    print("beta: ", beta)
    print("a: ", a)
    print("b: ", b)
    print("c: ", c)
    print("opseg: ", opseg)
    print("povrsina: ", povrsina)
time.sleep(10)







