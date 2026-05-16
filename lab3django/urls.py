from django.urls import path

from . import views
app_name = "lab3django"

urlpatterns = [
    path("carts/",views.carts,name='carts')
]
