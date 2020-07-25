from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('feedback/', views.reportGenerator, name='reportGenerator'),
    path('pdf/', views.pdf)
]