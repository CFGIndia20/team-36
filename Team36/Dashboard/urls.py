from django.urls import path, include
from . import views


urlpatterns = [
    path('feedback/', views.reportGenerator, name='reportGenerator'),
    # path('sendreport/donor1/',views.sendreport),
    path('pdf/', views.pdf, name="pdf"),
    path('', views.index, name='index'),
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('centers/',views.centers,name="centers"),
    path('beneficiaries/',views.beneficiaries,name="beneficiaries"),
    path('donors/',views.donors,name="donors"),
    path('beneficiaries/child1',views.child1,name="child1"),
    path('beneficiaries/child2',views.child2,name="child2"),
    path('donors/donor1',views.donor1,name="donor1"),
    path('donors/donor2',views.donor2,name="donor2"),
    path('sms/', views.sendSms, name="sms"),

]