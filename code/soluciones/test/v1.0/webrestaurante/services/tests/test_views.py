from django.test import TestCase
from services.models import Service
from django.urls import reverse


class ServiceListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        n_services = 10
        for id in range(n_services):
            Service.objects.create(title='Servicio ' + str(id),
                                   sub_title='Subtitulo del servicio ' +
                                   str(id),
                                   content='Contenido del servicio ' + str(id),
                                   cost=100,
                                   image='ruta de imagen del servicio ' + str(id))

    def test_view_url_desired_location(self):
        resp = self.client.get('/services/')
        self.assertEqual(resp.status_code, 200)

    def test_correct_template(self):
        resp = self.client.get('/services/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'services/service_list.html')

    def test_services_list_len(self):
        resp = self.client.get('/services/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(resp.context['services']) == 10)
