from django.db import models

# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='Titulo')
    image = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    description = models.TextField(null=True, verbose_name='Descripción')

    # Permite visualizar los cambios en el módulo administrativo.
    def __str__(self) -> str:
        fila = 'Titulo: ' + self.title + ' - ' + 'Descripción: ' + self.description
        return fila
    
    # Eliminación física del archivo desde el servidor.
    def delete(self, using=None, keep_parameters=False):
        self.image.storage.delete(self.image.name)
        super().delete()
