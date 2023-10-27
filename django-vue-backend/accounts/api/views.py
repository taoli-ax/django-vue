from accounts.api.authentication import JsonAuthentication
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
    # authentication_classes= [JsonAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]



class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = LoginSerializer
    @action(methods=['post'], detail=False)
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                "success": False,
                "message": "Please check input",
                "errors": serializer.errors,
            }, status=400)
        
        token = serializer.context.get('token')
        name = serializer.context.get('username')
        id = serializer.context.get('id')
        
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
            'token':token,
            'id':id,
            'username':username})
        # return Response({
        #     "success": True,
        #     "user": UserSerializer(instance=user).data,
        # })

