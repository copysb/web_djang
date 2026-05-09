from django.utils.timezone import now
from django.db import models


# Create your models here.
class Pokupatel(models.Model):
    created_at = models.DateField(default=now)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Tovar(models.Model):
    created_at = models.DateField(default=now)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} цена {self.price}P"


class Korzina(models.Model):
    created_at = models.DateField(default=now)
    pokupatel = models.ForeignKey(Pokupatel, on_delete=models.CASCADE)
    tovar = models.ManyToManyField(Tovar)
    is_buyed = models.BooleanField(default=False)

    @property
    def tovar_count(self):
        return self.tovar.count()
