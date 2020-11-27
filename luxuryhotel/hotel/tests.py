from django.test import TestCase
import unittest
from . models import Cliente, Pais, Habitacion, TipoHab

#UNIT TEST

class ClienteTestCase(TestCase):
    
    def setUp(self):
        p1=Pais.objects.create(id_pais="1", nombre_pais="Chile")
        Cliente.objects.create(rut="19954485-1",
                               nombres="Daniel Esteban",
                               apellidos="Muñoz Gonzalez",
                               pais=p1,
                               edad=22,
                               email="daniel@gmail.com",
                               direccion="Mi casa j",
                               password="11992288hc")
    
    def test_Cliente(self):
        c1=Cliente.objects.get(rut="19954485-1")
        self.assertEqual(c1.pais.nombre_pais, "Chile")
        
class HabitacionTestCase(TestCase):
    
    def setUp(self):
        th=TipoHab.objects.create(id_tipo=1, nombre_habitacion="Luxury Room", beneficios="None")
        Habitacion.objects.create(id_habitacion=1,
                                  id_tipo=th,
                                  caracteristicas="h",
                                  descripcion="o",
                                  servicios="l",
                                  equipamiento="aj",
                                  image_1='/static/image/luxury/1.jpg',
                                  image_2='/static/image/luxury/3.jpg')

    def test_Habitacion(self):
        h1=Habitacion.objects.get(id_habitacion=1)
        self.assertEqual(h1.id_tipo.nombre_habitacion, "Luxury Room")

#FORM TEST

from . forms import ClienteForm, HabitacionForm
from django.core.files.uploadedfile import SimpleUploadedFile

class ClienteFormsTest(TestCase):
    
    def test_valid_form(self):
        p = Pais.objects.create(id_pais=10,nombre_pais='Alemania')
        c = Cliente.objects.create(rut="1313132-1",
                               nombres="Daniel Esteban",
                               apellidos="Muñoz Gonzalez",
                               pais=p,
                               edad=22,
                               email="daniel@gmail.com",
                               direccion="Mi casa j",
                               password="11992288hc")
        c.save()
        data = {'rut': c.rut, 'nombres': c.nombres, 'apellidos': c.apellidos, 'pais': c.pais, 
                'edad': c.edad, 'email': c.email, 'direccion': c.direccion, 'password': c.password,}
        form = ClienteForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_form(self):
        p = Pais.objects.create(id_pais=1, nombre_pais='Chile')
        c = Cliente.objects.create(rut="19954485-1",
                               nombres="",
                               apellidos="Muñoz Gonzalez",
                               pais=p,
                               edad=22,
                               email="daniel@gmail.com",
                               direccion="Mi casa j",
                               password="")
        c.save()
        data = {'rut': c.rut, 'nombres': c.nombres, 'apellidos': c.apellidos, 'pais': c.pais, 
                'edad': c.edad, 'emain': c.email, 'direccion': c.direccion, 'password': c.password,}
        form = ClienteForm(data=data)
        self.assertFalse(form.is_valid())
    
class HabitacionFormsTest(TestCase):
    
    def test_valid_form(self):
        th = TipoHab.objects.create(id_tipo=1,nombre_habitacion='Luxury Room', beneficios='none')
        h = Habitacion.objects.create(id_habitacion="1",
                               id_tipo=th,
                               caracteristicas="h",
                               descripcion="o",
                               servicios="l",
                               equipamiento="aj",
                               image_1='/static/image/luxury/1.jpg',
                               image_2='/static/image/luxury/3.jpg')
        h.save()
        data = {'id_habitacion': h.id_habitacion, 'id_tipo': h.id_tipo, 'caracteristicas': h.caracteristicas, 'descripcion': h.descripcion, 
                'servicios': h.servicios, 'equipamiento': h.equipamiento, 'image_1': h.image_1, 'image_2': h.image_2,}
        form = HabitacionForm(data=data)
        self.assertFalse(form.is_valid())
        
    def test_invalid_form(self):
        th = TipoHab.objects.create(id_tipo=1,nombre_habitacion='Luxury Room', beneficios='none')
        h = Habitacion.objects.create(id_habitacion="1",
                               id_tipo=th,
                               caracteristicas="",
                               descripcion="",
                               servicios="l",
                               equipamiento="aj",
                               image_1='/static/image/luxury/1.jpg',
                               image_2='/static/image/luxury/3.jpg')
        h.save()
        data = {'id_habitacion': h.id_habitacion, 'id_tipo': h.id_tipo, 'caracteristicas': h.caracteristicas, 'descripcion': h.descripcion, 
                'servicios': h.servicios, 'equipamiento': h.equipamiento, 'image_1': h.image_1, 'image_2': h.image_2,}
        form = HabitacionForm(data=data)
        self.assertFalse(form.is_valid())
        
# TEST VIEWS

from django.urls import reverse

class ClienteListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crear 13 clientes para pruebas de paginación
        
        number_of_cliente = 13
        p = Pais.objects.create(id_pais=1,nombre_pais='Chile')
        
        for cliente_rut in range(number_of_cliente):
            Cliente.objects.create(
                rut=f'1995484232 {cliente_rut}',
                nombres=f'Prueba des {cliente_rut}',
                apellidos=f'Prueba desj {cliente_rut}',
                pais=p,
                edad=22,
                email=f'Prueba@gmail.com {cliente_rut}',
                direccion=f'Prueba {cliente_rut}',
                password=f'Pruebasjeje1 {cliente_rut}',
            )
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/hotel/clientes/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('clientes'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('clientes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'CRUD/cliente_list.html')
        
    def test_pagination_is_ten(self):
        response = self.client.get(reverse('clientes'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['cliente_list']) == 10)

class HabitacionListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crear 13 habitaciones para pruebas de paginación
        number_of_habitacion = 1
        th = TipoHab.objects.create(id_tipo=1, nombre_habitacion='Luxury Room', beneficios='none')
        
        with open('hotel/static/img/prese.jpg', 'rb') as file:
            document = SimpleUploadedFile(file.name, file.read(), content_type='image/jpg')

        for habitacion_id_habitacion in range(number_of_habitacion):
            Habitacion.objects.create(
                id_habitacion=1,
                id_tipo=th,
                caracteristicas=f'ho {habitacion_id_habitacion}',
                descripcion=f'laj {habitacion_id_habitacion}',
                servicios=f'como {habitacion_id_habitacion}',
                equipamiento=f'tas {habitacion_id_habitacion}',
                image_1=document,
                image_2=document,
            )
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/hotel/habitacion-adm/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('habitacion-adm'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('habitacion-adm'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_generic.html', 'CRUD/habitacion-list.html')
