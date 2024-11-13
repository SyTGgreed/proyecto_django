from django.db import models

# Create your models here.

class Car(models.Model):   # hereda los modelos de .models
    title = models.TextField(max_length=250)   # campo title recibe un texto con maximo 250 caracteres
    year = models.TextField(max_length=4, null=True)      # campo para año que recibe solo 4 digitos ejm ( 2024)
    color = models.TextField(max_length=10, null=True)
    # cada que se añada un nuevo campo o tabla se tiene que hacer el makemigrations y luego migrate

    def __str__(self):             # esta clase muestra la representacion textual de lo que se quiere ver dentro de 
        return f"{self.title} - {self.year} - {self.color}"         # la terminal de un objeto especifico