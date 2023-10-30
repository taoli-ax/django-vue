from datetime import timezone

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.utils import timezone
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .car_form import CarInfoForm
from .models import CarInfo
from .serializers import CarInfoSerializer


# Create your views here.
def list_cars(request):
    cars = CarInfo.objects.all()
    print(cars)
    return render(request, 'cars.html', context={'carinfo_list': cars})


class CarViewSet(ListView):
    model = CarInfo
    template_name = 'cars.html'
    queryset = CarInfo.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    # 定制query set
    # def get_queryset(self):
    #     return CarInfo.objects.filter(name=self.request.user)


class CarViewSetForCreate(CreateView):
    template_name = 'cars.html'
    form_class = CarInfoForm
    model = CarInfo

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, 'cars.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cars/views')
        return render(request, 'cars.html', {'form': form})


class CarInfoViewSets(ModelViewSet):
    queryset = CarInfo.objects.all()
    serializer_class = CarInfoSerializer
    # permission_classes = [permissions.AllowAny]
