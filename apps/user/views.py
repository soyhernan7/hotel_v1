# user/views.py
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework import pagination
from drf_yasg.utils import swagger_auto_schema

from apps.user.models import User
from apps.user.serializers import (
    UserSerializer, UserListSerializer, UpdateUserSerializer,
    PasswordSerializer, UserRegisterSerializer
)


class UserViewSet(GenericViewSet):
    """ UserViewSet para el manejo de usuarios """
    serializer_class = {
        'list': UserListSerializer,
        'create': UserSerializer,
        'retrieve': UserSerializer,
        'update': UpdateUserSerializer,
        'partial_update': UpdateUserSerializer,
        'set_password': PasswordSerializer,
        'register': UserRegisterSerializer,
    }
    queryset = User.objects.filter(is_active=True)
    pagination_class = pagination.PageNumberPagination

    def get_serializer_class(self):
        return self.serializer_class.get(self.action)

    def list(self, request):
        """ Retorna la lista de usuarios con paginacion """
        page = self.paginate_queryset(self.get_queryset())
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="Crea un nuevo usuario.")
    def create(self, request):
        """ Crea un nuevo usuario """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Usuario registrado correctamente.', 'user': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response({'message': 'Hay errores en el registro', 'errors': serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_description="Obtiene los detalles de un usuario específico.")
    def retrieve(self, request, pk=None):
        """ Retorna un usuario en especifico """
        user = get_object_or_404(User, pk=pk)
        serializer = self.get_serializer(user)
        return Response(serializer.data)


    def update(self, request, pk=None):
        """ Actualiza un usuario en especifico """
        user = get_object_or_404(User, pk=pk)
        serializer = self.get_serializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Usuario actualizado correctamente'})
        return Response({'message': 'Hay errores en la actualización', 'errors': serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
            Desactiva un usuario
        """
        user = get_object_or_404(User, pk=pk)
        user.is_active = False
        user.save()
        return Response({'message': 'Usuario eliminado correctamente'})


    def set_password(self, request, pk=None):
        """ Establece una nueva contraseña para un usuario """
        user = get_object_or_404(User, pk=pk)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'message': 'Contraseña actualizada correctamente'})
        return Response({'message': 'Hay errores en la información enviada', 'errors': serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='register', url_name='register')
    def register(self, request):
        """ Registra un nuevo usuario """
        return self.create(request)
