from django.urls import include, path
from rest_framework import routers
from productos import views
from django.conf import settings
from django.conf.urls.static import static
from frontend.views import index_page

router = routers.DefaultRouter()
router.register(r'productos', views.ProductoViewSet)
router.register(r'imagenes', views.ImagenViewSet)


urlpatterns = [
    path('', index_page, name='index'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
