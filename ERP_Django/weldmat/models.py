from blog.models import Order
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class WeldMat(models.Model):
    material = models.TextField()
    mass = models.IntegerField()


class WeldMatUse(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    order_num = models.ForeignKey(Order, on_delete=models.CASCADE)
    material = models.ForeignKey(WeldMat, on_delete=models.CASCADE)
    mass = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
