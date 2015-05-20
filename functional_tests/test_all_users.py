# -*- coding: utf-8 -*-

#Import python libraries for testing


from selenium import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import unittest

"""
we can test these two different things:
- The title in the home page is “TaskBuster”
- The text color of the h1 header in the home page is 
rgba(200, 50, 255, 1) ~ pink color
"""
class HomeNewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    """
    funcion auxiliar llamada get_full_url que 
    toma un argumento namespace el cual es un identificado
    para el url.
    En Django cuando trabajamos con identificadores puedo 
    cambiar el url si deseo que el codigo funcione
    como antes

    self.live_server_url me da el url de localhost
    Usamos este metodo porque el server de pruebas 
    usa otro url (usualmente http://127.0.0.1:8021)
    y este metodo es mas flexible
    reverse me da un url relativo de un namespace dado, 
    aqui /

    El resultado de la funcion get_full_url me da el 
    url absoluto de ese namespace (la suma de los dos
    anteriores) http://127.0.0.1:8021
    """
    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    
    """
    Prueba que la pagina de home tenga en el titulo
    la palabra TaskBuster. Crearemos un template para esto
    asi que si el titulo existe significa que el template
    ha sido cargado correctamente
    """
    def test_home_title(self):
        self.browser.get(self.get_full_url("home"))
        self.assertIn("TaskBuster", self.browser.title)

    """
    Prueba que el text h1 sea del color deseado
    La regla css para el color del texto sera un archivo
    css lo que significa que si la prueba pasa, entonces los
    archivos estaticos estan cargando correctamente
    """
    def test_h1_css(self):
        self.browser.get(self.get_full_url("home"))
        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(h1.value_of_css_property("color"),
                         "rgba(200, 50, 255, 1)")



"""
#TestCase class
class NewVisitorTest(unittest.TestCase):

    
    #setUp is a method that initialize the test
    #Open the browser and wait for 3 seconds just 
    #in case of the page don't load.
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    
    #tearDown method is executed after of each test 
    #and close the browser 
    
    def tearDown(self):
        self.browser.quit()

    
    #With this method test of that I want
    #open the browser and the url 'http://localhost:8000'
    #and in the assert we says if exist the title 'Welcome to Django' 
       
    def test_it_worked(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Django', self.browser.title)


#Solo si python ejecuta el archivo directamente (no importado)
#se ejecutara la funcion unittest.main()
#Esta funcion lanza el Test runner unittest que identifica las 
#diferentes pruebas definidas mediante los metodos que comienzan
#con la palabra test como en este caso de test_it_worked   

#We call the unittest.main() function with the optional 
#parameter warnings=’ignore’ to avoid a ResourceWarning message.


#if __name__ == '__main__':
#    unittest.main(warnings='ignore')

#Los metodos setUp y tearDown se ejecutan al principio
#y al final de cada metodo de prueba, de cada metodo que arranque
#con la palabra clave test como en este caso de test_it_worked

"""