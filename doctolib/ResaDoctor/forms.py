from django import forms

from .models import Patient, Appointment, Doctor


class PatientRegister(forms.ModelForm):
    first_name = forms.CharField(label='Entrez votre prénom', max_length=100)
    last_name = forms.CharField(label='Entrez votre nom', max_length=100)

    class Meta:
        model = Patient
        fields = ('first_name', 'last_name')


class DoctorRegister(forms.ModelForm):
    first_name = forms.CharField(label='Entrez votre prénom', max_length=100)
    last_name = forms.CharField(label='Entrez votre nom', max_length=100)

    class Meta:
        model = Doctor
        fields = ('first_name', 'last_name')


timeslots = [('08h00 à 09h00', '08h00 à 09h00'), ('09h00 à 10h00', '09h00 à 10h00'), ('10h00 à 11h00', '10h00 à 11h00'),
             ('11h00 à 12h00', '11h00 à 12h00'), ('14h00 à 15h00', '14h00 à 15h00'),
             ('15h00 à 16h00', '15h00 à 16h00'),
             ('16h00 à 17h00', '16h00 à 17h00')]


class AppointmentRegister(forms.Form):
    doctor = forms.ModelChoiceField(Doctor.objects.all(), label="Choisissez un médecin    ")
    date = forms.DateField(label="    Choisissez la date    ", widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    timeslot = forms.MultipleChoiceField(label="    Choisissez le créneau horaire    ", widget=forms.Select,
                                         choices=timeslots)
