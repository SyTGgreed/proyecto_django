from django.db import models

# Create your models here.

class Car(models.Model):   # hereda los modelos de .models
    title = models.TextField(max_length=250)   # campo title recibe un texto con maximo 250 caracteres
    year = models.TextField(max_length=4, null=True)      # campo para año que recibe solo 4 digitos ejm ( 2024)
    color = models.TextField(max_length=10, null=True)
    # cada que se añada un nuevo campo o tabla se tiene que hacer el makemigrations y luego migrate

    def __str__(self):             # esta clase muestra la representacion textual de lo que se quiere ver dentro de 
        return f"{self.title} - {self.year} - {self.color}"         # la terminal de un objeto especifico
    
class Publisher(models.Model):    # para observar las relaciones de tablas con django creamos como ejemplo dos clases
    name = models.TextField(max_length=200)   # una para los editores y una tabla para los libros
    address = models.TextField(max_length=30)

    def __str__(self) -> str:      # para poder ver en consola
        return self.name
    
class Book(models.Model):                      # clase libros
    title = models.TextField(max_length=200)   # titulo del libro 
    publications_date = models.DateField()     # fecha de publicacion del libro
    Publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)   # se establece la relacion de las tablas, en los parametros se establece la
                                               # la clase a relacionar en este caso con publisher
        # on_delete se utiliza para tomar una decision en caso de que se borre un publisher(editor)
        # DO_NOTHING  no hace nada, PROTECT no se puede borrar porque aun hay datos con ese publisher
        # CASCADE si se borra un publisher tambien borra todos los libros relacionados con este
    
    def __str__(self) -> str:
        return self.title             # mostramos el titulo en consola