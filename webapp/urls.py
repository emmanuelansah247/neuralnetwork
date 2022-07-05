
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home),
    path('trainappvalue/', views.trainappvalue, name="trainappvalue"),
    path('testnetwork/', views.testnetwork, name="testnetwork")
]
