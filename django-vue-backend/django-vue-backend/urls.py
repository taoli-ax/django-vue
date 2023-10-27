"""django-vue-backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from accounts.api.views import UserViewSet, AccountViewSet
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cars.views import CarInfoViewSets

router = routers.SimpleRouter()
router.register(r'api/carinfo',CarInfoViewSets)
router.register(r'api/users',UserViewSet)
router.register(r'api/accounts',AccountViewSet, basename='accounts')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('cars/', include('cars.urls'))
    path('', include(router.urls))

]
