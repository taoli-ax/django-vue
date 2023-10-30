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
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class AccountViewSet(viewsets.ViewSet):
    permission_classes=[permissions.AllowAny]

    @action(methods=['post'], detail=False)
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
           print("this line will not be excuted")
  
        user_id = serializer.validated_data['user_id']
        user = User.objects.get(pk=user_id)
        login(request, user)

        return Response({
            'success': True,
            'token':{
                'refresh': serializer.validated_data['refresh'],
                'access': serializer.validated_data['access'],
            },
            'user': user.username
          })


