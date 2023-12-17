# Importaciones necesarias de Django Rest Framework y otros módulos
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, JSONParser
from apps.Tarjeta.models import Tarjeta
from apps.Tarjeta.serializers import TarjetaSerializer, TarjetaSerializerListar
# Primera vista: Para listar y crear tarjetas


@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, JSONParser])
def tarjeta_api_view(request):
    # Listar tarjetas
    if request.method == 'GET':
        tarjeta = Tarjeta.objects.all()  # Obtener todos los tarjetas
        tarjeta_serializer = TarjetaSerializerListar(
            tarjeta, many=True)  # Serializar los datos
        # Respuesta con los tarjetas
        return Response(tarjeta_serializer.data, status=status.HTTP_200_OK)
    # Crear un nuevo tarjeta
    elif request.method == 'POST':
        tarjeta_serializer = TarjetaSerializer(
            data=request.data)  # Serializar los datos recibidos
        if tarjeta_serializer.is_valid():  # Validar los datos
            tarjeta_serializer.save()  # Guardar el nuevo tarjeta
            # Respuesta de éxito
            return Response({'message': 'tarjeta creado correctamente!'}, status=status.HTTP_201_CREATED)
        # Manejo de errores
        return Response(tarjeta_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Segunda vista: Para manejar un tarjeta específico (listar, actualizar, eliminar)


@api_view(['GET', 'PUT', 'DELETE'])
@parser_classes([MultiPartParser, JSONParser])
def tarjeta_detail_api_view(request, pk=None):
    # Encontrar el tarjeta específico por su clave primaria (pk)
    tarjeta = Tarjeta.objects.filter(idTarjeta=pk).first()
    # Si se encuentra el tarjeta
    if tarjeta:
        # Obtener detalles del tarjeta
        if request.method == 'GET':
            tarjeta_serializer = TarjetaSerializer(
                tarjeta)  # Serializar los datos del tarjeta
            # Respuesta con los datos del tarjeta
            return Response(tarjeta_serializer.data, status=status.HTTP_200_OK)
        # Actualizar tarjeta
        elif request.method == 'PUT':
            tarjeta_serializer = TarjetaSerializer(
                tarjeta, data=request.data)  # Serializar los datos
            if tarjeta_serializer.is_valid():  # Validar los datos
                tarjeta_serializer.save()  # Guardar los datos
                # Respuesta de éxito
                return Response({'message': 'tarjeta actualizado correctamente!'}, status=status.HTTP_200_OK)
            # Manejo de errores
            return Response(tarjeta_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Eliminar tarjeta
        elif request.method == 'DELETE':
            try:
                tarjeta.delete()  # Eliminar el tarjeta
                # Respuesta de éxito
                return Response({'message': 'tarjeta eliminado correctamente!'}, status=status.HTTP_200_OK)
            except Exception as e:
                # Manejo de errores
                return Response({'message': '¡No es posible eliminar un tarjeta en uso!'}, status=status.HTTP_409_CONFLICT)
    # Si no se encuentra el tarjeta
    # Manejo de errores
    return Response({'message': 'No se encontró el tarjeta indicado'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@parser_classes([MultiPartParser, JSONParser])
def tarjeta_usuario_api_view(request, pk=None):
    tarjetas = Tarjeta.objects.filter(propietario=pk)
    tjts_srlzr = TarjetaSerializer(tarjetas, many=True)
    return Response(tjts_srlzr.data, status=status.HTTP_200_OK)
