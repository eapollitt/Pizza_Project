import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzas.settings")

import django 
django.setup()

from pizzas.models import Pizza, Topping


Pizzas = Pizza.objects.all()
print(Pizzas)
Toppings = Topping.objects.all()
print(Toppings)

#for p in Pizzas:
    #print(p.text)

#for t in Toppings:
    #print(t.pizza)
   # print(t.topping_name)



