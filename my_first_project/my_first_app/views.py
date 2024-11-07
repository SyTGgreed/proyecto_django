from django.shortcuts import render

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