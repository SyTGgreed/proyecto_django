from django.db import models

# Create your models here.

class Car(models.Model):   # hereda los modelos de .models
    title = models.TextField(max_length=250)   # campo title recibe un texto con maximo 250 caracteres