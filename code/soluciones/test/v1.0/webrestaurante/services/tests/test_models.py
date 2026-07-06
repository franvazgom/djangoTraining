from django.test import TestCase
from services.models import Order, Service

class OrderModelTest(TestCase):
    def test_not_empty(self):
        order = Order(
            name = 'Francisco Vázquez',
            address = '4 Poniente 805',
            total = 1452.21,
            email = 'franvazgom@gmail.com'
        )
        order.save()
        orders = Order.objects.all()
        self.assertIs(len(orders) >0, True)
        self.assertEqual(orders[0].name, 'Francisco Vázquez')

class ServiceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        service = Service(
            title = 'Asado de res',
            sub_title = 'Los mejores cortes',
            content = 'Contenido asociado al asado de res',
            cost = 1250.0,
            image = 'ruta de imagen'
        )
        service.save()
    
    def test_title_name_label(self):
        service = Service.objects.get(id=1)
        field_label = service._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'Título')
    
    def test_title_max_length(self):
        service = Service.objects.get(id=1)
        max_length = service._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)
