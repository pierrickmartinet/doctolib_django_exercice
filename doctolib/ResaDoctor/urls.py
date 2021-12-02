from django.urls import path

from . import views

app_name = "resadoctor"
urlpatterns = [
    path('', views.get_patientInfo, name='index'),
    path('<int:patient_id>/rdv', views.get_appointmentInfo, name='rdv'),
    path('rdvindisponible', views.rdvIndispo, name='rdvindisponible'),
    path('doctorLogin', views.get_doctorInfo, name='doctorLogin')
]
