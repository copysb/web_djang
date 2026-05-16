from lab3django.models import Korzina
from django.shortcuts import render


# Create your views here.
def carts(request):
    korzinas = Korzina.objects.all()
    return render(request, "lab3django/carts.html", {"korzinas": (korzinas)})
