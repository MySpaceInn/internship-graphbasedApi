from django.db import models

class Records(models.Model):
    id = models.AutoField(primary_key=True)
    record_model = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name