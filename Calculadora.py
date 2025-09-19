
def sumar(a , b):
    return a + b

def restar( a , b ):
    return a - b

def multiplicar( a, b):
    return a * b

def dividir( a , b):
    if b == 0:
        raise ValueError('error al dividir por cero')
    return a / b

def calculadora_simple( operacion , a, b):
        if operacion == 'sumar':
            return sumar(a,b)
        elif operacion == 'restar':
            return restar(a,b)
        elif operacion == 'multiplicar':
            return multiplicar(a,b)
        elif operacion == 'dividir':
            return dividir(a,b)
        else:
            return KeyError(' OPERACION INVALIDA')

print(calculadora_simple("restar" ,400,2))