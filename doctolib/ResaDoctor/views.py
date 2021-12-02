from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from .forms import PatientRegister, AppointmentRegister, DoctorRegister
from .models import Doctor, Patient, Appointment


def get_patientInfo(request):
    if request.method == 'POST':
        form = PatientRegister(request.POST)
        if form.is_valid():
            patientDB = form.save()
            return HttpResponseRedirect(f'{patientDB.id}/rdv')
    else:
        form = PatientRegister()
    return render(request, 'ResaDoctor/index.html', {'form': form})


def get_doctorInfo(request):
    if request.method == 'POST':
        form = DoctorRegister(request.POST)
        loggedDoctor = Doctor.objects.get(last_name=request.POST['first_name'],
                                          first_name=request.POST['last_name'])
        doctorAppointments = Appointment.objects.filter(doctor=loggedDoctor.id)
        print(doctorAppointments)
        return render(request, 'ResaDoctor/doctorLogin.html',
                      {'form': form, 'loggedDoctor': loggedDoctor, 'doctorAppointments': doctorAppointments})
    else:
        form = DoctorRegister()
        return render(request, 'ResaDoctor/doctorLogin.html',
                      {'form': form})


def get_appointmentInfo(request, patient_id):
    if request.method == 'POST':
        form = AppointmentRegister(request.POST)
        appointmentAlreadyExists = Appointment.objects.filter(timeslot=request.POST['timeslot'],
                                                              doctor=Doctor.objects.get(id=request.POST['doctor']),
                                                              date=request.POST['date'])
        if appointmentAlreadyExists.exists():
            response = "Desolé cette date et créneau sont déà pris pour ce médecin, veuillez choisir une autre " \
                       "date/créneau/médecin "
            return render(request, 'ResaDoctor/rdvindisponible.html', {'response': response})
        else:
            appointment = Appointment(doctor=Doctor.objects.get(id=request.POST['doctor']),
                                      patient=Patient.objects.get(id=patient_id), date=request.POST['date'],
                                      timeslot=request.POST['timeslot'])
            appointment.save()

    else:
        form = AppointmentRegister()

    return render(request, 'ResaDoctor/rdv.html', {'form': form})


def rdvIndispo(request):
    return render(request, 'ResaDoctor/rdvindisponible.html')
