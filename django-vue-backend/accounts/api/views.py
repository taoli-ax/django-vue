from accounts.api.serializers import LoginSerializer, UserSerializer
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)



class AccountViewSet(viewsets.ViewSet):
    serializer_class= LoginSerializer

    @action(methods=['post'], detail=False)
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            print("valid data")
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)

        if not user or user.is_anonymous:
            return Response({
                    "success": False,
                    "message": "username and password does not match",
                }, status=400)
        login(request, user)
        return Response({
            "success": True,
            "user": UserSerializer(instance=user).data,
        })

