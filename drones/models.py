# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Model(models.TextChoices):
    CHOICE1 = 'Lightweight', 'Lightweight'
    CHOICE2 = 'Middleweight', 'Middleweight'
    CHOICE3 = 'Cruiserweight', 'Cruiserweight'
    CHOICE4 = 'Heavyweight', 'Heavyweight'


class STATES(models.TextChoices):
    STATE1 = 'IDLE', 'IDLE'
    STATE2 = 'Loading', 'Loading'
    STATE3 = 'Loaded', 'Loaded'
    STATE4 = 'Delivering', 'Delivering'
    STATE5 = 'Delivered', 'Delivered'
    STATE6 = 'Returning', 'Returning'


from django.core.validators import RegexValidator


# Create your models here.
class Drones(models.Model):
    serial_number = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    model = models.CharField(
        choices=Model.choices
    )
    weight_limit = models.PositiveIntegerField(validators=[
        MaxValueValidator(500),
        MinValueValidator(1)
    ])
    battery = models.FloatField(validators=[
        MaxValueValidator(100),
        MinValueValidator(0)
    ])
    state = models.CharField(
        choices=STATES.choices
    )


class Medication(models.Model):
    name_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9-_]+$',
        message='This field only contains letters numbers and - _',
    )

    code_validator = RegexValidator(
        regex=r'^[A-Z0-9_]+$',
        message='Allowed only upper case letters, underscore and numbers',
    )

    name = models.CharField(validators=[name_validator])
    weight = models.PositiveIntegerField(validators=[
        MinValueValidator(1)
    ])
    code = models.CharField(validators=[code_validator])
    image = models.ImageField(upload_to='medications/')
