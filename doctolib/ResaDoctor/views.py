from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Doctor


class IndexView(generic.ListView):
    template_name = 'ResaDoctor/index.html'
    context_object_name = 'doctor'


class RdvView(generic.ListView):
    template_name = 'ResaDoctor/rdv.html'
    context_object_name = 'doctor'

    def get_queryset(self):
        """Return the last five published questions."""
        return Doctor.objects.all()
