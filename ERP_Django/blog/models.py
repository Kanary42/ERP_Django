from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
import os


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.serial_num, instance.id, ext)
    return os.path.join('instance.model._meta', filename)


class Purchaser(models.Model):
    purchaser = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.purchaser)


class Instrument(models.Model):
    name = models.CharField(max_length=100)


class WeldMaterial(models.Model):
    CATEGORY_CHOICES = [(1, 'Wire'),
                        (2, 'Powder')]
    material = models.TextField()
    category = models.CharField(max_length=1,
                                choices=CATEGORY_CHOICES)
    mass = models.IntegerField()
    date_changed = models.DateField(default=timezone.now)


class ShieldingGas(models.Model):
    GAS_CHOICES = [(1, 'Argon'),
                   (2, 'K18')]
    name = models.CharField(max_length=1,
                            choices=GAS_CHOICES)


class LaserComplex(models.Model):
    COMPLEX_CHOICES = [(1, 'LK1'),
                       (2, 'LK2'),
                       (3, 'LK3')]
    name = models.CharField(max_length=1,
                            choices=COMPLEX_CHOICES)


class LaserHead(models.Model):
    HEAD_CHOICES = [(1, 'Wobbler 300 mm'),
                    (2, 'COAX'),
                    (3, '4-side'),
                    (4, 'Wobbler 500 mm'),
                    (5, 'Nittany')]
    name = models.CharField(max_length=1,
                            choices=HEAD_CHOICES)


class LaserWeldingParameters(models.Model):
    material = models.ForeignKey(WeldMaterial,
                                 on_delete=models.RESTRICT)
    power = models.PositiveSmallIntegerField()
    speed = models.PositiveSmallIntegerField()
    mat_speed = models.PositiveSmallIntegerField()
    shielding_gas = models.ForeignKey(ShieldingGas,
                                      on_delete=models.RESTRICT)
    complex = models.ForeignKey(LaserComplex,
                                on_delete=models.RESTRICT)
    head = models.ForeignKey(LaserHead,
                             on_delete=models.RESTRICT)
    welding_height = models.PositiveSmallIntegerField()
    cladding_height = models.DecimalField(max_digits=2,
                                          decimal_places=1)

    def __str__(self):
        return "{}, {}, {}".format(self.material,
                                   self.cladding_height,
                                   self.head)


class Worksite(models.Model):
    SITE_CHOICES = [(1, 'LK1'),
                    (2, 'LK2'),
                    (3, 'LK3'),
                    (4, 'Welding'),
                    (5, 'Fitting'),
                    (6, 'TS1620'),
                    (7, 'FC'),
                    (8, 'RT')]
    site = models.CharField(max_length=1,
                            choices=SITE_CHOICES)


class Post(models.Model):
    STATUS_CHOICES = [
            ('AC', 'Active'),
            ('CA', 'Cancelled'),
            ('PS', 'Postponed'),
            ('HD', 'Hidden'),
            ]
    title = models.CharField(max_length=100)
    content = models.TextField()
    purchaser = models.ForeignKey(Purchaser,
                                  on_delete=models.RESTRICT)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,
                               on_delete=models.RESTRICT,
                               default=1)
    status = models.CharField(max_length=2,
                              choices=STATUS_CHOICES,
                              default='HD')
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)

    def __str__(self):
        return "{}".format(self.title)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Order(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE)
    order_number = models.PositiveBigIntegerField()
    deadline = models.DateField()
    date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.order_number)


class SerialNumber(models.Model):
    order_number = models.ForeignKey(Order,
                                     on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=100,
                                     default='Missing')
    together = models.BooleanField(default=True)

    def __str__(self):
        return str(self.serial_number)


class Ingress(models.Model):
    serial_number = models.ForeignKey(SerialNumber,
                                      on_delete=models.CASCADE)
    received = models.DateField(default=timezone.now)


class ControlInput(models.Model):
    serial_number = models.ForeignKey(SerialNumber,
                                      on_delete=models.CASCADE)
    date_in = models.DateField(default=timezone.now)
    is_accepted_in = models.BooleanField()
    in_file = models.FileField(upload_to='ControlInput/')

    def __str__(self):
        return "{}, {}, {}".format(self.serial_number.order_number,
                                   self.serial_number,
                                   self.date_in)


class ControlOutput(models.Model):
    serial_number = models.ForeignKey(SerialNumber,
                                      on_delete=models.CASCADE)
    date_out = models.DateField(default=timezone.now)
    is_accepted_out = models.BooleanField()
    out_file = models.FileField(upload_to=content_file_name)

    def __str__(self):
        return "{}, {}, {}".format(self.serial_number.order_number,
                                   self.serial_number,
                                   self.date_in)


class WeldMaterialUse(models.Model):
    serial_number = models.ForeignKey(SerialNumber,
                                      on_delete=models.CASCADE)
    date_added = models.DateField(default=timezone.now)
    material = models.ForeignKey(WeldMaterial,
                                 on_delete=models.CASCADE)
    mass = models.IntegerField()
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)


class PenetrantTesting(models.Model):
    serial_number = models.ForeignKey(SerialNumber,
                                      on_delete=models.CASCADE)
    ptfile = models.ImageField(upload_to=content_file_name)


class ChemicalComposition(models.Model):
    serial_number = models.ForeignKey(SerialNumber,
                                      on_delete=models.CASCADE)
    ccfile = models.FileField(upload_to=content_file_name)


class TechCard(models.Model):
    serial_number = models.ForeignKey(SerialNumber,
                                      on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,
                               on_delete=models.RESTRICT)
    laser_parameters = models.ForeignKey(LaserWeldingParameters,
                                         on_delete=models.RESTRICT,
                                         blank=True,
                                         null=True)

    def __str__(self):
        return "{}, {}, {}".format(self.pk,
                               self.serial_number.order_number,
                               self.serial_number)


class TechCardOperations(models.Model):
    tc_number = models.ForeignKey(TechCard,
                                  on_delete=models.CASCADE)
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    content = models.TextField()
    instrument = models.ForeignKey(Instrument,
                                   on_delete=models.RESTRICT,
                                   blank=True,
                                   null=True)


class DayTaskSheet(models.Model):
    date = models.DateField(default=timezone.now)
    SHOP_CHOICES = [(1, 'Laser'),
                    (2, 'Mechanical')]
    shop = models.IntegerField(choices=SHOP_CHOICES)
    shop_master = models.ForeignKey(User,
                                    on_delete=models.RESTRICT)

    class Meta:
        unique_together = ['date', 'shop']

    def __str__(self):
        return "{}, {}".format(self.date,
                               self.get_shop_display())

    def get_absolute_url(self):
        return reverse('daytasksheet-detail', kwargs={'pk': self.pk})


class DayTask(models.Model):
    sheet = models.ForeignKey(DayTaskSheet,
                              on_delete=models.RESTRICT)
    SITE_CHOICES = [(1, 'LK1'),
                    (2, 'LK2'),
                    (3, 'LK3'),
                    (4, 'Welding'),
                    (5, 'Fitting'),
                    (6, 'TS1620'),
                    (7, 'FC'),
                    (8, 'RT')]
    site = models.IntegerField(choices=SITE_CHOICES)
    worker = models.ForeignKey(User,
                               on_delete=models.RESTRICT)
    serial_number = models.ForeignKey(SerialNumber,
                                      on_delete=models.RESTRICT)
    operation = models.ForeignKey(TechCard,
                                  on_delete=models.RESTRICT)
    time = models.PositiveSmallIntegerField()

    def __str__(self):
        return "{}, {}, {}, {}".format(self.sheet.date,
                                       self.get_site_display(),
                                       self.serial_number.order_number,
                                       self.serial_number)
