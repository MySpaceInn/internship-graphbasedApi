from django.contrib import admin
from app.model.attributevalue import AttributeValues
from app.model.record import Records
# from project.app.model.user import MyUser

# Register your models here.
admin.site.register(AttributeValues)
admin.site.register(Records)
# admin.site.register(MyUser)