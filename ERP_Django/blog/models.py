from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Order(models.Model):
    order_num = models.PositiveBigIntegerField(blank=True, null=True)
    description = models.TextField()
    deadline = models.DateTimeField(default=timezone.now)
    date_added = models.DateTimeField(default=timezone.now)
    manager = models.ForeignKey(User, on_delete=models.RESTRICT)


class Post(models.Model):
    STATUS_CHOICES = [
        ('AC', 'Active'),
        ('CA', 'Cancelled'),
        ('PS', 'Postponed'),
        ('HD', 'Hidden'),
    ]
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    order_num = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='HD',
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Ingress(models.Model):
    received = models.DateTimeField(default=timezone.now)
    order_num = models.ForeignKey(Order, on_delete=models.CASCADE)


class Control(models.Model):
    date_in = models.DateTimeField(default=timezone.now)
    is_accepted_in = models.BooleanField()
    date_out = models.DateTimeField(default=timezone.now)
    is_accepted_out = models.BooleanField()
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


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)
    content = models.TextField()
