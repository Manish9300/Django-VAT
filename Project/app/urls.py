from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('signup',views.signup),
    path('ins',views.ins),
    path('dashboard',views.dashboard),
    path('show',views.show),
    path('del/<int:id>',views.dele),
    path('edit/<int:id>',views.edit),
    path('edcode/<int:id>',views.edcode),
    path('class_A',views.class_A),
    path('choose_class',views.choose_class),
    path('status', views.status),
    path('login',views.login),
    path('log',views.log),
    path('logout',views.logout),
]