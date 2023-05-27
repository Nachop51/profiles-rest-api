from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloApiView(APIView):
    """ Test API View """
    serializer_class = serializers.HelloSerializer

    def get(self, req, format=None):
        """ Returns a list of APIView features """
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, req):
        """ Create a hello message with our name """
        serializer = self.serializer_class(data=req.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'

            return Response({'message': message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, req, pk=None): # pk -> object to be updated
        """ Handle updating an object """
        return Response({'method': 'PUT'})

    def patch(self, req, pk=None):
        """ Handle a partial update of an object """
        return Response({'method': 'PATCH'})

    def delete(self, req, pk=None):
        """ Delete an object """
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet """

    serializer_class = serializers.HelloSerializer

    def list(self, req):
        """ Return a hello message """
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, req):
        """ Create a new hello message """
        serializer = self.serializer_class(data=req.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'

            return Response({'message': message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, req, pk=None):
        """ Handle getting an object by its ID """
        return Response({'http_method': f'GET {str(pk)}'})

    def update(self, req, pk=None):
        """ Handle updating an object """
        return Response({'http_method': 'PUT'})

    def partial_update(self, req, pk=None):
        """ Handle updating part of an object """
        return Response({'http_method': 'PATCH'})

    def destroy(self, req, pk=None):
        """ Handle removing an object """
        return Response({'http_method': 'DELETE'})

