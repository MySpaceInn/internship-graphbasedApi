from rest_framework import serializers
from app.model.attributevalue import AttributeValues
from app.model.record import Records
from .attribute_serializer import AttributeValueSerializers

class RecordSerializers(serializers.ModelSerializer):
    attributes = AttributeValueSerializers(many=True)

    class Meta:
        model = Records
        fields = ['id', 'record_model', 'type', 'attributes']

    def create(self, validated_data):
        attributes_data = validated_data.pop('attributes')
        record = Records.objects.create(**validated_data)
        for attribute_data in attributes_data:
            AttributeValues.objects.create(record=record, **attribute_data)
        return record