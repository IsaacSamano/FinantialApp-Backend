# Importaciones necesarias de Django
from django.urls import path
from apps.Movimiento.api import movimiento_api_view, movimiento_detail_api_view
# Lista de patrones de URL
urlpatterns = [
    # URL para operaciones generales de usuarios (listar y crear)
    path('movimientos/', movimiento_api_view, name='movimiento_api'),
    # URL para operaciones específicas de un usuario (obtener detalles, actualizar, eliminar)
    path('movimientos/<int:pk>/', movimiento_detail_api_view,
         name='movimiento_detail_api')
]
