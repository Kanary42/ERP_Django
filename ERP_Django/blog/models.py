from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Order(models.Model):
    order_num = models.PositiveBigIntegerField()
    description = models.TextField()
    deadline = models.DateTimeField(default=timezone.now)
    date_added = models.DateTimeField(default=timezone.now)
    manager = models.ForeignKey(User, on_delete=models.RESTRICT)


class Intake(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    is_accepted = models.BooleanField()
    order_num = models.ForeignKey(Order, on_delete=models.CASCADE)


class WeldMat(models.Model):
    material = models.TextField()
    mass = models.IntegerField()


class WeldMatUse(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    order_num = models.ForeignKey(Order, on_delete=models.CASCADE)
    material = models.ForeignKey(WeldMat, on_delete=models.CASCADE)
    mass = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
