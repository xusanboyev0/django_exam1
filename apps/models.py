from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, FloatField, ForeignKey, CASCADE, IntegerField, TextChoices, TextField


class User(AbstractUser):
    phone = CharField(max_length=50, null=True, blank=True)


class DistrictModel(Model):
    name = CharField(max_length=100)


class VacancyModel(Model):
    title = CharField(max_length=255)
    salary = FloatField(null=True, blank=True)
    company = CharField(max_length=50)
    description = TextField()
    district = ForeignKey('apps.DistrictModel', CASCADE)
    user = ForeignKey('apps.User', CASCADE)
    practice = IntegerField()

    class Time(TextChoices):
        FULL_TIME = 'full time', 'Full Time'
        PART_TIME = 'part time', 'Part Time'
        PROJECT_WORK = 'project work', 'Project Work'

    time = CharField(max_length=50, choices=Time.choices)
