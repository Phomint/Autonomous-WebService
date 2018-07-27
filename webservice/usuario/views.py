from django.shortcuts import render

from .models import Usuario
from .serializer import UsuarioSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
class UsuarioList(APIView):
    serializer_class = UsuarioSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Usuario.objects.all(), many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"403 Forbidden"}, status=status.HTTP_409_CONFLICT)

class UsuarioView(APIView):
    serializer_class = UsuarioSerializer

    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Usuario = self.get_object(pk)
        serializer = self.serializer_class(Usuario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Usuario = self.get_object(pk)
        serializer = self.serializer_class(Usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Usuario = self.get_object(pk)
        Usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
