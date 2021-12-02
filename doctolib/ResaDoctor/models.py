from datetime import datetime, timezone

from django.db import models


class Doctor(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.speciality}'


class Patient(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField('date')
    timeslot = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.doctor} a un rendez-vous avec {self.patient} le {self.date} de {self.timeslot}'
