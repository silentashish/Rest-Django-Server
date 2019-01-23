from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . import serializers
from . import models
from . import permissions


class HelloApiView(APIView):
    """Test API View."""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as function (get, post ,patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the tmost control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request):
        """Handles updating an object."""

        return Response({'method': 'put'})

    def patch(self, request):
        """Patch request, only updates fields provied in the request."""

        return Response({'method': 'patch'})

    def delete(self, request):
        """Deletes an object."""

        return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code.'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handles getting an object by its id."""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object."""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object."""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token."""

        return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfilesFeedItemSerializer
    queryset = models.ProfilesFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        serializer.save(user_profile=self.request.user)

class ImageFieldViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ImageFieldSerializer
    queryset = models.ImageUploadField.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        serializer.save(user_profile=self.request.user)

class ImageViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    serializer_class = serializers.ImageSerializer
    queryset = models.ImageField.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class CommentFieldViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.CommentFieldSerializer
    queryset = models.CommentField.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        serializer.save(user_profile=self.request.user)

class TokenViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items."""

    serializer_class = serializers.TokenSerializer
    queryset = models.TokenFiled.objects.all()

    def perform_create(self, serializer):
        from fcm_django.models import FCMDevice

        devices = FCMDevice.objects.all().first()

        devices.send_message(title="Title", body="Message")
        devices.send_message(title="Title", body="Message", data={"test": "test"})
        devices.send_message(data={"test": "test"})
        serializer.save()
