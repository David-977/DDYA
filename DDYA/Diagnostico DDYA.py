def main():
    num=pedir_numero()
    positivo_negativo(num)
    par_impar(num)
    numero_fibo(num)
    primo(num)
    sumar_intermedios(num)
    codigo_estudiante()
    mes=fecha_codigo()
    vocales_consonantes(mes)
    posicion_abecedario(mes)


def pedir_numero():
    cant=int(input("Cuantos numeros vas a ingresar?: "))
    num=[]
    for rep in range(cant):
        n=int(input("Coloque su numero: "))
        num.append(n)
    return num

def par_impar(num):
    print("Punto 2")
    for n in num:
        if n%2==0:
            print("Su numero",n,"es par")
            print("Elevado al cubo:",n**3)
        else:
            print("Su numero",n,"es impar")
            print("Elevado al cuadrado:",n**2)


def primo(num):
    print("Punto 4")
    for n in num:
        if n<=1:
            print("Su numero",n,"no es primo")
        else:
            es_primo=True

            for rep in range(2,int(n**0.5)+1):
                if n%rep==0:
                    es_primo=False
            if es_primo:
                print("Su numero",n,"es primo")
            else:
                print("Su numero",n,"no es primo")


def positivo_negativo(num):
    print("Punto 1")
    for n in num:
        if n==0:
            print("Su numero es 0")
        elif n>0:
            print("Su numero",n,"es positivo")
        else:
            print("Su numero",n,"es negativo")


def numero_fibo(num):
    print("Punto 3")
    for n in num:
        a=0
        b=1
        while b<n:
            c=a+b
            a=b
            b=c
        if b==n or n==0:
            print("Su numero",n,"pertenece a Fibonacci")
        else:
            print("Su numero",n,"no pertenece a Fibonacci")


def sumar_intermedios(num):
    print("Punto 5")
    if len(num)!=2:
        print("Para este punto debe ingresar exactamente 2 numeros")
    else:
        n1=num[0]
        n2=num[1]
        suma=0
        if n1<n2:
            for rep in range(n1+1,n2):
                suma=suma+rep
        else:
            for rep in range(n2+1,n1):
                suma=suma+rep
        print("Numeros intermedios=",suma)


def codigo_estudiante():
    print("Punto 7")
    codigo=1000116646
    lista=[codigo]
    positivo_negativo(lista)
    par_impar(lista)
    numero_fibo(lista)
    primo(lista)


def fecha_codigo():
    print("Punto 8")
    codigo=1000116646
    fecha="14septiembre"
    entrada=fecha+str(codigo)
    print("Entrada:",entrada)

    mes=entrada[2:12]
    print("Mes:",mes)
    numero=[codigo]
    
    positivo_negativo(numero)
    par_impar(numero)
    numero_fibo(numero)
    primo(numero)

    return mes


def vocales_consonantes(mes):
    print("Punto 9")
    vocales="aeiou"
    for letra in mes:
        if letra in vocales:
            print(letra,"es vocal")
        else:
            print(letra,"es consonante")


def posicion_abecedario(mes):
    print("Punto 10")
    abecedario="abcdefghijklmnopqrstuvwxyz"

    for letra in mes:
        posicion=abecedario.index(letra)+1
        print(letra,"-",posicion)


main()