# Importaciones necesarias de Django
from django.urls import path
from apps.Tarjeta.api import tarjeta_api_view, tarjeta_detail_api_view, tarjeta_usuario_api_view
# Lista de patrones de URL
urlpatterns = [
    # URL para operaciones generales de usuarios (listar y crear)
    path('tarjetas/', tarjeta_api_view, name='tarjeta_api'),
    # URL para operaciones específicas de un usuario (obtener detalles, actualizar, eliminar)
    path('tarjetas/<int:pk>/', tarjeta_detail_api_view, name='tarjeta_detail_api'),
    path('tarjetas_usuario/<int:pk>/', tarjeta_usuario_api_view,
         name='tarjeta_usuario_detail_api')
]
