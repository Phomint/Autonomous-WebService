from django.shortcuts import render

from .models import Autonomo
from .serializer import AutonomoSerializer

from rest_framework.views import APIView
from rest_framework.response import Response


class AutonomoList(APIView):
    serializer_class = AutonomoSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Autonomo.objects.all(), many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"403 Forbidden"}, status=status.HTTP_409_CONFLICT)

class AutonomoView(APIView):

    def get(self, request, pk, format=None):
        id = Autonomo.objects.get(pk=pk)
        serializer = AutonomoSerializer(id)
        return Response(serializer.data)
