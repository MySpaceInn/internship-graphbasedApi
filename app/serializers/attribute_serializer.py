from rest_framework import serializers
from app.model.attributevalue import AttributeValues

class AttributeValueSerializers(serializers.ModelSerializer):
    class Meta:
        model = AttributeValues
        fields = ['id', 'name', 'type', 'value']
