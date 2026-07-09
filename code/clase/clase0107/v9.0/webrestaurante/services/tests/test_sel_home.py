from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from services.models import Service as Servicio


class TestServices(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        PATH_WEB_DRIVER = r'C:\Users\Francisco\Downloads\chromedriver-win64\chromedriver.exe'
        cls.service = Service(PATH_WEB_DRIVER)
        cls.selenium = webdriver.Chrome(service=cls.service)
        cls.selenium.set_window_size(1200, 1000)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_home_title(self):
        browser = self.selenium
        url = self.live_server_url
        browser.get(url + '/')
        self.assertIn('La Recova', browser.title)

    def test_cart(self):
        # Se crean 10 servicios
        n_services = 10
        for id in range(n_services):
            Servicio.objects.create(title='Servicio ' + str(id),
                                    sub_title='Subtitulo del servicio ' +
                                    str(id),
                                    content='Contenido del servicio ' +
                                    str(id),
                                    cost=100,
                                    image='ruta de imagen del servicio ' + str(id))
        # Se accede al link de servicios
        browser = self.selenium
        url = self.live_server_url
        browser.get(url + '/services/')
        time.sleep(1)
        # Se agrega al carrito el primer elemento
        btn_add_cart = browser.find_element(By.LINK_TEXT, 'Agrega al carrito')
        btn_add_cart.click()
        time.sleep(1)
        browser.get(url + '/services/')
        # Click en el carrito de compras
        btn_badge = browser.find_element(By.ID, 'cart-badge')
        btn_badge.click()
        time.sleep(1)
        # Se verifica que el total sea 100 pesos
        body = browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('Total = $ 100', body.text)
        time.sleep(1)
        # Se realiza la compra
        btn_compra = browser.find_element(By.LINK_TEXT, 'Confirmar pedido')
        btn_compra.click()
        time.sleep(1)
        # Llena el formulario
        caja = browser.find_element(By.XPATH, '//*[@id="id_name"]')
        caja.send_keys("Pepito Rodriguez")
        time.sleep(1)
        caja = browser.find_element(By.XPATH, '//*[@id="id_address"]')
        caja.send_keys("4 Poniente 9876, México")
        time.sleep(1)
        caja = browser.find_element(By.XPATH, '//*[@id="id_email"]')
        caja.send_keys("pepito@gmail.com")
        time.sleep(1)
        form = browser.find_element(By.ID, 'formOrder')
        form.submit()
        # Verifica que termina de manera correcta
        body = browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('Gracias por su compra', body.text)
        time.sleep(1)
