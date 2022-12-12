from django.shortcuts import render
from .models import Pizza, Topping
# Create your views here.

def home(request):
    return render(request, 'pizzas/home.html')

def pizza_menu(request):
    pizzas = Pizza.objects.all()
    context = {'pizzas':pizzas,}
    return render(request, 'pizzas/pizza_menu.html', context)
    #print(response)
    #return response
    



def pizza_details(request, pizza_id):
    # get the Pizza object
    pizza = Pizza.objects.get(id=pizza_id)

    # get the queryset of Topping objects
    toppings = Topping.objects.filter(pizza=pizza)

    # convert the queryset of Topping objects to a list of strings
    topping_names = [topping.__str__() for topping in toppings]

    pizza.picture = 'some/file/path/here'

    context = {
        'pizza': pizza,
        'toppings': topping_names,
        'picture': pizza.picture,
    }
    return render(request, 'pizzas/pizza_details.html',context)
