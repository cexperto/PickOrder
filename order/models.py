from django.db import models


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    latitud_collected = models.DecimalField(max_digits=22, decimal_places=16)
    longitud_collected = models.DecimalField(max_digits=22, decimal_places=16)
    latitud_destiny = models.DecimalField(max_digits=22, decimal_places=16)
    longitud_destiny = models.DecimalField(max_digits=22, decimal_places=16)
    date_order = models.DateField()
    hour = models.CharField(max_length=30)
    driver = models.CharField(max_length=250)

    class Meta:
        managed = True
        ordering = ('id',)
        db_table = 'order'

    def __str__(self):
        return '__all__'