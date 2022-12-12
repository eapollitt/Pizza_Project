from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'pizzas'


urlpatterns = [
    path('', views.home, name='home'),
    path('pizza-menu/', views.pizza_menu, name='pizza_menu'),
    path('pizza-details/<int:pizza_id>/', views.pizza_details, name='pizza_details'),
    path('pizza/<int:pizza_id>/comment/', views.add_comment, name='add_comment'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



