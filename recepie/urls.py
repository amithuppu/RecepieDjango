from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'index',views.index, name='index'),
    url(r'createRecepie', views.createRecepie.as_view(), name='createRecepie'),
    url(r'getRecepiesByUser',views.getRecepiesByUser.as_view(), name='getRecepiesByUser'),
    url(r'getallRecepies',views.getallRecepies.as_view(), name='getallRecepies'),
    url(r'deleteRecepie',views.deleteRecepie.as_view(), name='deleteRecepie'),
    url(r'updateRecepie',views.updateRecepie.as_view(), name='updateRecepie'),
]