from django.contrib import admin
from app.model.attributevalue import AttributeValues
from app.model.record import Records

# Register your models here.
admin.site.register(AttributeValues)
admin.site.register(Records)
