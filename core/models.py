from django.db import models
from django.db.models.fields import CharField, DecimalField, TextField
from stdimage.models import StdImageField
import uuid

def get_file_path(__instance,filename):
    ext=filename.split('.')[-1]
    filename=f'{uuid.uuid4()}.{ext}'
    return filename

class Classes(models.Model):
    titulo=CharField('titulo',max_length=200)
    treinador=CharField('Nome do Treinador',max_length=500)
    especialidade=TextField('qual exercicio',max_length=600)
    preco=DecimalField(decimal_places=2,max_digits=10000)
    foto=StdImageField('imagem',upload_to=get_file_path,variations={'thumb':{'width' : 350,'height':233.333 ,'crop':True}})
    # instagram=models.URLField('Instagram',)
    # facebook=models.URLField('Facebook',)




    class Meta:
        verbose_name='Classes'

    def __str__(self):
        return self.titulo