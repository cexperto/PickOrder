from django.db import models


HOUR_CHOICES = (
    ("8:00", "8:00"),
    ("9:00", "9:00"),
    ("10:00", "10:00"),
    ("11:00", "11:00"),
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
    ("16:00", "16:00"),
    ("17:00", "17:00"),
    ("18:00", "18:00"),
)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    latitud_collected = models.IntegerField()
    longitud_collected = models.IntegerField()
    latitud_destiny = models.IntegerField()
    longitud_destiny = models.IntegerField()
    date_order = models.DateField()
    hour = models.CharField(max_length=30, choices=HOUR_CHOICES)
    driver = models.CharField(max_length=250)

    class Meta:
        managed = True
        ordering = ("id",)
        db_table = "order"

    def __str__(self):
        return "__all__"
