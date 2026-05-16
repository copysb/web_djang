from django.db.models import Sum
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
    tovar = models.ManyToManyField(Tovar,through="Tovar_M")
    is_buyed = models.BooleanField(default=False)

    @property
    def tovar_count(self):
        total = Tovar_M.objects.filter(korzina=self).aggregate(total=Sum("count"))["total"]
        if not total:
            return 0
        return total
    @property
    def total_price(self):
        total = 0
        for tovar in Tovar_M.objects.filter(korzina=self):
            total += tovar.count * tovar.tovar.price
        return total


class Tovar_M(models.Model):
    tovar = models.ForeignKey(Tovar,on_delete=models.CASCADE)
    korzina = models.ForeignKey(Korzina,on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField()
