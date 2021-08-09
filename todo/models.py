from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Todo(models.Model):

    name = models.CharField(max_length=50)
    points = ArrayField(
        ArrayField(
            models.DecimalField(max_digits = 10, decimal_places = 2),
            size=2,
        ),
        size=4,
    )

    def _str_(self):
        return self.name