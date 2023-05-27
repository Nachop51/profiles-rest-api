from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
