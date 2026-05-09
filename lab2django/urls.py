from django.urls import path

from . import views
app_name = "lab1django"

urlpatterns = [
    path("carts/",views.carts,name='carts')
]
