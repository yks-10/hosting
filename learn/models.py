from django.db import models

# Create your models here.
class Common(models.Model):
    name = models.CharField(max_length=200)
    addhar_no = models.CharField(max_length=200)

    def __str__(self):
        return self.name
