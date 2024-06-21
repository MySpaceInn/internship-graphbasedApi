from django.db import models
from app.model.record import Records

class AttributeValues(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    record = models.ForeignKey(Records, related_name='attributes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name