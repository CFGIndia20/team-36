from django.urls import path, include
from . import views


urlpatterns = [
    path('feedback/', views.reportGenerator, name='reportGenerator'),
    path('pdf/', views.pdf),
    path('', views.index, name='index'),
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
]