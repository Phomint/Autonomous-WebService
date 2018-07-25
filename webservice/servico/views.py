from django.shortcuts import render

from .models import Servico
from .serializer import ServicoSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class ServicoList(APIView):
    serializer_class = ServicoSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Servico.objects.all(), many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"403 Forbidden"}, status=status.HTTP_409_CONFLICT)

class ServicoView(APIView):
    serializer_class = ServicoSerializer

    def get(self, request, pk, format=None):
        Servico = Servico.objects.get(pk=pk)
        serializer = self.serializer_class(Servico)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Servico = Servico.objects.get(pk=pk)
        serializer = self.serializer_class(Servico, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Servico = Servico.objects.get(pk=pk)
        Servico.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
