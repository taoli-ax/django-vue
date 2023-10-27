import re
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from rest_framework import serializers, exceptions

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ('username','password')

    def validate(self, attrs):
         # username mobile 都可能是登录账户
        username = attrs.get('username')
        password = attrs.get('password')

        user = User.objects.filter(username=username).first() # 用户名登录
        if user and user.check_password(password):  # 如果登录成功,生成token
            payload = jwt_payload_handler(user)  # 通过user拿到payload
            token = jwt_encode_handler(payload)  # 通过payload拿到token
            print('生成token：' + token)
            # 视图类和序列化类之间通过context这个字典来传递数据
            self.context['token'] = token
            self.context['username'] = user.username
            self.context['id'] = user.id
            return attrs
        else:
            raise exceptions.ValidationError("账户或密码错误")

