from .models import Producto, Imagen
from rest_framework import viewsets
from .serializers import ProductoSerializer, ImagenSerializer
from rest_framework import filters
import time

class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite editar y buscar los productos activos, (aparecen en orden de mayor a menor visualizaciones.
    """
    queryset         = Producto.objects.prefetch_related('imagenes').filter(activo=True).order_by('-visualizaciones')
    serializer_class = ProductoSerializer
    lookup_field     = 'slug'
    filter_backends  = [filters.OrderingFilter]
    ordering_fields  = ['referencia']

    # def dispatch(self, *args, **kwargs):
    #     response = super().dispatch(*args, **kwargs)
    #     # For debugging purposes only.
    #     from django.db import connection
    #     # Una query para todos los productos y otra para las imagenes
    #     # asociadas al producto.
    #     print(connection.queries)
    #     print('# of Queries: {}'.format(len(connection.queries)))
    #     return response

class ImagenViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite buscar y editar imagenes.
    """
    # Con select_related crea una query para todas las imagenes con sus
    # productos asociados.
    queryset         = Imagen.objects.select_related('producto')
    serializer_class = ImagenSerializer
    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        # For debugging purposes only.
        from django.db import connection
        print(connection.queries)
        print('# of Queries: {}'.format(len(connection.queries)))
        return response
