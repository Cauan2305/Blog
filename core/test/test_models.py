from django.test import TestCase
from django.test.utils import tag
from model_mommy import mommy
from core.models import Publicação
from django.contrib.auth.models import User
# testando __str__

class TestePublicacao(TestCase):
    def setUp(self):
        # Publicação.objects.create(
        #     tag='esporte',
        #     usuario=None,
        #     titulo='Sao Paulo',
        #     texto='ola',
            

        # )
       cria=mommy.make(tag='esporte',titulo='Sao Paulo',texto='ola')
        


    def test_retorno_str(self):
        # p1=Publicação.objects.get(tag='esporte')

        self.assertEqual(p1.__str__(),'esporte')

