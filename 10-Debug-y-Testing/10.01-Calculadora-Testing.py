import unittest
from Calculadora import *

class CalculadoraTesting(unittest.TestCase):
    #Método de preparación, se ejecutan antes de las pruebas y siempre se llama setUp()
    def setUp(self):
        self.calculadora = Calculadora()
        self.calculadora.Numero1 = 5
        self.calculadora.Numero2 = 10

    #Método que contiene una prueba, obligatoriamente comienza por test_
    def test_suma(self):
        self.assertEqual(self.calculadora.Suma(), 15)

    #Método que contiene una prueba, obligatoriamente comienza por test_
    def test_resta(self):
        self.assertEqual(self.calculadora.Resta(), -5)

    #Método de finalización, se ejecutan después de las pruebas y siempre se llama tearDown()
    def tearDown(): pass

# Permite inicial la Prueba Unitaria ejecutando el fichero como script
# También podemos iniciar las pruebas con el comando py -m unittest 10.01-Calculadora-Testing
# Otra opción es ejecutar solo una función mediante el comando py -m unittest 10.01-Calculadora-Testing.test_suma

if __name__ == '__main__':
    unittest.main()