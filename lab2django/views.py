from lab2django.models import Korzina
from django.shortcuts import render


# Create your views here.
def carts(request):
    korzinas = Korzina.objects.all()
    return render(request, "lab2django/carts.html", {"korzinas": (korzinas)})
