
from django import views
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

from my_first_project.my_first_app.models import Author,profile

# Create your views here.
def my_view(request):   # metodo my_view que recibe un request como parametro y retorna una respuesta
    carl_list = [
        {"title":"BMW"},
        {"title":"Mazda"}
    ]
    context = {
        "car_list": carl_list
    }
    return render(request, "my_first_app/car_list.html",context)   # render necesita un request y un template
                                        # para poder que django encuentre el archivo template se necesita registrarlo
                                        # en la app; en settigns.py INSTALLED APPS

class CarListView(views.TemplateView):                  # creacion de vista por medio de clase
    template_name = "my_first_project/my_first_app/car_list.html"

    def get_context_data(self):
        carl_list = [
            {"title":"BMW"},
            {"title":"Mazda"}
        ]
        return {
            "car_list": carl_list
    }

def my_test_view(request,*args,**kwargs):      # cuando se agregan datos dinamicamente, se agregan como parametros:
    print(args)                           # (*args,**kwargs),creamos una vista para hacer prueba
    print(kwargs)
    return HttpResponse("")     # ---> respuesta http  con control + . se puede importar automaticamente la clase a usar

def author_view(request, *args,**kwargs):
    print(args)
    print(kwargs)
    author = Author.objects.get(id=kwargs['id'])
    Profile = profile.objects.get(author_id=kwargs["id"])
    return HttpResponse(f"Autor: {author.name} - Sitio Web: {profile.website} - Biografia: {profile.biografia}")