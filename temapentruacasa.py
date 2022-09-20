"a"
def suma(a,b):
    suma=a+b
    return print("Suma numerelor ",a," si ",b," = ",suma)
"b"
def produsul(a,b):
    produs=a*b
    return print(" Produsul numerelor ",a," si ",b," = ",produs)
"c"
def media(a,b):
    media=(a+b)/2
    return print(" Media aritmetica a numerelor ",a," si ",b," = ",media)
"d"
def cel_mai_mare_divizor(a,b):
    w=[]
    z=[]
    for i in range (1,a+1):
        if (a%i==0):
            w.append(i)
    for j in range (1,b+1):
        if (b%j==0):
            z.append(j)
    c=set(w).intersection(z)
    g=max(c)
    return print(" Cel mai mare divizor comun al numerelor ",a," si ",b," = ",g)
"e"
def cel_mai_mic_multiplu_c(a,b):
    if a>b:
        mp=a
    elif b>a:
        mp=b
    else:
        mp=a
    while True:
        if ((mp%a==0)and(mp%b==0)):
            comun=mp
            break
        mp +=1
    return print("Cel mai mic multiplu comun al numerelor ",a," si ",b," = ",comun)
"f"
def minim(a,b):
    if a<b :
        min=a
    else:
        min=b 
    return print(" Numarul minim =",a)
"g"
def maxim(a,b):
    if a>b :
        max=a
    else:
        max=b  
    return print(" Numarul maxim =",b)
"h"
def suma_numarul_2():
    a= int(input('Introduceti primul  numar: '))
    b= int(input('Introduceti al doilea numar: '))
    c=a+b
    return print("suma= ",a," + ",b," = ",c)
"i"
def produsul_numarul_2():
    a=int(input('Introduceti primul nr: '))  
    b=int(input('Introduceti al doilea nr: '))  
    c=a*b
    return print("produsul= ",a," * ",b," = ",c)
"j"
def divizori(a,b):
    x=[]
    y=[]
    for i in range (1,a+1):
        if (a%i==0):
            x.append(i)
    for j in range (1,b+1):
        if (b%j==0):
            y.append(j)
    c=set(x).intersection(y)
    q=list(c)
    return print("divizorii comuni lui ",a," si ",b," = ",q)
"k"
def cinci_mp(a,b):
    multiplii=[]
    if a>b:
        mp=a
    elif b>a:
        mp=b
    else:
        mp=a
    while len(multiplii)<5:
        if ((mp%a==0)and(mp%b==0)):
            multiplii.append(mp)
            mp +=1
        else:
            mp+=1
    return print("5 multipli comuni ale lui",a," si ",b," sunt=",multiplii)
"l"
def cifre_comune(x,y):
    o=[]
    p=[]
    for i in str(x):
        o.append(int(i))
    for k in str(y):
        p.append(int(k))
    comuni=set(o).intersection(p)
    t=list(comuni)
    if len(t)!=0:
        return print("l) Cifrele comune care se contin in nr ",o," si ",p," sunt: ",cifre_comune(o,p))
"m"
def cifrele_diferite(a,b):
    u=[]
    v=[]
    for i in str(a):
        u.append(int(i))
    for n in str(b):
        v.append(int(n))
    comuni=set(u).difference(v)
    l=list(comuni)
    return print("cifrele care se contin in numarul ",a," si nu se contin in numarul ",b," = ",l)

"n"
def num_divizor (a,b):
    x=[]
    z=[]
    for i in range (1,a+1):
        if (a%i==0):
            x.append(i)
    for n in range (1,b+1):
        if (b%n==0):
            z.append(n)
    if len(x)==len(z):
        return print("nr sunt PRIETENE")
    else:
        return print("nr nu sunt PRIETENE") 
num1= int(input('dati num1='))
num2= int(input('dati num2='))
#a
suma(num1,num2)
#b
produsul(num1,num2)
#c
media(num1,num2)
#d
cel_mai_mare_divizor(num1,num2)
#e
cel_mai_mic_multiplu_c(num1,num2)
#f
minim(num1,num2)
#g
maxim(num1,num2)
#h
divizori(num1,num2)
#i
cinci_mp(num1,num2)
#j
cifre_comune(num1,num2)
#k
cifrele_diferite(num1,num2)
#l
num_divizor(num1,num2)
#m
suma_numarul_2()
#n
produsul_numarul_2()
