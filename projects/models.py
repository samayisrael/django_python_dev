from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


class ElementType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Element(models.Model):
    name = models.CharField(max_length=100)
    elementtype = models.ForeignKey(ElementType, on_delete=models.CASCADE, default=1)
    daily_target = models.DecimalField(max_digits=11, decimal_places=2, default=0)
    measured_in = models.CharField(max_length=2, default='mg')

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Amount(models.Model):
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
