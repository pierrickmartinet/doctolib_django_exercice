from django.urls import path

from . import views

app_name = "resadoctor"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('rdv', views.RdvView.as_view(), name='rdv'),
]
