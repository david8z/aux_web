from productos.models import Producto, Imagen
from rest_framework import serializers
from django.db.models.query import QuerySet



class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    imagenes        = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='imagen-detail')
    id              = serializers.ReadOnlyField()
    visualizaciones = serializers.SerializerMethodField()

    def get_visualizaciones(self, producto):
        if not isinstance(self.instance, QuerySet): # Solamente se actiualizarán las visualizaciones cuando se acceda un producto en específico.
            producto.visualizaciones = producto.visualizaciones + 1
            producto.save()
        return producto.visualizaciones
    class Meta:
        model  = Producto
        fields = ['url', 'id', 'referencia','color_codigo', 'activo', 'imagenes', 'visualizaciones']
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
        }

class ImagenSerializer(serializers.HyperlinkedModelSerializer):
    id       = serializers.ReadOnlyField()
    producto = serializers.SlugRelatedField(
        queryset   = Producto.objects.all(),
        slug_field = 'slug'
     )
    class Meta:
        model  = Imagen
        fields = ['url', 'id', 'producto', 'imagen']
