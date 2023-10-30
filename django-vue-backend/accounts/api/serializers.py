import re
from django.contrib.auth.models import User
from rest_framework import serializers, exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class LoginSerializer(TokenObtainPairSerializer):
    username = serializers.CharField()
    password = serializers.CharField()


    @classmethod
    def get_token(self, user):
        token = super().get_token(user)
        token['user'] = user.username
        print("加入 token 的 user 信息:",user)
        return token
        

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        # 令牌到期时间
        data['expire'] = refresh.access_token.payload['exp']  # 有效期
        # 用户名
        data['user_id'] = self.user.id
        return data
        # 原文链接：https://blog.csdn.net/u014783334/article/details/124841293

