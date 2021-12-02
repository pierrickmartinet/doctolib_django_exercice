from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from .forms import PatientRegister, AppointmentRegister
from .models import Doctor, Patient, Appointment


def get_patientInfo(request):
    if request.method == 'POST':
        form = PatientRegister(request.POST)
        if form.is_valid():
            patientDB = form.save()
            print(patientDB.id)
            return HttpResponseRedirect(f'{patientDB.id}/rdv')
    else:
        form = PatientRegister()
    return render(request, 'ResaDoctor/index.html', {'form': form})


def get_appointmentInfo(request, patient_id):
    if request.method == 'POST':
        form = AppointmentRegister(request.POST)
        if form.is_valid():
            appointment = Appointment(doctor=Doctor.objects.get(id=request.POST['doctor']),
                                      patient=Patient.objects.get(id=patient_id), date=request.POST['date'],
                                      timeslot=request.POST['timeslot'])
            appointment.save()
    else:
        form = AppointmentRegister()

    return render(request, 'ResaDoctor/rdv.html', {'form': form})
