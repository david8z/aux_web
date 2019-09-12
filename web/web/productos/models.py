from django.db import models
from django.db.models.signals import pre_save


class Producto(models.Model):
    referencia      = models.PositiveIntegerField()
    color_codigo    = models.PositiveSmallIntegerField()
    activo          = models.BooleanField(default=False)
    slug            = models.SlugField(unique=True,max_length=6, blank=True)
    # stock           = models.PositiveSmallIntegerField(default=0)
    visualizaciones = models.IntegerField(default=0)
    # descripcion     = models.TextField(max_length=500, blank=True, null=True)
    # categoria       =
    # pvp             = models.FloatField()
    # pr              = models.FloatField(blank=True, null=True)
    # tags (related words for search)
    class Meta:
        unique_together = ('referencia', 'color_codigo')

    def __str__(self):
        return "{:05d}".format(self.referencia) + str(self.color_codigo)
    # def get_absolute_url(self):
    def get_colores(self):
        """
        Devuelve todos los modelos con la misma referencia y distinto color.
        """
        return Producto.objects.filter(referencia = self.referencia, activo=True).exclude(color_codigo = self.color_codigo)


class Imagen(models.Model):
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, related_name='imagenes')
    imagen   = models.ImageField(upload_to="imagen")


def producto_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = "{:05d}".format(instance.referencia) + str(instance.color_codigo)

pre_save.connect(producto_pre_save_receiver, sender=Producto)
