# Dado um número n, o n-ésimo termo da sequência de Fibonacci é a soma dos dois termos anteriores (F(n) = F(n-1) + F(n-2)), 
#  * com F(0) = 0 e F(1) = 1

import unittest

def fibonacci(numero):
  if(numero <= 1):
    return numero
  else:
    return fibonacci(numero - 1) + fibonacci(numero - 2)  


numero = int(input("Digite um numero:"))
print("A soma fibonacci F(N) eh igual a", fibonacci(numero))


class FibonacciTest(unittest.TestCase):
  def testFibonacci(self):
    resultado = fibonacci(3)
    self.assertEqual(resultado, 2)

if __name__ == '__main__':
  unittest.main()
