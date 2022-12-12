from django.shortcuts import render, redirect
from .models import Pizza, Topping
from .forms import CommentForm
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


def add_comment(request, pizza_id):
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            return redirect('pizza_details',pizza_id=pizza_id)
    return render(request, 'pizzas/add_comment.html', {'form': form})

def submit_comment(request, pizza_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # process the form data
            comment = form.cleaned_data['comment']
            # save the comment to the database
            # redirect to the pizza_details page
            return redirect('pizza_details', pizza_id=pizza_id)
    else:
        form = CommentForm()
    return render(request, 'pizzas/add_comment.html', {'form': form})
