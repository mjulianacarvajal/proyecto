from django.db import models
from administracion.models import Usuario
from django.core.validators import MinValueValidator


# Create your models here.


class EntregaCliente (models.Model):
    e_hora_C = models.TimeField(auto_now=True)
    e_fecha_C = models.DateField(auto_now=True)
    eC_total = models.PositiveIntegerField(validators=[MinValueValidator(1)],verbose_name='Cantidad Individual')

    eC_usuario_fk = models.ForeignKey(Usuario,on_delete= models.CASCADE)

    def __str__(self):
        return str(self.eC_total)



class EntregaExterna(models.Model):
    e_hora = models.TimeField(auto_now=True)
    e_fecha = models.DateField(auto_now=True)
    eE_total = models.PositiveBigIntegerField(validators=[MinValueValidator(1)],verbose_name='Cantidad Total')
    
    eE_usuario_fk = models.ForeignKey(Usuario,on_delete= models.CASCADE)

    def __str__(self):
        return str(self.eE_total)
