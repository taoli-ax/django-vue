import re
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from cars.models import CarInfo



class CarInfoSerializer(serializers.HyperlinkedModelSerializer):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    class Meta:
        model = CarInfo
        fields = ['name']
    

    def validate(self, attrs):
        # username mobile 都可能是登录账户
        car_name = attrs.get('name')
        print("验证attr: ",attrs)
        if isinstance(car_name, str):  # 手机号正则
           
            payload = self.jwt_payload_handler()  # 通过user拿到payload
        #     token = self.jwt_encode_handler(payload)  # 通过payload拿到token
        #     print('生成token：' + token)
        #     # 视图类和序列化类之间通过context这个字典来传递数据
        #     self.context['token'] = token
        #     self.context['username'] = user.username
        #     self.context['id'] = user.id
        #     return attrs
        # else:
        #     raise ValidationError("账户或密码错误")
        return attrs

# 原文链接：https://blog.csdn.net/Karse_/article/details/129910708
