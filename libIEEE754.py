import time


def to_ieee754(number):
    inicio = time.time()
    signal = 0
    if number < 0 :
        signal = 1
        number = number * (-1)
    p = 30

    dec = to_binary(number, positions = p)
    first_point = dec.find('.')
    first_numberOne = dec.find('1')

    if first_numberOne > first_point :
        dec = dec.replace('.', '')
        first_numberOne -= 1
        first_point -= 1
    elif first_numberOne < first_point :
        dec = dec.replace('.', '')
        first_point -= 1
        mantissa = dec[first_numberOne + 1:]

    exponent = first_point - first_numberOne
    exponent_bits = exponent + 127

    exponent_bits = bin(exponent_bits).replace('0b', '')

    mantissa = mantissa[0:23]

    final = str(signal) + exponent_bits.zfill(8) + mantissa
    fim = time.time()
    print('Funcao to_ieee754 - Tempo de execução: ', (fim-inicio))
    return final

    

def to_binary(number, positions = 3):
    inicio = time.time()
    inteiro, decimal = str(number).split(".")
    inteiro = int(inteiro)
    result = (str(bin(inteiro)) + ".").replace('0b', '')

    for _ in range(positions):
        decimal = str('0.') + str(decimal)
        timer = '%1.20f' % (float(decimal) * 2)
        inteiro, decimal = timer.split(".")
        result += inteiro 
    fim = time.time()
    print('Funcao to_binary - Tempo de execução: ', (fim-inicio))
    return result

def to_int(mantissa):
    potencia = -1
    valor_mantissa = 0

    for i in mantissa:
        valor_mantissa += (int(i) * pow(2, potencia))
        potencia -= 1
    return (valor_mantissa + 1)       


def to_float(ieee_32):
    inicio = time.time()
    bit_signal = int(ieee_32[0])

    expoente_bias = int(ieee_32[1 : 9], 2)
    expoente_unbias = expoente_bias - 127

    mantissa_str = ieee_32[9 : ]
    mantissa_int = to_int(mantissa_str)
    fim = time.time()
    print('Funcao to_float - Tempo de execução:', (fim-inicio))
    return pow(-1, bit_signal) * mantissa_int * pow(2, expoente_unbias)

def equals( A , B):
    return A == B

def lessThan(A, B):
    return A < B

def sum(A: float, B: float):
    inicio = time.time()
    if isinstance(A, float) and isinstance(B,float):
        fim  = time.time()
        print('Funcao sum - Tempo de execução: ' , (fim-inicio))
        return A + B
   
    return None


result_binary = to_ieee754(-5.5)
print(result_binary)

result_float= to_float(result_binary)
print(result_float)

result_equals = equals(result_float, -4.5)
print(result_equals)

result_lessThan = lessThan(result_float, 4.0)
print(result_lessThan)

result_sum = sum(result_float, 4.0)
print(result_sum)