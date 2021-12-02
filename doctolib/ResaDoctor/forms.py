from django import forms

from .models import Patient, Appointment, Doctor


class PatientRegister(forms.ModelForm):
    first_name = forms.CharField(label='Entrez votre prénom', max_length=100)
    last_name = forms.CharField(label='Entrez votre nom', max_length=100)

    class Meta:
        model = Patient
        fields = ('first_name', 'last_name')


timeslots = [(1, '08h00-09h00'), (2, '09h00-10h00'), (3, '10h00-11h00'), (4, '11h00-12h00'), (5, '14h00-15h00'),
             (6, '15h00-16h00'),
             (7, '16h00-17h00')]


class AppointmentRegister(forms.Form):
    doctor = forms.ModelChoiceField(Doctor.objects.all())
    date = forms.DateField(label="Choisissez la date:", widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    timeslot = forms.MultipleChoiceField(label="Choisissez le créneau horaire:", widget=forms.Select, choices=timeslots)

    # class Meta:
    #     model = Appointment
    #     fields = ('doctor', 'timeslot', 'date')
