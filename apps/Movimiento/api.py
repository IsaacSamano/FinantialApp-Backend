# Importaciones necesarias de Django Rest Framework y otros módulos
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, JSONParser
from apps.Movimiento.models import Movimiento
from apps.Movimiento.serializers import MovimientoSerializer, MovimientoSerializerListar
# Primera vista: Para listar y crear movimientos


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, JSONParser])
def movimiento_api_view(request):
    # Listar movimientos
    if request.method == 'GET':
        movimiento = Movimiento.objects.all()  # Obtener todos los movimientos
        movimiento_serializer = MovimientoSerializerListar(
            movimiento, many=True)  # Serializar los datos
        # Respuesta con los movimientos
        return Response(movimiento_serializer.data, status=status.HTTP_200_OK)
    # Crear un nuevo movimiento
    elif request.method == 'POST':
        movimiento_serializer = MovimientoSerializer(
            data=request.data)  # Serializar los datos recibidos
        if movimiento_serializer.is_valid():  # Validar los datos
            movimiento_serializer.save()  # Guardar el nuevo movimiento
            # Respuesta de éxito
            return Response({'message': 'movimiento creado correctamente!'}, status=status.HTTP_201_CREATED)
        # Manejo de errores
        return Response(movimiento_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Segunda vista: Para manejar un movimiento específico (listar, actualizar, eliminar)


@api_view(['GET', 'PUT', 'DELETE'])
@parser_classes([MultiPartParser, JSONParser])
def movimiento_detail_api_view(request, pk=None):
    # Encontrar el movimiento específico por su clave primaria (pk)
    movimiento = Movimiento.objects.filter(idMovimiento=pk).first()
    # Si se encuentra el movimiento
    if movimiento:
        # Obtener detalles del movimiento
        if request.method == 'GET':
            movimiento_serializer = MovimientoSerializer(
                movimiento)  # Serializar los datos del movimiento
            # Respuesta con los datos del movimiento
            return Response(movimiento_serializer.data, status=status.HTTP_200_OK)
        # Actualizar movimiento
        elif request.method == 'PUT':
            movimiento_serializer = MovimientoSerializer(
                movimiento, data=request.data)  # Serializar los datos
            if movimiento_serializer.is_valid():  # Validar los datos
                movimiento_serializer.save()  # Guardar los datos
                # Respuesta de éxito
                return Response({'message': 'movimiento actualizado correctamente!'}, status=status.HTTP_200_OK)
            # Manejo de errores
            return Response(movimiento_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Eliminar movimiento
        elif request.method == 'DELETE':
            try:
                movimiento.delete()  # Eliminar el movimiento
                # Respuesta de éxito
                return Response({'message': 'movimiento eliminado correctamente!'}, status=status.HTTP_200_OK)
            except Exception as e:
                # Manejo de errores
                return Response({'message': '¡No es posible eliminar un movimiento en uso!'}, status=status.HTTP_409_CONFLICT)
    # Si no se encuentra el movimiento
    # Manejo de errores
    return Response({'message': 'No se encontró el movimiento indicado'}, status=status.HTTP_400_BAD_REQUEST)
