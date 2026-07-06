from django.test import TestCase
from services.forms import OrderForm

class OrderFormTest(TestCase):
    def test_title_label(self):
        orderForm = OrderForm()
        self.assertTrue(orderForm.fields['name'].label == 'Nombre')
    
    def test_inclomplete_fields(self):
        data = {
            'address':"4 Poniente 805",
            'total':1250.0
        }
        orderForm = OrderForm(data)
        self.assertFalse(orderForm.is_valid())