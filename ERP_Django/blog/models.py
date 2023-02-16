from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    STATUS_CHOICES = [
        ('AC', 'Active'),
        ('CA', 'Cancelled'),
        ('PS', 'Postponed'),
        ('HD', 'Hidden'),
    ]
    order_num = models.PositiveBigIntegerField(blank=True,
                                               null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    purchaser = models.CharField(max_length=100,
                                 default='Missing')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,
                               on_delete=models.RESTRICT, default=1)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='HD',
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Order(models.Model):
    order_num = models.ForeignKey(Post,
                                  on_delete=models.RESTRICT,
                                  blank=True,
                                  null=True)
    deadline = models.DateField(blank=True,
                                null=True)
    date_added = models.DateField(default=timezone.now)


class Ingress(models.Model):
    order_num = models.ForeignKey(Order,
                                  on_delete=models.CASCADE)
    received = models.DateField(default=timezone.now)


class Control(models.Model):
    order_num = models.ForeignKey(Order,
                                  on_delete=models.CASCADE)
    date_in = models.DateField(default=timezone.now)
    is_accepted_in = models.BooleanField()
    date_out = models.DateField(default=timezone.now)
    is_accepted_out = models.BooleanField()


class WeldMaterial(models.Model):
    material = models.TextField()
    mass = models.IntegerField()
    date_changed = models.DateField(default=timezone.now)


class WeldMaterialUse(models.Model):
    order_num = models.ForeignKey(Order,
                                  on_delete=models.CASCADE)
    date_added = models.DateField(default=timezone.now)
    material = models.ForeignKey(WeldMaterial,
                                 on_delete=models.CASCADE)
    mass = models.IntegerField()
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
