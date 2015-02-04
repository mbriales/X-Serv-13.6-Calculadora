#!/usr/bin/python
# -*- coding: utf-8 -*-
# Miguel Briales Romanillos

import sys                              # For get arguments

# Reads and checks arguments
try:
    Funcion     =   sys.argv[1]
    Operando_1  =   float(sys.argv[2])
    Operando_2  =   float(sys.argv[3])  # Switched to floats for operate

# Operates entered operands
    if Funcion      ==  'sumar':
        Result = Operando_1 + Operando_2
    elif Funcion    ==  'restar':
        Result = Operando_1 - Operando_2
    elif Funcion    ==  'multiplicar':
        Result =Operando_1 * Operando_2
    elif Funcion    ==  'dividir':
        Result = Operando_1 / Operando_2
# Prints the result
    print Result

# Exceptions
except IndexError:
    print 'calculadora.py <función> <operando 1> <operando 2>'
    sys.exit(2)   
except ValueError and ZeroDivisionError:
    print 'Operando/s inválidos'
    sys.exit(2)
except NameError:
    print 'Función inválida'
    sys.exit(2)