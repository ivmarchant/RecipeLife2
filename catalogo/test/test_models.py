from django.test import TestCase
from catalogo.models import Mangaka

class BookTestCase(TestCase):
    @classmethod
    def setUpData(cls):
        Mangaka.objects.create(primer_nombre='Manuel', apellido='Juan')
    def test_primer_nombre_label(self):
        mangaka=Mangaka.objects.get(id=1)
        field_label= mangaka._meta.get_field('primer_nombre').verbose_name
        self.assertEquals(field_label, 'primer_nombre')
    def test_fecha_muerte_label(self):
        mangaka=Mangaka.objects.get(id=1)
        field_label = mangaka._meta.get_field('fecha_muerte').verbose_name
        self.assertEquals(field_label,'died') 
    def test_primer_nombre_length(self):
        mangaka=Mangaka.objects.get(id=1)
        max_length= mangaka._meta.get_field('primer_nombre').max_length
        self.assertEquals(max_length,100)  
    def test_object_name_is_apellido_comma_primer_nombre(self):
        mangaka=Mangaka.objects.get(id=1)
        expected_object_name = '%s, %s' % (mangaka.apellido, mangaka.primer_nombre)
        self.assertEquals(expected_object_name,str(mangaka))
    def test_get_absolute_url(self):
        mangaka=Mangaka.objects.get(id=1)
        self.assertEquals(mangaka.get_absolute_url(),'/catalogo/mangaka/11')    

#PROFE LA QUEREMOS MUCHO ♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡♡