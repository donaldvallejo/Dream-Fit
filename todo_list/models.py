from django.db import models

class List(models.Model):
     item = models.CharField(max_length=200)
     price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
     quantity = models.IntegerField(default=1)
     completed = models.BooleanField(default=False)

     def __str__(self):
        return self.item + ' | ' + str(self.price) + " | " + str(self.quantity) + " | " + str(self.completed)