# -*- coding: utf-8 -*-

#Import python libraries for testing
from selenium import webdriver
import unittest

#TestCase class
class NewVisitorTest(unittest.TestCase):

    """
    setUp is a method that initialize the test
    Open the browser and wait for 3 seconds just 
    in case of the page don't load.
    """
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    """
    tearDown method is executed after of each test 
    and close the browser 
    """
    def tearDown(self):
        self.browser.quit()

    """
    With this method test of that I want
    open the browser and the url 'http://localhost:8000'
    and in the assert we says if exist the title 'Welcome to Django' 
    """    
    def test_it_worked(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Django', self.browser.title)

"""
Solo si python ejecuta el archivo directamente (no importado)
se ejecutara la funcion unittest.main()
Esta funcion lanza el Test runner unittest que identifica las 
diferentes pruebas definidas mediante los metodos que comienzan
con la palabra test como en este caso de test_it_worked   

We call the unittest.main() function with the optional 
parameter warnings=’ignore’ to avoid a ResourceWarning message.

"""
if __name__ == '__main__':
    unittest.main(warnings='ignore')

"""
Los metodos setUp y tearDown se ejecutan al principio
y al final de cada metodo de prueba, de cada metodo que arranque
con la palabra clave test como en este caso de test_it_worked
"""
